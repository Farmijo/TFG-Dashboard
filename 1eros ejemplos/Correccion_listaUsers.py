import json
from utils import Agrupador
f=open("processed_data/processed_listaUsuarios.json", "r")
f_out=open("processed_data/processed_listaUsuariosCorregida.json", "w")
struct_users=[]


myData = json.load(f)

for i in range(1,708,4):


				#print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
	datos = dict()
	datos["username_{}".format(1)]=myData[i+3]["username"]
	datos["username_{}".format(2)]=myData[i+2]["username"]
	datos["username_{}".format(3)]=myData[i+1]["username"]
	datos["username_{}".format(4)]=myData[i]["username"]

	struct_users.append(datos)
				


json.dump(struct_users,f_out)

