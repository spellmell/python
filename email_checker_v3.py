# email checker
# https://pastebin.com/GFQb5n6C

def email_checker(string):
    email = False
    etc = string  # email to check
    el = len(etc)
    minuserlen = 6
    etc_valido = False
    proveedor_valido = False
    dominio_valido = False
    arroba = False
    arrobacount = 0
    dot = False
    dotscount = 0

    # proveedores y dominios admitidos
    proveedores = ["gmail", "yahoo", "outlook", "protonmail", "autistici"]
    dominios = [".com", ".org", ".gub", ".com.uy", ".com.ar"]

    print("\nValidando...")
    # validación inicial de @, puntos y caracteres.
    cv = "0123456789abcdefghijklmnñopqrstuvwxyz@."  # caracteres válidos
    for x in etc:
        if x == "@":
            arroba = True
            arrobacount = arrobacount+1
        if x == ".":
            dot = True
            dotscount = dotscount+1
        if x not in cv:
            msg = x + " no es un carácter válido.\nÚnicamente se adminten \
caracteres de la a-z, números del 0-9, la @, y el ."
            etc_valido = False
            break
    else:
        if arroba and dot:
            etc_valido = True
            apos = etc.index("@")
            dotpos = etc.index(".")
            usuario = etc[:apos]
            # validación de 1, 2, y 3 puntos
            if dotpos > apos and dotscount <= 2:
                proveedor = etc[apos+1:dotpos]
                dominio = etc[dotpos:]
            elif dotpos < apos and dotscount > 1 and dotscount <= 3:
                proveedor = etc[apos+1:etc.index(".", apos, len(etc))]
                dominio = etc[apos+len(proveedor)+1:]
            elif dotscount > 3:
                proveedor = ""
                dominio = ""

        if not arroba:
            msg = "El texto ingresado no contiene una @. No es un email."
            etc_valido = False
        elif arrobacount > 1:
            msg = "El texto ingresado contiene más de una @."
            etc_valido = False
        elif not dot:
            msg = "El texto ingresado no contiene un punto. No es un email."
            etc_valido = False
        elif dotscount > 3:
            msg = "El email no puede tener más de 3 puntos."
            etc_valido = False
        elif len(usuario) == 0:
            msg = "El correo ingresado no tiene nombre de usuario."
            etc_valido = False
        elif len(usuario) < minuserlen:
            msg = "El nombre de usuario no puede tener menos de " + \
                str(minuserlen) + " caracteres."
            etc_valido = False
        elif len(usuario.split(".")) > 2:
            msg = "El nombre de usuario no puede tener más de un punto"
            etc_valido = False
        elif len(dominio.split(".")) > 3 and dotpos > apos:
            msg = "El dominio no puede tener más de 2 puntos"
            etc_valido = False

    # chequeo de proveedor
    if etc_valido:
        if proveedor not in proveedores:
            proveedor_valido = False
            msg = "El proveedor " + proveedor + " no es válido."
        else:
            proveedor_valido = True

    # chequeo de dominio
    if proveedor_valido:
        if dominio not in dominios:
            dominio_valido = False
            msg = "El dominio " + dominio + " no es válido."
        else:
            dominio_valido = True

    # salida final
    if(arroba and etc_valido and proveedor_valido and dominio_valido):
        email = True
        if email:
            return (f"\nDatos ingresados: \nEmail: {etc}\nLongitud del email: \
{el} caracteres\nPosición de la @: {apos} carácter\nUsuario: \
{usuario} \nProveedor: {proveedor}\nDominio: {dominio}\n\nEl email \
{etc} es válido.\n")
    else:
        return (f"\nEl email no es válido.\n{msg}")


print(email_checker(input("Ingresa tu email: ").lower()))
