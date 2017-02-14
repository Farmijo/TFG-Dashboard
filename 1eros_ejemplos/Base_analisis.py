import json

for i in range(187):
	f = open("splitted/outputbatch_{}.json".format(i), "r")
	f_out=open("processed_data/testsData/analized_{}.json".format(i), "w")
	output = []
	myData = json.load(f)


	#Parsing para (no) existencia de atributo
	for line in myData:
		if  line["event_type"]== "problem_check":
				#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
				output.append(line)

	json.dump(output,f_out)

'''

#Parsing para valores concretos de un atributo 
for line in myData:
	if line["event"] == "":
			#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
			output.append(line)

json.dump(output,f_out)
				




#Parsing en caso de que exista un objeto (context en este caso)

for line in myData:
	if "username" in line :

			print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
			output.append(line)

json.dump(output,f_out)



#Parsing para existencia de atributos dentro de objetos
for line in myData:
	try: 
		if line["context"]["path"]:
		#	print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
			output.append(line)


			#print "json con valor"
	except KeyError:
		print "1"

json.dump(output,f_out)
		

#parsing para existencia de objetos en objetos 
for line in myData:
 
		if  "context" "course_user_tags" in line:
			print "caca"
		else:
		#	print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
			output.append(line)
			print "Ok"
			#print "json con valor"

json.dump(output,f_out)

#parsing para existencia de objetos en objetos 
for line in myData:
 
		if  "event" \"id\" in line:
			print "caca"
		else:
		#	print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
			output.append(line)
			print "Ok"
			#print "json con valor"

json.dump(output,f_out)

'''
