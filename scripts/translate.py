import re

with open("C:/Users/User/Desktop/caja-de-herramientas/index.html", encoding="utf-8") as f:
    html = f.read()

# Replace "No hay recursos" message in render function
old = "<h3>No hay recursos</h3><p>Agrega recursos desde Hermes o carga un archivo JSON con el boton &quot;Cargar JSON&quot;.</p>"
new = "<h3>' + __(\"no_recursos_tit\") + '</h3><p>' + __(\"no_recursos_desc\") + '</p>"
html = html.replace(old, new)

# Replace static field labels in render function
pairs = [
    ("'Para que sirve'", "' + __('para_que') + '"),
    ("'Por que se recomienda'", "' + __('por_que') + '"),
    ("'Casos de uso'", "' + __('casos_uso') + '"),
    ("'Pasos para implementar'", "' + __('pasos_impl') + '"),
    ("'Modelos limitados'", "' + __('modelos_lim') + '"),
    ("'Es agnostic0'", "' + __('es_agnostico') + '"),
    ("'Como hacerlo agnostic0'", "' + __('como_agnostico') + '"),
    ("'Notas'", "' + __('notas') + '"),
    ("'Sub-recursos'", "' + __('sub_recursos') + '"),
    ("'Detalle'", "' + __('detalle') + '"),
    ("'URL'", "' + __('url') + '"),
    ("'Licencia'", "' + __('licencia') + '"),
    ("'Estrellas'", "' + __('estrellas') + '"),
    ("'Fecha guardado'", "' + __('fecha_guardado') + '"),
    ("'Ultimo commit'", "' + __('ultimo_commit') + '"),
    ("'Fuente'", "' + __('fuente') + '"),
    ("'Tags'", "' + __('tags') + '"),
    ("'Abrir repo ↗'", "' + __('abrir_repo') + ' ↗'"),
    ("'⚠ Limitado a:'", "'⚠ ' + __('limitado_a') + '"),
    ("'✓ Agnostic0'", "'✓ ' + __('agnostic0')"),
]

for old, new in pairs:
    html = html.replace(old, new)

# Fix statusLabel function
html = html.replace(
    'return { nuevo: "Nuevo", "pendiente-probar": "Pendiente", probado: "Probado", recomendado: "Recomendado", descartado: "Descartado" }[e] || e;',
    'var m = { nuevo: __("nuevo"), "pendiente-probar": __("pendiente"), probado: __("probado"), recomendado: __("recomendado"), descartado: __("descartado") }; return m[e] || e;'
)

# Fix "Si"/"No" 
html = html.replace(
    'r.es_agnostico ? "Si" : "No"',
    'r.es_agnostico ? __("si") : __("no")'
)

# Fix count bar
html = html.replace(
    'recursos.length + " recursos (" + filtrados.length + " filtrados)"',
    'recursos.length + " " + __("recursos") + " (" + filtrados.length + " " + __("filtrados") + ")"'
)

# Fix filter option "Todos"
html = html.replace(
    '<option value="">Todos</option>',
    '<option value="">' + 'Todos' + '</option>'
)

# Kit modal
html = html.replace(
    '"<h2>Kits de implementacion</h2>"',
    '"<h2>" + __("kit_tit") + "</h2>"'
)

html = html.replace(
    '"Recursos agrupados segun la necesidad de implementacion."',
    '" + __("kit_desc") + "'
)

with open("C:/Users/User/Desktop/caja-de-herramientas/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("All replacements done")
