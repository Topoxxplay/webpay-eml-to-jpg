#Para definir funciones poner_tildes(), quitar signos() y tipo_de_pago()

def poner_tildes(nombre):
    if "=C3=-A1" in nombre:
        nombre = nombre.replace("=C3=-A1", "á")
    if "=C3=A1" in nombre:
        nombre = nombre.replace("=C3=A1", "á")
    if "=C3=A9" in nombre:
        nombre = nombre.replace("=C3=A9", "é")
    if "=C3=-A9" in nombre:
        nombre = nombre.replace("=C3=-A9", "é")
    if "=C3=AD" in nombre:
        nombre = nombre.replace("=C3=AD", "í")
    if "=C3=-AD" in nombre:
        nombre = nombre.replace("=C3=-AD", "í")
    if "=C3=B3" in nombre:
        nombre = nombre.replace("=C3=B3", "ó")
    if "=C3=-B3" in nombre:
        nombre = nombre.replace("=C3=-B3", "ó")
    if "=C3=BA" in nombre:
        nombre = nombre.replace("=C3=BA", "ú")
    if "=C3=-B1" in nombre:
        nombre = nombre.replace("==C3=B1", "ñ")
    if "=C3=B1" in nombre:
        nombre = nombre.replace("=C3=B1", "ñ")
    if "=C3=-B1" in nombre:
        nombre = nombre.replace("=C3=-B1", "ñ")
    return nombre

def quitar_signos(nombre):
    if "=" in nombre:
        nombre = nombre.replace("=\n", "")
    return nombre

def tipo_pago(v):
    if v == "VN" or v == "NC" or v == "VC" or v == "SI" or v == "S2":
        return "Crédito"
    elif v == "VD" or v == "VP":
        return "Débito"
    else:
        return "error"