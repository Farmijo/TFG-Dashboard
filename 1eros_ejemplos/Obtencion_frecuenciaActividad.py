import json
from utils import Agrupador
f_out=open("processed_data/processed_numAcciones.json", "w")
output=[]
datos=json.load(f)
frecuencia = dict()
for i in range(187):
	f = open("splitted/outputbatch_{}.json".format(i), "r")
	

for line in datos:
	referencia=line['time']
	referencia=referencia.encode('ascii','ignore')
	if referencia not in frecuencia.keys():
		frecuencia[referencia]=1
	else:
		frecuencia[referencia]=frecuencia[referencia]+1

output.append(frecuencia)
json.dump(output,f_out)



