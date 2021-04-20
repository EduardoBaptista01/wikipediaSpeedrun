# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import requests
# import webbrowser

start_time = time.time()

listaLinks = ['Gondomar,_Portugal']
paginaAlvo = "Jimmy_Carr"
dicLinks = {listaLinks[0]: 'end'}
print(f"\nStarting Page = {listaLinks[0]}")
print(f"Goal = {paginaAlvo}\n")

# Word matching
res = requests.get(f"https://en.wikipedia.org/wiki/{paginaAlvo}")
texto = res.text.partition("From Wikipedia, the free encyclopedia")[2].partition("#See_also")[0]
words = texto.split()
links_goal = []
elapsed_time = 0
for word in words:
    if 'href="/wiki/' in word and 'File:' not in word and word[12:-1]:
        links_goal.append(f"{word[12:-1]}")
# print(links_goal)
# print(len(links_goal))
lista_matches = []
top_match = 0
if paginaAlvo in links_goal:
    print('got it')

lista_tempo = []
for pagina in listaLinks:
    start_time_pag = time.time()
    if paginaAlvo in listaLinks:
        break
    res = requests.get(f"https://en.wikipedia.org/wiki/{pagina}")
    # Trimming the only important parts of the text
    texto = res.text.partition("From Wikipedia, the free encyclopedia")[2].partition("/wiki/Help:Category")[0]
    #print(texto)
    words = texto.split()
    links = []
    amount_of_links = len(listaLinks)
    for word in words:
        if 'href="/wiki/' in word and 'File:' not in word and word[12:-1] not in listaLinks and 'identifier' not in word and 'Wikipedia' not in word and 'Help:' not in word and 'Category:' not in word and 'Template:' not in word and 'Special:' not in word and 'Portal:' not in word:
            links.append(f"{word[12:-1]}")
            listaLinks.append(f"{word[12:-1]}")
            dicLinks[f"{word[12:-1]}"] = pagina
    if paginaAlvo in links:
        break
    ocurrences = list(set(links_goal) & set(links))
    # for occ in ocurrences:
    #     if occ in lista_matches or occ in listaLinks:
    #         ocurrences.remove(occ)
    #         continue
    #     lista_matches.append(occ)
    ocurrences_len = len(ocurrences)
    if ocurrences_len > top_match:
        for index_occ, occ in enumerate(ocurrences):
            listaLinks.insert(listaLinks.index(pagina)+1+index_occ, occ)
    seconds = time.time() - start_time_pag
    seconds = float("{:.3f}".format(seconds))
    lista_tempo.append(seconds)
    avrg = sum(lista_tempo) / len(lista_tempo)
    avrg = float("{:.3f}".format(avrg))
    space = "-" * (40-len(pagina)) + ">"
    space2 = "-" * (45-len(space))
    elapsed_time = float("{:.3f}".format(time.time() - start_time))
    print(f"{pagina}{space} in {seconds} sec / Average:{avrg} sec / added {len(listaLinks) - amount_of_links} pages / elapsed time:{elapsed_time} sec / matches:{ocurrences_len}")
    print(f"{ocurrences}")

print(f"Found {paginaAlvo}!")
print(f"Scanned {len(listaLinks)} pages")

caminho = f"{paginaAlvo}"
alvo = paginaAlvo

while list(dicLinks.keys())[0] not in caminho:
    # print(alvo)
    alvo = dicLinks.get(alvo)
    caminho = f"{alvo} -> {caminho}"

print(caminho)
print("\n\n--- Completed in %s seconds ---" % elapsed_time)
