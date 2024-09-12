import os
import csv
import eml_to_html
from utils import poner_tildes, tipo_pago

path = os.getcwd()
carpeta = input("Escribe el nombre de la carpeta: ")
abs_route = path + f"/{carpeta}/"
route_mails = os.listdir(abs_route)

lista = []
lista_cai = []

for item in route_mails:
    with open(abs_route + item, "r", encoding="utf8") as f:
        if item.endswith(".eml"):
            lines = f.read()
            rut = ""
            tipo = ""
            pago = ""
            nombre = ""
            apellidos = ""
            observaciones = ""
            monto = ""
            año = ""
            claves = []
            
            tipo_de_pago = ""
            
            if lines.find("Tipo de pago:"):
                tipo_de_pago_start = lines.find('top;">', lines.find("Tipo de pago:")) + len('top;">')
                tipo_de_pago_end = lines.find('<', tipo_de_pago_start)
                tipo_de_pago = lines[tipo_de_pago_start:tipo_de_pago_end]
                tipo_de_pago = tipo_de_pago.replace('\n', '')
                tipo_de_pago = poner_tildes(tipo_de_pago)
                tipo_de_pago = tipo_de_pago.replace('=', '')
            
            if tipo_de_pago == "Encuentro Directivas Cai -120 años":
                if lines.find("Nombres:") != -1:
                    #nombre_start = lines.find("Nombre:") + len("Nombre:")
                    nombre_start = lines.find('top;">', lines.find("Nombres:")) + len('top;">')
                    nombre_end = lines.find('<', nombre_start)
                    nombre = lines[nombre_start:nombre_end]
                    nombre = nombre.replace('\n', '')
                    nombre = poner_tildes(nombre)
                    nombre = nombre.replace('=', '')
                    apellidos_start = lines.find('top;">', lines.find("Apellidos:")) + len('top;">')
                    apellidos_end = lines.find('<', apellidos_start)
                    apellidos = lines[apellidos_start:apellidos_end]
                    apellidos = apellidos.replace('\n', '')
                    apellidos = poner_tildes(apellidos)
                    apellidos = apellidos.replace('=', '')
                if lines.find("Correo:") != -1:
                    #correo_start = lines.find("Correo:") + len("Correo:") + 109
                    correo_start = lines.find('top;">', lines.find("Correo:")) + len('top;">')
                    correo_end = lines.find('<', correo_start)
                    correo = lines[correo_start:correo_end]
                    correo = correo.replace('\n', "")
                    correo = correo.replace('=', "")
                if lines.find("Rut:") != -1:
                    #rut_start = lines.find("Rut o pasaporte:") + len("Rut o pasaporte:") + 109
                    rut_start = lines.find('top;">', lines.find("Rut:")) + len('top;">')
                    rut_end = lines.find('<', rut_start)
                    rut = lines[rut_start:rut_end]
                    if "k" in rut:
                        rut = rut.replace("k", "K")
                    if "." in rut:
                        rut = rut.replace(".", "")
                    if "-" not in rut:
                        rut = rut[:len(rut)-1] + "-" + rut[len(rut)-1:]
                    rut = rut.replace('\n', '')
                if lines.find("Forma de pago:") != -1:
                    #pago_start = lines.find("Forma de pago:") + len("Forma de pago:") + 108
                    pago_start = lines.find('top;">', lines.find("Forma de pago:")) + len('top;">')
                    pago_end = lines.find("<", pago_start)
                    pago = lines[pago_start:pago_end]
                    pago = pago.replace('\n', '')
                if lines.find("Monto:") != -1:
                    #monto_start = lines.find("Monto:") + len("Monto:") + 109
                    monto_start = lines.find('top;">', lines.find("Monto:")) + len('top;">')
                    monto_end = lines.find("<", monto_start)
                    monto = lines[monto_start:monto_end]
                    monto = monto.replace("\n", "")
                if lines.find("Comentarios:") != -1:
                    #observaciones_start = lines.find("Observaciones:") + len("Observaciones:") + 109
                    observaciones_start = lines.find('top;">', lines.find("Comentarios:")) + len('top;">')
                    observaciones_end = lines.find("<", observaciones_start)
                    observaciones = lines[observaciones_start:observaciones_end]
                    observaciones = poner_tildes(observaciones)
                    observaciones = observaciones.replace('\n', '')
                if lines.find("A=C3=B1oCai:") != -1:
                    #observaciones_start = lines.find("Observaciones:") + len("Observaciones:") + 109
                    año_start = lines.find('top;">', lines.find("A=C3=B1oCai:")) + len('top;">')
                    año_end = lines.find("<", año_start)
                    año = lines[año_start:año_end]
                    año = poner_tildes(año)
                    año = año.replace('\n', '')
                nombre = nombre.title()
                apellidos = apellidos.title()
                claves = [f"{nombre} {apellidos}", correo, rut, "", monto, año, observaciones, tipo_pago(pago)]

                lista_cai.append(claves)
                new_name = rut + " " + nombre + " " + apellidos + ".eml"

            elif tipo_de_pago == "PUC Escuela de Ingeniería":    
                if lines.find("Nombre:") != -1:
                    #nombre_start = lines.find("Nombre:") + len("Nombre:")
                    nombre_start = lines.find('top;">', lines.find("Nombre:")) + len('top;">')
                    nombre_end = lines.find('<', nombre_start)
                    nombre = lines[nombre_start:nombre_end]
                    nombre = nombre.replace('\n', '')
                    nombre = poner_tildes(nombre)
                    nombre = nombre.replace('=', '')
                if lines.find("Correo:") != -1:
                    #correo_start = lines.find("Correo:") + len("Correo:") + 109
                    correo_start = lines.find('top;">', lines.find("Correo:")) + len('top;">')
                    correo_end = lines.find('<', correo_start)
                    correo = lines[correo_start:correo_end]
                    correo = correo.replace('\n', "")
                    correo = correo.replace('=', "")
                if lines.find("Rut o pasaporte:"):
                    #rut_start = lines.find("Rut o pasaporte:") + len("Rut o pasaporte:") + 109
                    rut_start = lines.find('top;">', lines.find("Rut o pasaporte:")) + len('top;">')
                    rut_end = lines.find('<', rut_start)
                    rut = lines[rut_start:rut_end]
                    if "k" in rut:
                        rut = rut.replace("k", "K")
                    if "." in rut:
                        rut = rut.replace(".", "")
                    if "-" not in rut:
                        rut = rut[:len(rut)-1] + "-" + rut[len(rut)-1:]
                    rut = rut.replace('\n', '')
                if lines.find("Forma de pago:"):
                    #pago_start = lines.find("Forma de pago:") + len("Forma de pago:") + 108
                    pago_start = lines.find('top;">', lines.find("Forma de pago:")) + len('top;">')
                    pago_end = lines.find("<", pago_start)
                    pago = lines[pago_start:pago_end]
                    pago = pago.replace('\n', '')
                if lines.find("Monto:"):
                    #monto_start = lines.find("Monto:") + len("Monto:") + 109
                    monto_start = lines.find('top;">', lines.find("Monto:")) + len('top;">')
                    monto_end = lines.find("<", monto_start)
                    monto = lines[monto_start:monto_end]
                    monto = monto.replace("\n", "")
                if lines.find("Observaciones:"):
                    #observaciones_start = lines.find("Observaciones:") + len("Observaciones:") + 109
                    observaciones_start = lines.find('top;">', lines.find("Observaciones:")) + len('top;">')
                    observaciones_end = lines.find("<", observaciones_start)
                    observaciones = lines[observaciones_start:observaciones_end]
                    observaciones = poner_tildes(observaciones)
                    observaciones = observaciones.replace('\n', '')
                nombre = nombre.title()
                claves = [nombre, correo, rut, tipo_pago(pago), monto, observaciones]

                lista.append(claves)
                new_name = rut + " " + nombre + ".eml"
    # Cambiar el nombre del archivo
    if not os.path.exists(carpeta + "/" + new_name):
        os.rename(abs_route + item, abs_route + new_name)
        eml_to_html.eml_to_html(abs_route + new_name)
    elif os.path.exists(carpeta + "/" + new_name) and (not os.path.exists(carpeta + "/" + new_name[:-4] + ".html")):
        eml_to_html.eml_to_html(abs_route + new_name)
    elif os.path.exists(carpeta + "/" + new_name) and (not os.path.exists(carpeta + "/" + new_name)):
        print("hola")

with open('out_b2s.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lista)

with open('out_cai.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lista_cai)