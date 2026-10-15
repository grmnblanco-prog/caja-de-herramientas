# Caja de Herramientas — PropulsarIA

[![Live Demo](https://img.shields.io/badge/demo-grmnblanco--prog.github.io%2Fcaja--de--herramientas-E8633A?style=flat-square&logo=githubpages)](https://grmnblanco-prog.github.io/caja-de-herramientas/)
[![Recursos](https://img.shields.io/badge/recursos-144-blue?style=flat-square)](#)
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
| Enlaces abandonados | Se verifica que cada repositorio siga vivo antes de incluirlo |
| Trucos sin comprobar | Los trucos que se documentan se prueban antes de publicarse |

---

## Kits de implementación

Los **144 recursos** se agrupan en **10 kits temáticos**. La asignación no se mantiene a mano: cada kit se calcula cruzando las etiquetas, aplicaciones y categoría de cada recurso, así que un recurso nuevo entra solo al kit que le corresponde.

| Kit | Recursos | Ejemplos |
|:----|:---------|:---------|
| 🔧 Configuración de Agentes | 67 | Karpathy Rules, Superpowers, Hermes Agent, OpenClaw, Composio |
| 📋 Gestión de Clientes y CRM | 11 | Chatwoot, Twenty CRM, DeskcommCRM, OpenWA, WAHA |
| 🤖 Automatización de Procesos | 22 | n8n, ToolJet, Browser Use, Super Productivity, scrcpy |
| 📈 Marketing y Contenido | 19 | Marketing Skills, MoneyPrinterTurbo, OpenSERP, Social Media Research Skills, no-ai-slop |
| 🎨 Diseño y UI | 39 | UI/UX Pro Max, Excalidraw, DESIGN.md, Screenshot to Code, taste-skill |
| 🗄️ Datos y Conocimiento | 41 | Docling, MarkItDown, Firecrawl, Crawl4AI, Graphify |
| 🔒 Seguridad y Cumplimiento | 9 | Strix, Anthropic Cybersecurity Skills, Cloudflare Security Audit, OpenSign |
| ☁️ Infraestructura y Hosting | 44 | Ollama, llama.cpp, Open WebUI, vLLM, Coolify |
| 🧠 Consulting y Estrategia | 17 | Management Consulting, McKinsey-style Visualization, Wondelai Skills, Agentic Business Analysis, Slavingia Skills |
| 🎓 Aprendizaje y Capacitación | 14 | Train LLM from Scratch, Humanizer, Matt Pocock Skills, Unsloth, Aider |

Un recurso puede pertenecer a más de un kit: muchas herramientas sirven para varias necesidades a la vez.

---

## Stack técnico

- **Frontend:** HTML + CSS + JavaScript vanilla (sin dependencias)
- **Datos:** JSON plano (única fuente de verdad)
- **Infraestructura:** GitHub Pages (hosting gratuito, CDN global)
- **Integración:** compatible con Obsidian (notas .md generadas desde el JSON)
- **Idiomas:** español (por defecto) / inglés (conmutador)
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

Los cambios se hacen en el JSON y se propagan. Nunca al revés. Las vistas que dependen de los datos —kits, filtro de aplicación, índices— se generan a partir del JSON en tiempo de ejecución, de modo que no hay listas que se desincronicen.

---

## Licencia

MIT — haz lo que quieras con esto. Si te sirve, una estrella es suficiente.

---

*Curado y mantenido por [PropulsarIA](https://estrateg-ia-xi.vercel.app) — Consultoría en Implementación de IA.*
