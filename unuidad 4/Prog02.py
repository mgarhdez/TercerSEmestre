

import json    # Esta libreria es para crear archivos json
import os      # Esta librearia es para crear archivos y carpetas 

archivo = "datos.json"
datos = {
    "Nombre": "Juan",
    "Edad": 50,
    "Domicilio":"Hidalgo #120"
    
}
if not os.path.exists(archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
        
datoslocales = {}

if  os.path.exists(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        datoslocales = json.load(f)
    if len(datoslocales)==0:
        print("El archivo esta vacio")
    else:
        for i, d in enumerate(datoslocales, start=1):
            print(f'{d,['Nombre']}{d,["Edad"]}{d,["Domicilio"]}')            