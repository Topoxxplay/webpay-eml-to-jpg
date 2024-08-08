import os
from html2image import Html2Image


path = os.getcwd()
# Loop input 
existe_carpeta = True
carpeta = input("Escribe el nombre de la carpeta donde están los HTML: ")
while existe_carpeta:
    if not os.path.isdir(path + f"/{carpeta}"):
        carpeta = input("Esa carpeta no existe: ")
        existe_carpeta = True
    else:
        existe_carpeta = False

destino = input("Escribe el nombre de la carpeta donde quieres guardar las imágenes: ")
html_path = path + f"/{carpeta}/"
route_mails = os.listdir(html_path)

destiny_path = path + f"/{destino}"

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