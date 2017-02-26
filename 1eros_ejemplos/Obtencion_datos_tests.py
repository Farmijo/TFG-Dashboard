import json
f_out=open("processed_data/testsData/processed_test_marks_1attempt.json", "w")
f_out2=open("processed_data/testsData/processed_averages_1st_attempt.json", "w")
output = []
output2=[]
output3=[]
notas_medias= dict()


for i in range(187):
	f = open("splitted/outputbatch_{}.json".format(i), "r")
	
	
	myData = json.load(f)


	#Parsing para (no) existencia de atributo
	for line in myData:

		if  line["event_type"]== "problem_check" and line["event_source"]=="server":
				#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
				if line["event"]["attempts"]==1:
					instancia_curso=dict()
					instancia_curso["alumno"]=line["username"]
					instancia_curso["modulo"]=line["context"]["module"]["display_name"]
					instancia_curso["nota"]=line["event"]["grade"]
					instancia_curso["nota_ponderada"]=((line["event"]["grade"])  *10)  /  line["event"]["max_grade"]
					lista=line["time"]
					lista=lista.split('T')[0]
					instancia_curso["fecha"]=lista
				#print line
				output.append(instancia_curso)

json.dump(output,f_out)

for line in output:
	curso=line["modulo"]
	if curso not in notas_medias.keys():

		notas_medias[curso]=[]
		notas_medias[curso].append(line["nota_ponderada"])

	else:
		notas_medias[curso].append(line["nota_ponderada"])

for ref in notas_medias.keys():
	nota_media=dict()
	nota_media[ref]=sum(notas_medias[ref])/float(len(notas_medias[ref]))

	output2.append(nota_media)

i=0
for line in output2:
	final =dict()
	ref=output2[i].keys()[0]
	final["curso"]=ref
	final["nota_media"]=output2[i][ref]
	output3.append(final)
	i=i+1


json.dump(output3,f_out2)



