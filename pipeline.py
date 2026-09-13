from pathlib import Path
import json
from src.consistency import check_readme
ROOT=Path(__file__).parent
if __name__=='__main__':
    ok,req=check_readme(ROOT)
    print('Automotive Industrialization Control Tower - reproducibility smoke pipeline')
    print('Core results:', json.loads((ROOT/'outputs/core_results.json').read_text()))
    print('README consistency:',ok)
    if not ok: raise SystemExit(2)
