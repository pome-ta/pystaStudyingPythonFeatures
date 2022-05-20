from pathlib import Path


json_path = Path('./sample01.json')
json_str = json_path.read_text(encoding='utf-8')

for n, s in enumerate(json_str):
  print(f'{n:02}: {s}')
