import xmltodict
import json, requests
import datetime
now = datetime.datetime.now()

openx = open("boinaxml.json", "w", encoding="utf8")
mes = str(now.month)
dia = str(now.day)

if len(mes) == 1:
   mes = "0"+mes
if len(dia) == 1:
   dia = "0"+dia

mescomp = str(now.year)+mes+dia
hora = now.hour
minuto = now.minute

r = requests.get('http://tv.factoryiptv.com:80/xmltv.php?username=zizelia&password=zizelia')

my_dict=xmltodict.parse(r.content)
json_data=json.dumps(my_dict, indent=4, ensure_ascii=False).encode('utf8')
pegartempo = ([data1["@start"] for data1 in json.loads(json_data.decode())["tv"]["programme"]])
pegarparar = ([data1["@stop"] for data1 in json.loads(json_data.decode())["tv"]["programme"]])
pegarcanal = ([data1["@channel"] for data1 in json.loads(json_data.decode())["tv"]["programme"]])
titulo = ([data1["title"] for data1 in json.loads(json_data.decode())["tv"]["programme"]])


tudo = {}
valores = {}
v = 0
for h in pegartempo:
   if mescomp in h:
      horax1 = int(h[8]+h[9])
      horax2 = int(h[10]+h[11])
      i = pegarparar[v]
      horay1 = int(i[8]+i[9])
      horay2 = int(i[10]+i[11])
      if horax1 <= hora and horay1 >= hora:
         if not horax1 == hora and horax2 > minuto or not horay1 == hora and horay2 < minuto:
            #print(str(horax1)+":"+str(horax2)+" "+str(horay1)+":"+str(horay2)+" "+pegarcanal[v]+" "+titulo[v])
            valores['nome'] = pegarcanal[v]
            valores['progra'] = titulo[v]
            if len(str(horax1)) == 1:
               horax1 = "0"+str(horax1)
            if len(str(horax2)) == 1:
               horax2 = "0"+str(horax2)
            if len(str(horay1)) == 1:
               horay1 = "0"+str(horay1)
            if len(str(horay2)) == 1:
               horay2 = "0"+str(horay2)
            valores['horas'] = str(horax1)+":"+str(horax2)+" "+str(horay1)+":"+str(horay2)
            print(valores)
            try:
              tudo[pegarcanal[v]].append(valores)
            except KeyError:
              tudo[pegarcanal[v]] = []
              tudo[pegarcanal[v]].append(valores)
            valores = {}
   v+=1
with open('xmltv.json', 'w', encoding='utf-8') as f:
    json.dump(tudo, f, ensure_ascii=False, indent=4)


print(hora, minuto)
'''with open('boinaxml.json', encoding="utf8") as f:
  data = json.load(f)
print([data1["@start"] for data1 in data["tv"]["programme"]])'''

'''for j in json_data.decode():
   openx.writelines(j)'''
