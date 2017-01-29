import json


f = open("test_reduced.json", "r")
f_out=open("analized.json", "w")
output = []
myData = json.load(f)

'''
#Parsing para valores concretos de un atributo 
for line in myData:
	if line["context"]["org_id"]!="":
			#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
			json.dump(line,f_out)
				




#Parsing en caso de que exista un objeto (context en este caso)

for line in myData:
	if "username" in line :

			print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
			json.dump(line,f_out)



#Parsing para existencia de atributos dentro de objetos
for line in myData:
	try: 
		if line["context"]["path"]:
		#	print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
			json.dump(line,f_out)
			#print "json con valor"
	except KeyError:
		print "1"

		'''

#parsing para existencia de objetos en objetos 
for line in myData:
 
		if  "context" "course_user_tag" in line:
			print "caca"
		else:
		#	print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
			output.append(line)
			#print "json con valor"

json.dump(output,f_out)