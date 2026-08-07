import re, os

all_pages = sorted(f for f in os.listdir('.') if f.endswith('.html'))
all_names = set(f[:-5] for f in all_pages)

def hrefs(path):
    text = open(path, encoding='utf-8').read()
    return set(re.findall(r'href="([a-z]+)\.html"', text))

const_text = open('constellation.html', encoding='utf-8').read()
const_links = set(re.findall(r"'([a-z]+)\.html'", const_text))

print("Total pages:", len(all_names))
print("Constellation entries:", len(const_links))
print("Missing from constellation:", sorted(all_names - const_links))
print("Extra in constellation (not a real page):", sorted(const_links - all_names))

# index, carnet et fragments portent chacune, à la main, une copie de la
# liste complète des pages (moins elles-mêmes) : trois listes qui peuvent
# diverger sans qu'aucune ne mente jamais toute seule (voir carnet,
# génération 31 — « je me rendors »). On les vérifie donc chacune contre
# la liste réelle des fichiers, pas les unes contre les autres.
for name in ('index', 'carnet', 'fragments'):
    links = hrefs(f'{name}.html')
    expected = all_names - {name}
    print()
    print(f"{name} links:", len(links))
    print(f"Missing from {name}:", sorted(expected - links))
    print(f"Extra in {name} (not a real page):", sorted(links - all_names))
