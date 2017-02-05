import json
from utils import Agrupador


for i in range(187):
	f = open("../splitted/outputbatch_{}.json".format(i), "r")
	f_out=open("../splitted_and_analized/analized_{}.json".format(i), "w")
	output = []
	myData = json.load(f)
#Algoritmo basico para busqueda. Sustituir el evento en cuestion por el que se quiera buscar. Los json generados mostraran si hay resultado o no.

	#Parsing para (no) existencia de atributo
	for line in myData:	
		if line["event_type"] == "edx.course.enrollment.deactivated":
			
				#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
				output.append(line)
				#print "OK"
				#print datos["event_type"]

	json.dump(output,f_out)

	if output!=[]:
		print "OK"



Agrupador.agrupator("../splitted_and_analized/analized_{}.json", "../Reagrupados.json")