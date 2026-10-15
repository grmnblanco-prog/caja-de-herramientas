# Toolbox — PropulsarIA

[![Live Demo](https://img.shields.io/badge/demo-grmnblanco--prog.github.io%2Ftoolbox-E8633A?style=flat-square&logo=githubpages)](https://grmnblanco-prog.github.io/caja-de-herramientas/)
[![Resources](https://img.shields.io/badge/resources-141-blue?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](#)
[![Obsidian](https://img.shields.io/badge/Obsidian-vault-7C3AED?style=flat-square&logo=obsidian)](#)

**A living, filterable library of AI tools, frameworks, skills, and resources for implementation.** Classified by type, application, maturity level, and grouped into **Implementation Kits** based on the specific project need.

> A curated list is not enough. Each resource includes: what it does, why it's recommended, concrete use cases with how to implement, model compatibility, and steps to make it agnostic when limited to a specific ecosystem.

---

## Live Demo

👉 **[https://grmnblanco-prog.github.io/caja-de-herramientas/](https://grmnblanco-prog.github.io/caja-de-herramientas/)**

Filter by type, status, level, category. Explore by Implementation Kits. No registration, no backend, no ads.

---

## What makes this different

| Other curated lists | This Toolbox |
|:--------------------|:-------------|
| Flat link list | Filterable by type, status, level, and category |
| No usage criteria | Each resource has: what it does, why recommended, use cases with how-to |
| Ignore compatibility | Shows Claude, Codex, Gemini compatibility or agnostic status |
| No implementation context | Grouped into **Kits** (Agent Setup, CRM, Marketing, Infrastructure...) |
| Static | Updated from GitHub — data travels with the repo |
| Dev-only | Classified for consultants, implementers, and decision-makers |
| Dead links | Every repository is checked to be still maintained before inclusion |

---

## Implementation Kits

The **141 resources** are grouped into **10 thematic kits**. The assignment is not maintained by hand: each kit is computed by matching every resource's tags, applications, and category, so a new resource joins its kit on its own.

| Kit | Resources | Examples |
|:----|:----------|:---------|
| 🔧 Agent Configuration | 57 | Superpowers, Karpathy Rules, Caveman, Browser Use, Composio |
| 📋 CRM & Client Management | 17 | Chatwoot, Twenty CRM, DeskcommCRM, OpenWA, WAHA |
| 🤖 Process Automation | 26 | n8n, ToolJet, Agent Zero, SuperAGI, Crawlee |
| 📈 Marketing & Content | 20 | Marketing Skills, MoneyPrinterTurbo, OpenSERP, Remotion, Social Media Research Skills |
| 🎨 Design & UI | 36 | UI/UX Pro Max, Excalidraw, DESIGN.md, Screenshot to Code, taste-skill |
| 🗄️ Data & Knowledge | 33 | Docling, MarkItDown, Firecrawl, Crawl4AI, Graphify |
| 🔒 Security & Compliance | 9 | Strix, Anthropic Cybersecurity Skills, Cloudflare Security Audit |
| ☁️ Infrastructure & Hosting | 46 | Ollama, llama.cpp, Open WebUI, vLLM, Coolify |
| 🧠 Consulting & Strategy | 22 | Management Consulting, McKinsey-style Visualization, Wondelai Skills, Agentic Business Analysis |
| 🎓 Learning & Training | 14 | Train LLM from Scratch, Scientific Agent Skills, Humanizer, Matt Pocock Skills |

A resource may belong to more than one kit: many tools serve several needs at once.

---

## Tech stack

- **Frontend:** HTML + CSS + vanilla JavaScript (no dependencies)
- **Data:** Flat JSON (single source of truth)
- **Infrastructure:** GitHub Pages (free hosting, global CDN)
- **Integration:** Obsidian-compatible (.md notes generated from JSON)
- **License:** MIT
- **Languages:** Spanish (default) / English (toggle)

---

## Architecture

```
biblioteca_recursos.json   ← SINGLE SOURCE OF TRUTH
        │
        ├──► index.html              (browsable, self-contained, bilingual)
        └──► Obsidian vault          (.md notes + indexes + kits)
```

Changes are made in the JSON and propagated. Never the other way around. Views that depend on the data — kits, application filter, indexes — are generated from the JSON at runtime, so there are no lists that can drift out of sync.

---

## License

MIT — do whatever you want with this. If it helps, a star is enough.

---

*Curated and maintained by [PropulsarIA](https://estrateg-ia-xi.vercel.app) — AI Implementation Consulting.*
