import os
from html2image import Html2Image
import csv
import eml_to_html
from utils import poner_tildes, tipo_pago

def crear_csv(directorio_eml, directorio_csv):
    abs_route = f"{directorio_eml}/"
    route_mails = os.listdir(abs_route)
    
    lista = []

    for item in route_mails:
        with open(abs_route + item, "r", encoding="utf8") as f:
            if item.endswith(".eml"):
                lines = f.read()
                rut = ""
                pago = ""
                nombre = ""
                observaciones = ""
                monto = ""
                claves = []
                if lines.find("Nombre:") != -1:
                    #nombre_start = lines.find("Nombre:") + len("Nombre:")
                    nombre_start = lines.find('top;">', lines.find("Nombre:")) + len('top;">')
                    nombre_end = lines.find('<', nombre_start)
                    nombre = lines[nombre_start:nombre_end]
                    nombre = nombre.replace('\n', '')
                    nombre = poner_tildes(nombre)
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
        if not os.path.exists(abs_route + new_name):
            os.rename(abs_route + item, abs_route + new_name)
            eml_to_html.eml_to_html(abs_route + new_name)
        elif os.path.exists(abs_route + new_name) and (not os.path.exists(abs_route + new_name[:-4] + ".html")):
            eml_to_html.eml_to_html(abs_route + new_name)

    with open(f'{directorio_csv}out.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lista)

def crear_img(directorio_eml, directorio_img):
    html_path = f"{directorio_eml}/"
    route_mails = os.listdir(html_path)

    destiny_path = f"{directorio_img}"

    hti = Html2Image(browser="edge", output_path=destiny_path)

    images_list = os.listdir(destiny_path)

    # Por cada html en la carpeta, se creará una imagen si es que esta no se 
    # encuentra en la carpeta de destino

    for item in route_mails:
        if (".html" in item) and (".eml" not in item):
            position = item.find(".html")
            name = item[:position]
            image_name = name + ".jpg"
            if not image_name in images_list:
                hti.screenshot(
                    html_file=html_path+item,
                    save_as=name+".jpg"
                )