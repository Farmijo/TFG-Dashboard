import json

f=open("processed_data/processed_inscripcionAnulada.json","r")
f_out=open("processed_data/processed_frecuencias_anulacion.json", "w")

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


i=0
for line in frecuencia:
	final=dict()
	ref=frecuencia.keys()[i]
	final['fecha']=ref
	final['frecuencia']=frecuencia[ref]
	output.append(final)
	i=i+1




json.dump(output,f_out)


