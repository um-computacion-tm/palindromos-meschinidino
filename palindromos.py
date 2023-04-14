#funcion que lee de los parametros una palabra (string)
#y determina si es un palindromo

def palindromo(palabra):
    if " " in palabra:
        palabra = palabra.split()
        palabra = "".join(palabra)

    if palabra[::-1] == palabra:
        return True