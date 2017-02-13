import json
from utils import Agrupador
f_out=open("processed_data/processed_listaUsuarios.json", "w")
output = []
struct_users=[]
for i in range(187):
	f = open("splitted/outputbatch_{}.json".format(i), "r")
	
	myData = json.load(f)


#algoritmo para poder obtener los datos de inscripcion en el curso.
	#Parsing para (no) existencia de atributo
	for line in myData:
		if  line["username"] not in output:
				#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
				datos = dict()
				datos["username"]=line["username"]
				output.append(line["username"])
				struct_users.append(datos)
				#print output


json.dump(struct_users,f_out)

#ejecutar posteriormente
#Agrupador.agrupator("splitted_and_analized/analized_{}.json", "processed_data/processed_listaUsuarios.json")