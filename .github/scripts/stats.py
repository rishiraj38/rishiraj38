"""Generate self-hosted GitHub stats + top-languages cards as SVGs.

Runs in GitHub Actions with GITHUB_TOKEN, so the README doesn't depend on
third-party stats servers that go down or get rate-limited.
"""
import json
import os
import sys
import urllib.request
from html import escape

USER = os.environ.get("GH_USER", "rishiraj38")
OUT = sys.argv[1] if len(sys.argv) > 1 else "dist"
HIDE = {"c#", "powershell", "mathematica", "ruby", "objective-c", "objective-c++", "cuda", "plpgsql", "jupyter notebook"}

BG, BORDER, TEXT, MUTED, GREEN, ORANGE = "#0d1117", "#30363d", "#ffffff", "#8b949e", "#79ff97", "#ff6b35"
FONT = "Segoe UI, Ubuntu, -apple-system, sans-serif"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection { totalCommitContributions restrictedContributionsCount totalPullRequestReviewContributions }
    pullRequests { totalCount }
    merged: pullRequests(states: MERGED) { totalCount }
    issues { totalCount }
    repositories(ownerAffiliations: OWNER, isFork: false, first: 100) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name color } } }
      }
    }
  }
}"""


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    if "errors" in data:
        sys.exit(f"GraphQL error: {data['errors']}")
    return data["data"]["user"]


def fmt(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def card(w, h, title, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>
<text x="25" y="38" fill="{TEXT}" font-size="18" font-weight="600">{escape(title)}</text>
{body}
</svg>"""


def stats_svg(u):
    c = u["contributionsCollection"]
    prs, merged = u["pullRequests"]["totalCount"], u["merged"]["totalCount"]
    rows = [
        ("Commits (last year)", c["totalCommitContributions"] + c["restrictedContributionsCount"]),
        ("PRs reviewed (last year)", c["totalPullRequestReviewContributions"]),
        ("Pull requests", prs),
        ("PRs merged", merged),
        ("Merge rate", f"{round(merged / prs * 100) if prs else 0}%"),
        ("Issues opened", u["issues"]["totalCount"]),
        ("Stars earned", sum(r["stargazerCount"] for r in u["repositories"]["nodes"])),
    ]
    body = []
    for i, (label, val) in enumerate(rows):
        y = 72 + i * 25
        val = fmt(val) if isinstance(val, int) else val
        body.append(
            f'<circle cx="31" cy="{y - 5}" r="4" fill="{GREEN}"/>'
            f'<text x="45" y="{y}" fill="{MUTED}" font-size="14">{label}</text>'
            f'<text x="440" y="{y}" fill="{TEXT}" font-size="14" font-weight="600" text-anchor="end">{val}</text>'
        )
    return card(465, 245, "GitHub Stats", "\n".join(body))


def langs_svg(u):
    totals, colors = {}, {}
    for repo in u["repositories"]["nodes"]:
        for e in repo["languages"]["edges"]:
            name = e["node"]["name"]
            if name.lower() in HIDE:
                continue
            totals[name] = totals.get(name, 0) + e["size"]
            colors[name] = e["node"]["color"] or MUTED
    top = sorted(totals.items(), key=lambda kv: -kv[1])[:8]
    total = sum(s for _, s in top) or 1

    body, x = ['<clipPath id="bar"><rect x="25" y="58" width="415" height="10" rx="5"/></clipPath><g clip-path="url(#bar)">'], 25.0
    for name, size in top:
        w = size / total * 415
        body.append(f'<rect x="{x:.2f}" y="58" width="{w + 0.5:.2f}" height="10" fill="{colors[name]}"/>')
        x += w
    body.append("</g>")
    for i, (name, size) in enumerate(top):
        col, row = i % 2, i // 2
        cx, cy = 31 + col * 215, 100 + row * 32
        body.append(
            f'<circle cx="{cx}" cy="{cy - 5}" r="5" fill="{colors[name]}"/>'
            f'<text x="{cx + 14}" y="{cy}" fill="{TEXT}" font-size="14">{escape(name)}</text>'
            f'<text x="{cx + 190}" y="{cy}" fill="{MUTED}" font-size="13" text-anchor="end">{size / total * 100:.1f}%</text>'
        )
    return card(465, 245, "Top Languages", "\n".join(body))


if __name__ == "__main__":
    user = json.load(open(os.environ["MOCK"])) if os.environ.get("MOCK") else fetch()
    os.makedirs(OUT, exist_ok=True)
    open(f"{OUT}/stats.svg", "w").write(stats_svg(user))
    open(f"{OUT}/langs.svg", "w").write(langs_svg(user))
    print("wrote stats.svg and langs.svg")
