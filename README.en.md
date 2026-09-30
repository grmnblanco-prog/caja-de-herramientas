# Toolbox — PropulsarIA

[![Live Demo](https://img.shields.io/badge/demo-grmnblanco--prog.github.io%2Ftoolbox-E8633A?style=flat-square&logo=githubpages)](https://grmnblanco-prog.github.io/caja-de-herramientas/)
[![Resources](https://img.shields.io/badge/resources-92-blue?style=flat-square)](#)
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

---

## Implementation Kits

The 92 resources are grouped into 10 kits by implementation need:

| Kit | Resources |
|:----|:----------|
| 🔧 Agent Configuration | Karpathy Rules, Super Powers, Firecrawl, Caveman, Agent Reach, Browser Use, Composio... |
| 📋 CRM & Client Management | Chatwoot, Twenty CRM, DeskcommCRM, OpenWA |
| 🤖 Process Automation | n8n, ToolJet, Agent Zero, SuperAGI, OmniAgents |
| 📈 Marketing & Content | Marketing Skills, Remotion, MoneyPrinterTurbo, OpenSerp |
| 🎨 Design & UI | DESIGN.md, Screenshot to Code, Excalidraw, Understand Anything |
| 🗄️ Data & Knowledge | Matrixone, Docling, Graphify, Codebase Memory MCP |
| 🔒 Security | Strix, Anthropic Cybersecurity, Cloudflare Auditor |
| ☁️ Infrastructure | Coolify, Ollama, Open WebUI, vLLM, Exo |
| 🧠 Consulting & Strategy | Management Consulting, McKinsey Visualization, Wondelai Skills |
| 🎓 Learning | Train LLM from Scratch, Scientific Agent Skills, Humanizer |

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

Changes are made in the JSON and propagated. Never the other way around.

---

## License

MIT — do whatever you want with this. If it helps, a star is enough.

---

*Curated and maintained by [PropulsarIA](https://estrateg-ia-xi.vercel.app) — AI Implementation Consulting.*
