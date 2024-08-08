import os
import csv
import eml_to_html
from utils import poner_tildes, tipo_pago

path = os.getcwd()
carpeta = input("Escribe el nombre de la carpeta: ")
abs_route = path + f"/{carpeta}/"
route_mails = os.listdir(abs_route)

lista = []

for item in route_mails:
    with open(abs_route + item, "r", encoding="utf8") as f:
        if item.endswith(".eml"):
            lines = f.read()
            rut = ""
            tipo = ""
            pago = ""
            nombre = ""
            observaciones = ""
            monto = ""
            claves = []
            if lines.find("Nombre:") != -1:
                nombre_start = lines.find("Nombre:") + len("Nombre:") + 109
                nombre_end = lines.find('<', nombre_start)
                nombre = lines[nombre_start:nombre_end]
                nombre = poner_tildes(nombre)
            if lines.find("Correo:") != -1:
                correo_start = lines.find("Correo:") + len("Correo:") + 109
                correo_end = lines.find('<', correo_start)
                correo = lines[correo_start:correo_end]
            if lines.find("Rut o pasaporte:"):
                rut_start = lines.find("Rut o pasaporte:") + len("Rut o pasaporte:") + 109
                rut_end = lines.find('<', rut_start)
                rut = lines[rut_start:rut_end]
                if "k" in rut:
                    rut = rut.replace("k", "K")
                if "." in rut:
                    rut = rut.replace(".", "")
                if "-" not in rut:
                    rut = rut[:len(rut)-1] + "-" + rut[len(rut)-1:]
            if lines.find("Forma de pago:"):
                pago_start = lines.find("Forma de pago:") + len("Forma de pago:") + 108
                pago_end = lines.find("<", pago_start)
                pago = lines[pago_start:pago_end]
            if lines.find("Monto:"):
                monto_start = lines.find("Monto:") + len("Monto:") + 109
                monto_end = lines.find("<", monto_start)
                monto = lines[monto_start:monto_end]
            if lines.find("Observaciones:"):
                observaciones_start = lines.find("Observaciones:") + len("Observaciones:") + 109
                observaciones_end = lines.find("<", observaciones_start)
                observaciones = lines[observaciones_start:observaciones_end]
                observaciones = poner_tildes(observaciones)
            nombre = nombre.title()
            claves = [nombre, correo, rut, tipo_pago(pago), monto, observaciones]

            lista.append(claves)
            new_name = rut + " " + nombre + ".eml"
        
    # Cambiar el nombre del archivo

    if not os.path.exists(carpeta + "/" + new_name):
        os.rename(abs_route + item, abs_route + new_name)
        eml_to_html.eml_to_html(abs_route + new_name)

with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lista)