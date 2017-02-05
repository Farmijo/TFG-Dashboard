import json
from utils import Agrupador
'''
for i in range(187):
	f = open("splitted/outputbatch_{}.json".format(i), "r")
	f_out=open("splitted_and_analized/analized_{}.json".format(i), "w")
	output = []
	myData = json.load(f)

#algoritmo para poder obtener los datos de inscripcion en el curso.
	#Parsing para (no) existencia de atributo
	for line in myData:
		if  line["event_type"]== "edx.course.enrollment.deactivated":
				#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
				datos = dict()
				datos["event_type"]=line["event_type"]
				datos["username"]=line["username"]
				lista=line["time"]
				datos["time"]=lista.split('T')[0]

				output.append(datos)
				#print datos["event_type"]

	json.dump(output,f_out)
'''
#ejecutar posteriormente
Agrupador.agrupator("splitted_and_analized/analized_{}.json", "processed_data/processed_inscripcionAnulada.json")