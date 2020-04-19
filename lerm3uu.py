# -*- coding: utf-8 -*-
#qpy:2
#qpy:console
import json
import re
import requests, sys

url = sys.argv[1]
ab = open("m3u_mod.txt","a")
ab2 = open(url,"r",encoding="utf8")
ab3 = open("todos.txt", "a")
urlsm3u = []
imgm3u = []
nome = []
listagrupo = []
idm3u = []
def criarjson(li2, tudo2):
        np = 0
        go = ""
        tvg1 = ['tvg-name=""','tvg-logo=""','group-title=""']
        if "#EXTINF:-1" in li2:
            li2 = li2.replace('#EXTINF:-1', '').replace('tvg-id="','(*)').replace('" tvg-name="', '(*)').replace('" tvg-logo="','(*)').replace('" group-title="','(*)').replace('"','').split("(*)")
            li2.remove(li2[0])
            print(len(li2))
            #print(li2)
            imgm3u.append(li2[1])
            tudo2['id'] = li2[0]
            tudo2['imagem'] = li2[2]
            nx = 0
            no = li2[1]
            if "- Episode" in li2[1]:
               no = li2[1]
               no = no.replace("- Episode","- Episodio")
               print(no)
            tudo2['nome'] = no
            if "-" in li2[1]:
               #print('ok')
               go = li2[1].split("-")[1]
            tudo2['grupo'] = li2[3]+go
            nome.append(li2[0])
            if li2[2] not in listagrupo:
                listagrupo.append(li2[2])
                    #print li2
        elif "http://" in li2:
            urlsm3u.append(li2.replace("\r\n","").split(" ")[0])
            tudo2['url'] = li2.replace('\n', '')
        return tudo2
        #fin = json.dumps(tudo, indent=4, separators=(',', ': '), ensure_ascii=False)
tudo = {}
tudo2 = {}
tudo3 = {}
cont = 0
cont2 = 1
boinax = ""
tudo['series_tudo'] = []
tudo['filmes_tudo'] = []
tudo['tv_tudo'] = []
for li in ab2.readlines():
    boi = criarjson(li,tudo2)
    print(boi)
    if len(tudo2) == 5:
        b = str(boi['grupo'].replace(' ', '_').replace('\t','').replace('\n','')).split(",")[0]
        boina = re.sub('\b+', '', b)
        #print (boina2)
        #print(boina)
        try:
           tudo[boina].append(boi)
        except KeyError:
           tudo[boina] = []
           tudo[boina].append(boi)
        if "/series/" in boi['url'] and not boina in tudo['series_tudo']:
           tudo['series_tudo'].append(boina)
        if "/live/" in boi['url'] and not boina in tudo['tv_tudo']:
           tudo['tv_tudo'].append(boina)
        if "/movie/" in boi['url'] and not boina in tudo['filmes_tudo']:
           tudo['filmes_tudo'].append(boina)
        tudo2 = {}
    cont+=1
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(tudo, f, ensure_ascii=False, indent=4)
           #fin = json.dumps(tudo, indent=4, separators=(',', ': '), ensure_ascii=False)
           #outfile.write(fin)
    #if "#EXTINF:-1" in li2[0]:
    #print li2[1]
#ab.writelines(urlsm3u)
ab.close()
#print(tudo)
#print imgm3u
n1 = 0
'''for n in urlsm3u:
    for o in imgm3u:
        for p in nome:
            for q in listagrupo:
                tudo = {'url': n, 'imagem': o,'nome': p,'listagrupo': q}
                with open('m3u_mod.txt', 'w') as outfile:
                   json.dump(tudo, outfile)'''
#ab.writelines(li.replace('#EXTINF:-1 tvg-id="" ',""))
    