import json

f=open("processed_data/processed_inscripcion.json","r")
f_out=open("processed_data/processed_frecuencias_inscripcion.json", "w")

output=[]
datos=json.load(f)
frecuencia = dict()
for line in datos:
	referencia=line['time']
	referencia=referencia.encode('ascii','ignore')
	if referencia not in frecuencia.keys():
		frecuencia[referencia]=1
	else:
		frecuencia[referencia]=frecuencia[referencia]+1

output.append(frecuencia)
json.dump(output,f_out)


