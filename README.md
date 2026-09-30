# Caja de Herramientas — PropulsarIA

[![Live Demo](https://img.shields.io/badge/demo-grmnblanco--prog.github.io%2Fcaja--de--herramientas-E8633A?style=flat-square&logo=githubpages)](https://grmnblanco-prog.github.io/caja-de-herramientas/)
[![Recursos](https://img.shields.io/badge/recursos-92-blue?style=flat-square)](#)
[![Licencia](https://img.shields.io/badge/licencia-MIT-green?style=flat-square)](#)
[![Obsidian](https://img.shields.io/badge/Obsidian-vault-7C3AED?style=flat-square&logo=obsidian)](#)

**Biblioteca viva, navegable y filtrable de herramientas, frameworks, skills y recursos de IA para implementación.** Clasificada por tipo, aplicación, nivel de madurez y agrupada en **Kits de implementación** según la necesidad concreta del proyecto.

> Una lista curada no es suficiente. Cada recurso incluye: para qué sirve, por qué se recomienda, casos de uso concretos con cómo implementarlo, compatibilidad con modelos, y pasos para hacerlo agnóstico cuando está limitado a un ecosistema.

---

## Demo en vivo

👉 **[https://grmnblanco-prog.github.io/caja-de-herramientas/](https://grmnblanco-prog.github.io/caja-de-herramientas/)**

Filtra por tipo, estado, nivel, aplicación. Explora por Kits de implementación. Sin registro, sin backend, sin anuncios.

---

## ¿Qué hace diferente a esta biblioteca?

| Otras listas curadas | Caja de Herramientas |
|:---------------------|:---------------------|
| Lista plana de enlaces | Filtrable por tipo, estado, nivel y aplicación |
| Sin criterio de uso | Cada recurso tiene: para qué sirve, por qué se recomienda, casos de uso con cómo implementarlo |
| Ignoran compatibilidad | Indica si funciona con Claude, Codex, Gemini o es agnóstico |
| Sin contexto de implementación | Agrupado en **Kits** (Configuración de Agentes, CRM, Marketing, Infraestructura...) |
| Estáticas | Se actualiza desde GitHub — los datos viajan con el repo |
| Solo para developers | Clasificado para consultores, implementadores y tomadores de decisión |

---

## Kits de implementación

Los 92 recursos están agrupados en 10 kits según la necesidad de implementación:

| Kit | Recursos |
|:----|:---------|
| 🔧 Configuración de Agentes | Karpathy Rules, Super Powers, Firecrawl, Caveman, Agent Reach, Browser Use, Composio... |
| 📋 Gestión de Clientes y CRM | Chatwoot, Twenty CRM, DeskcommCRM, OpenWA |
| 🤖 Automatización de Procesos | n8n, ToolJet, Agent Zero, SuperAGI, OmniAgents |
| 📈 Marketing y Contenido | Marketing Skills, Remotion, MoneyPrinterTurbo, OpenSerp |
| 🎨 Diseño y UI | DESIGN.md, Screenshot to Code, Excalidraw, Understand Anything |
| 🗄️ Datos y Conocimiento | Matrixone, Docling, Graphify, Codebase Memory MCP |
| 🔒 Seguridad | Strix, Anthropic Cybersecurity, Cloudflare Auditor |
| ☁️ Infraestructura | Coolify, Ollama, Open WebUI, vLLM, Exo |
| 🧠 Consulting y Estrategia | Management Consulting, McKinsey Visualization, Wondelai Skills |
| 🎓 Aprendizaje | Train LLM from Scratch, Scientific Agent Skills, Humanizer |

---

## Stack técnico

- **Frontend:** HTML + CSS + JavaScript vanilla (sin dependencias)
- **Datos:** JSON plano (única fuente de verdad)
- **Infraestructura:** GitHub Pages (hosting gratuito, CDN global)
- **Integración:** compatible con Obsidian (notas .md generadas desde el JSON)
- **Licencia:** MIT

---

## Cómo contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para agregar recursos, corregir datos o mejorar la interfaz.

---

## Arquitectura

```
biblioteca_recursos.json   ← FUENTE ÚNICA
        │
        ├──► index.html              (vista navegable, auto-contenida)
        └──► Obsidian vault          (notas .md + índices + kits)
```

Los cambios se hacen en el JSON y se propagan. Nunca al revés.

---

## Licencia

MIT — haz lo que quieras con esto. Si te sirve, una estrella es suficiente.

---

*Curado y mantenido por [PropulsarIA](https://estrateg-ia-xi.vercel.app) — Consultoría en Implementación de IA.*
