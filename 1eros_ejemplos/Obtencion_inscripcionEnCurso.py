import json
from utils import Agrupador
f_out=open("processed_data/processed_inscripcion2.json", "w")
output = []
for i in range(187):
	f = open("splitted/outputbatch_{}.json".format(i), "r")
	
	myData = json.load(f)

#algoritmo para poder obtener los datos de inscripcion en el curso.
	#Parsing para (no) existencia de atributo
	for line in myData:
		if  line["event_type"]== "edx.course.enrollment.activated":
				#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
				datos = dict()
				datos["event_type"]=line["event_type"]
				datos["username"]=line["username"]
				lista=line["time"]
				lista=lista.encode('ascii','ignore')
				lista=lista.split('T')[0]
				#lista=lista.replace('-','')
				datos["time"]=lista
				output.append(datos)
				#print datos["event_type"]

json.dump(output,f_out)

#ejecutar posteriormente
#Agrupador.agrupator("splitted_and_analized/analized_{}.json", "processed_data/processed_inscripcion2.json")