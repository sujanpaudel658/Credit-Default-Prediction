import json

with open('23050272_IMPROVED_FINAL.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Remove output and execution counts to clean up, keep all code
for cell in nb['cells']:
    if 'outputs' in cell:
        cell['outputs'] = []
    if 'execution_count' in cell:
        cell['execution_count'] = None

with open('23050272_IMPROVED_FINAL.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print(f"✓ Cleaned up notebook - removed outputs/execution counts")
