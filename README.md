<p align="center">
  <img src="./assets/header.svg" width="100%" alt="Rishi Raj — Open source, systems in Go, machine learning" />
</p>

<p align="center">
  <a href="https://rishiraj38.github.io"><img src="https://img.shields.io/badge/Portfolio-0d1117?style=for-the-badge&logo=googlechrome&logoColor=79ff97" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/rishi-raj-3488432ab/"><img src="https://img.shields.io/badge/LinkedIn-0d1117?style=for-the-badge&logo=linkedin&logoColor=0A66C2" alt="LinkedIn" /></a>
  <a href="https://leetcode.com/u/rishiraj438/"><img src="https://img.shields.io/badge/LeetCode-0d1117?style=for-the-badge&logo=leetcode&logoColor=FFA116" alt="LeetCode" /></a>
  <a href="https://github.com/meshery"><img src="https://img.shields.io/badge/Meshery-0d1117?style=for-the-badge&logo=cncf&logoColor=00B39F" alt="Meshery" /></a>
</p>

---

## 👋 About me

I'm a third-year CS & AI student at **Newton School of Technology** who likes building things from the ground up and understanding how they actually work underneath.

I spent a good chunk of my time in open source as a **maintainer across Meshery** (a CNCF project), and did my **LFX mentorship** there adding OCI registry support for Meshery models. These days I'm writing systems code in Go, like a vector database built from scratch, and going deep on machine learning.

