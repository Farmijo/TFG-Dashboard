import json


def agrupator(input, output):
	f_out=open(output, "w")
	output = []

	#junta los distintos JSONS analizados en un unico

	for i in range(187):
		f = open(input.format(i), "r")
		myData = json.load(f)
		
		for line in myData:
			output.append(line)


	json.dump(output,f_out)

					