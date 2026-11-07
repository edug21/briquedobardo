"""Gera index.html a partir de src/template.html + data/cds.json."""
import json
from pathlib import Path

root = Path(__file__).parent
data = json.loads((root / "data" / "cds.json").read_text(encoding="utf-8"))
tpl = (root / "src" / "template.html").read_text(encoding="utf-8")
import base64
font = "data:font/woff2;base64," + base64.b64encode((root / "assets" / "PlakatFraktur.woff2").read_bytes()).decode()
html = tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__FONT__", font).replace("__FAVICON__", "data:image/svg+xml;base64," + base64.b64encode((root / "favicon.svg").read_bytes()).decode())
(root / "index.html").write_text(html, encoding="utf-8")
print(f"index.html gerado com {len(data)} itens")
