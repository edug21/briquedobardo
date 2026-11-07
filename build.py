"""Gera index.html a partir de src/template.html + data/cds.json."""
import json
from pathlib import Path

root = Path(__file__).parent
data = json.loads((root / "data" / "cds.json").read_text(encoding="utf-8"))
tpl = (root / "src" / "template.html").read_text(encoding="utf-8")
(root / "index.html").write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False)), encoding="utf-8")
print(f"index.html gerado com {len(data)} itens")
