import json
f_out=open("processed_data/testsData/analized.json", "w")
output = []
for i in range(187):
	f = open("splitted/outputbatch_{}.json".format(i), "r")

	
	myData = json.load(f)


	#Parsing para (no) existencia de atributo
	for line in myData:
		if  line["event_type"]== "problem_check":
				#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
				output.append(line)
				#print line

json.dump(output,f_out)