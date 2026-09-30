# Cómo contribuir

Gracias por tu interés en la Caja de Herramientas. Hay dos formas principales de contribuir.

## 1. Agregar un recurso

### Opción A — Abrir un Issue (recomendada)

1. Ve a [Issues](https://github.com/grmnblanco-prog/caja-de-herramientas/issues)
2. Haz clic en "New Issue"
3. Usa la plantilla "Agregar recurso" (si existe) o incluye:
   - Nombre del recurso
   - URL del repositorio o sitio web
   - Breve descripción
   - Tipo (Framework, Herramienta, Skill, CRM, etc.)
   - Aplicación (desarrollo, marketing, seguridad, etc.)
   - Casos de uso

### Opción B — Enviar un Pull Request

Si quieres editar el JSON directamente:

1. Haz fork del repo
2. Edita `biblioteca_recursos.json`
3. Agrega el nuevo recurso siguiendo la estructura existente:

```json
{
  "id": "nombre-slug",
  "nombre": "Nombre del Recurso",
  "url": "https://github.com/usuario/repo",
  "descripcion": "Breve descripción",
  "para_que_sirve": "Para qué se usa en implementaciones",
  "por_que_se_recomienda": "Por qué está en la biblioteca",
  "casos_de_uso": [
    "Caso de uso 1 con cómo implementarlo",
    "Caso de uso 2 con cómo implementarlo"
  ],
  "pasos_implementacion": [
    "Paso 1 concreto",
    "Paso 2 concreto"
  ],
  "compatibilidad_modelos": "Claude, Codex, Gemini o Agnóstico",
  "modelo_limitado": false,
  "aplicaciones": ["categoria1", "categoria2"],
  "tipo": "Framework | Herramienta | Skill | CRM | ...",
  "estrellas": 12345,
  "licencia": "MIT",
  "estado": "nuevo",
  "nivel": "N1 | N2 | N3 | N4",
  "fuente": "github | linkedin | youtube | ...",
  "notas": "",
  "sub_recursos": []
}
```

4. Envía el PR

## 2. Mejorar la interfaz

El HTML es vanilla JS sin dependencias. Si quieres mejorar los filtros, la visualización o agregar funcionalidad:

1. Haz fork del repo
2. Edita `index.html`
3. Envía un PR describiendo el cambio

## 3. Reportar problemas

Si un enlace está roto, un recurso está desactualizado o un filtro no funciona:

1. Ve a [Issues](https://github.com/grmnblanco-prog/caja-de-herramientas/issues)
2. Describe el problema (incluye captura de pantalla si aplica)

## Criterios de inclusión

- **Recursos de IA aplicada** (frameworks, herramientas, skills, plataformas, bases de conocimiento)
- **Preferencia open-source** (MIT, Apache 2.0, GPL)
- **Que tenga documentación** (README, ejemplos, casos de uso)
- **Que sea implementable** (no solo conceptual, sino accionable)

---

*Gracias por hacer crecer esta biblioteca.*
