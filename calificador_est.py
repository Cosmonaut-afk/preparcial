from clave_X.clave_x import suma, multiplicacion, sumarLista, getGithubUrl

result = suma()
if result == 6:
    print("ejercicio01: pass")
else:
    print("ejercicio01: fail")

result1 = multiplicacion()
if result1 == 40:
    print("ejercicio02: pass")
else:
    print("ejercicio02: fail")

numerosLista = []
result2 = sumarLista()
if result2 == 38:
    print("ejercicio03: pass")
else:
    print("ejercicio03: fail")

result = getGithubUrl()
if not result == "":
    print("ejercicio04: pass")
else:
    print("ejercicio04: fail")