- 🔭 Building **[quiver](https://github.com/rishiraj38/quiver)**, a vector database in pure Go
- 🧠 Working through a long-term ML roadmap: maths, classical ML, deep learning, research papers
- 🤝 Open to internships in backend, infra and ML engineering

---

## 💼 Experience

<table>
<tr>
<td width="80" align="center" valign="top">
  <a href="https://lfx.linuxfoundation.org/tools/mentorship/"><img src="https://github.com/cncf.png" width="56" alt="CNCF" /></a>
</td>
<td valign="top">

**LFX Mentee · CNCF / Meshery** &nbsp;·&nbsp; *2026 Term 2*<br/>
<sub>Models Support for OCI Registries · Linux Foundation Mentorship</sub>

Added support for storing and distributing Meshery models through OCI registries, so models can be pushed and pulled the same way as container images.

- Built OCI/ORAS-based model registry support in Meshery
- Worked hands-on with the OCI spec: blobs, manifests, digests, media types and multi-platform images

</td>
</tr>
<tr>
<td width="80" align="center" valign="top">
  <a href="https://github.com/meshery"><img src="https://github.com/meshery.png" width="56" alt="Meshery" /></a>
</td>
<td valign="top">

**Maintainer · Meshery (CNCF / Layer5)** &nbsp;·&nbsp; *Graduated 2026*<br/>
<sub>Meshery UI · Meshery Cloud · Kanvas · Sistent · Schemas</sub>

- **300+** PRs reviewed, **100+** merged as maintainer, **100+** of my own PRs merged
- Led the permission-shield migration across Meshery UI, Meshery Cloud and Kanvas, moving permission checks into Sistent so consumer repos only pass a permission key and action
- Drove the "evaluate design" permission key end to end, from `meshery/schemas` to `meshery/meshery`

</td>
</tr>
</table>

---

## 🚀 Featured Projects

<table>
<tr>
<td width="50%" valign="top">

### [⚡ quiver](https://github.com/rishiraj38/quiver)
Vector database written from scratch in Go with **zero third-party dependencies**. HNSW index, write-ahead log with group commit, snapshots and crash recovery.

- **0.99 recall@10** at ~3.8k QPS per core on SIFT1M, between FAISS and hnswlib
- Hand-written **ARM64 NEON** kernels, 2.5× faster than compiled Go
- Group commit took durable writes from 420 to **14,900/sec**

<img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" /> <img src="https://img.shields.io/badge/ARM64_NEON-0d1117?style=flat-square&logo=arm&logoColor=white" /> &nbsp;[**Live demo →**](https://quiver-i5qu.onrender.com)

</td>
<td width="50%" valign="top">

### [📰 Helix](https://github.com/rishiraj38/news-aggregator)
Autonomous news pipeline that runs unattended every day. It pulls ~400 articles from 13 sources, summarises them with an LLM, ranks them per subscriber and sends a personalised email.

- Auto-posts top stories as an Instagram carousel
- Runs on a GitHub Actions cron, no server to babysit
- Next.js dashboard with Clerk auth and Prisma

<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" /> <img src="https://img.shields.io/badge/Groq-f55036?style=flat-square" /> <img src="https://img.shields.io/badge/Prisma-2D3748?style=flat-square&logo=prisma&logoColor=white" /> &nbsp;[**Live →**](https://helix-seven-eta.vercel.app)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [🚑 OpenEnv RL Environments](https://huggingface.co/spaces/rishi38/SmartCity-Emergency-Dispatch)
**Finalist, Meta × Hugging Face OpenEnv Hackathon.** Built two reinforcement learning environments: Smart City Emergency Dispatch and Email Triage.

- Five-component reward and Dijkstra-based dispatch routing
- SFT + GRPO training pipeline targeting Qwen2.5-7B-Instruct

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" /> <img src="https://img.shields.io/badge/RL-GRPO-0d1117?style=flat-square" />

</td>
<td width="50%" valign="top">

### [🎤 AeroPrep](https://github.com/rishiraj38/AeroPrep)
AI mock-interview platform that runs realistic interview sessions and gives feedback on your answers.

- Full-stack app with Next.js frontend and Express API
- Prisma on NeonDB serverless Postgres

<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" /> <img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" /> &nbsp;[**Live →**](https://ai-interview-coach-eight-mu.vercel.app)

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

**Languages**<br/>
<img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" /> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />

**Cloud Native & DevOps**<br/>
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/OCI_/_ORAS-262261?style=for-the-badge&logo=opencontainersinitiative&logoColor=white" /> <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" /> <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" /> <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logoColor=FF9900" />

**Backend & Data**<br/>
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" /> <img src="https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" /> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" /> <img src="https://img.shields.io/badge/Prisma-2D3748?style=for-the-badge&logo=prisma&logoColor=white" />

**AI / ML**<br/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" /> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" /> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" /> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" /> <img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge&logo=meta&logoColor=white" /> <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />

**Frontend**<br/>
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" /> <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" /> <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" />

---

## 🏆 Achievements

<table>
<tr>
<td width="200" align="center">
  <a href="https://cloud.layer5.io/user/5f456e61-75ed-4789-8c59-56cb3beb9ca2?tab=badges&badge=certified-meshery-contributor">
    <img src="https://badges.layer5.io/assets/badges/certified-meshery-contributor/certified-meshery-contributor.png" width="140" alt="Certified Meshery Contributor" />
  </a>
</td>
<td valign="middle">

- 🎓 **LFX Mentee**, CNCF – Meshery: Models Support for OCI Registries (2026 Term 2)
- 🛡️ **Former Meshery Maintainer**: 300+ PRs reviewed across the project
- 🏅 **Certified Meshery Contributor**, Layer5
- 🥈 **Finalist**, Meta × Hugging Face OpenEnv Hackathon
- 💻 **LeetCode**: 1551 contest rating, 360+ problems solved

</td>
</tr>
</table>

---

## 📊 GitHub Activity

<p align="center">
  <img src="https://raw.githubusercontent.com/rishiraj38/rishiraj38/output/stats.svg" height="190" alt="GitHub Stats" />
  &nbsp;
  <img src="https://raw.githubusercontent.com/rishiraj38/rishiraj38/output/langs.svg" height="190" alt="Top Languages" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=rishiraj38&background=0d1117&border=30363d&stroke=30363d&ring=ff6b35&fire=ff6b35&currStreakNum=ffffff&sideNums=ffffff&currStreakLabel=ff6b35&sideLabels=79ff97&dates=8b949e" alt="GitHub Streak Stats" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/rishiraj38/rishiraj38/output/github-snake-dark.svg" alt="GitHub Contribution Snake" />
</p>

---

<p align="center">
  <b>Let's build something.</b> Reach out on <a href="https://www.linkedin.com/in/rishi-raj-3488432ab/">LinkedIn</a> or check out my <a href="https://rishiraj38.github.io">portfolio</a>.
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=rishiraj38&color=0d1117&style=flat-square&label=profile+views" alt="Profile views" />
</p>
