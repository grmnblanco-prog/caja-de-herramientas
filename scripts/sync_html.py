# -*- coding: utf-8 -*-
"""Sincroniza el bloque de recursos embebido en index.html a partir del JSON.

El JSON (biblioteca_recursos.json) es la FUENTE UNICA DE VERDAD.
El HTML se DERIVA: nunca se edita a mano el bloque de recursos.

Uso:
    python scripts/sync_html.py            # reescribe el bloque del HTML
    python scripts/sync_html.py --check    # no escribe; sale con 1 si estan desincronizados

Que hace exactamente:
    localiza  var recursos = [ ... ];  en index.html, vuelca cada registro del JSON
    con el mismo formato que usa el archivo (claves en el orden del JSON, separadores
    ", " y ": ", sin escapar caracteres no ASCII) y reemplaza solo ese bloque.

Por que existe:
    Antes el JSON y el HTML se editaban a mano por separado. Eso ya produjo
    divergencias (fichas corregidas en un lado y no en el otro). Este script
    elimina esa clase de error.
"""
import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_PATH = RAIZ / "biblioteca_recursos.json"
HTML_PATH = RAIZ / "index.html"

# Estructura del bloque en index.html:
#   var recursos = [\r\n{rec1},\r\n{rec2},...\r\n{recN}\r\n];
PATRON = re.compile(r"(var recursos\s*=\s*\[)(.*?)(\n\s*\];)", re.S)
SEPARADOR = ",\r\n"


def volcar(recursos):
    """Reproduce cada registro tal como vive hoy en el HTML."""
    registros = [
        json.dumps(r, ensure_ascii=False, separators=(", ", ": ")) for r in recursos
    ]
    return "\r\n" + SEPARADOR.join(registros) + "\r"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="no escribe; informa y sale con codigo 1 si hay diferencias",
    )
    args = ap.parse_args()

    for ruta in (JSON_PATH, HTML_PATH):
        if not ruta.exists():
            print(f"ERROR: no existe {ruta}", file=sys.stderr)
            return 2

    try:
        with open(JSON_PATH, encoding="utf-8") as fh:
            recursos = json.load(fh)
    except json.JSONDecodeError as exc:
        print(f"ERROR: el JSON no es valido: {exc}", file=sys.stderr)
        return 2

    if not isinstance(recursos, list):
        print("ERROR: el JSON debe ser una lista de recursos", file=sys.stderr)
        return 2

    # Comprobacion de integridad: identificadores unicos
    ids = [r.get("id") for r in recursos if isinstance(r, dict)]
    duplicados = {i for i in ids if ids.count(i) > 1}
    if duplicados:
        print(f"ERROR: hay identificadores duplicados: {sorted(duplicados)}", file=sys.stderr)
        return 2

    with open(HTML_PATH, encoding="utf-8", newline="") as fh:
        html = fh.read()

    m = PATRON.search(html)
    if not m:
        print("ERROR: no encontre el bloque 'var recursos = [' en index.html", file=sys.stderr)
        return 2

    actual = m.group(2)
    nuevo = volcar(recursos)

    if actual == nuevo:
        print(f"Sin cambios. {len(recursos)} recursos, HTML ya sincronizado.")
        return 0

    # Diagnostico: cuantos registros tiene cada lado
    n_actual = len(re.findall(r"^\s*\{\"id\":", actual, re.M))
    print(f"JSON: {len(recursos)} recursos | HTML: {n_actual} recursos")

    if args.check:
        print("DESINCRONIZADOS. Ejecuta sin --check para corregirlo.", file=sys.stderr)
        return 1

    resultado = html[: m.start(2)] + nuevo + html[m.end(2) :]
    with open(HTML_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(resultado)
    print(f"index.html sincronizado desde el JSON ({len(recursos)} recursos).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
