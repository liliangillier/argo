import re, os

all_pages = sorted(f for f in os.listdir('.') if f.endswith('.html'))
all_names = set(f[:-5] for f in all_pages)

const_text = open('constellation.html', encoding='utf-8').read()
const_links = set(re.findall(r"'([a-z]+)\.html'", const_text))

idx_text = open('index.html', encoding='utf-8').read()
idx_links = set(re.findall(r'href="([a-z]+)\.html"', idx_text))

print("Total pages:", len(all_names))
print("Constellation entries:", len(const_links))
print("Missing from constellation:", sorted(all_names - const_links))
print("Extra in constellation (not a real page):", sorted(const_links - all_names))
print()
print("Index links:", len(idx_links))
expected_idx = all_names - {'index'}
print("Missing from index:", sorted(expected_idx - idx_links))
print("Extra in index (not a real page):", sorted(idx_links - all_names))
