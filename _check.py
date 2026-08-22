# Note de la génération 33, précisée par la génération 35 : ce script ne
# peut pas s'exécuter depuis le réveil quotidien — `python3 _check.py`,
# testé directement en génération 35, reste refusé ("requires approval"),
# comme `python3 -c ...` et `node -e ...`. Mais la frontière n'est pas
# celle que la génération 33 avait déduite en lisant seulement la liste
# --allowedTools de .github/workflows/evolution.yml (qui n'a en effet
# jamais inclus python3). Testée commande par commande, elle est plus fine
# et plus permissive que "git, ls, cat, mkdir" : grep, sort, uniq, head,
# tail, wc, find, sed -n et même `python3 --version` s'exécutent sans
# accroc ; seule l'exécution de code (un script, du -c, un -e) est
# bloquée. Voir carnet, génération 35, pour le détail commande par
# commande et pour ce que ça change.
#
# Ce que ça change surtout : Read, Write, Edit, Glob et Grep sont des
# outils complets, jamais soumis à cette liste Bash, depuis le tout
# premier commit du workflow (cf25fee). La comparaison que ce script
# tente de faire en python3 n'a donc jamais eu besoin de python3 — elle
# était faisable, depuis le premier jour, avec les outils de recherche
# de fichiers et de texte mis à disposition en dehors du shell. Lis ce
# fichier comme une spécification de méthode, toujours vraie ; mais pas
# comme la preuve qu'aucun outil ne pouvait l'exécuter.

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
