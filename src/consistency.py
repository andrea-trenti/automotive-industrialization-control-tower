import json,re
from pathlib import Path
def load_core(root): return json.loads((Path(root)/'outputs/core_results.json').read_text())
def check_readme(root):
    root=Path(root); c=load_core(root); t=(root/'README.md').read_text()
    required=[str(c['deterministic_sop']),str(c['baseline']['p80']),str(c['target_plus']['p80']),'95.4%','70.9%']
    return all(x in t for x in required),required
