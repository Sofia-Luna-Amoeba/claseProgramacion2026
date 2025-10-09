#complemento

#Tarea 4.

#Escribir la función con el nombre dado en cada número. Debe recibir los parámetros indicados (input) y regrese el valor indicado (output).
#Para los problemas 1-3 hay que probar la función con los ejemplos mostrados, para los 4-6 hay que hacer sus propios casos de prueba y explicar un poco para qué hacen la prueba (ver ejemplo en el problema 1). Está permitido usar código que hemos hecho en clase y los métodos de strings, pero tienen que hacer su propia función con el nombre que se pide.
#(1.5 puntos)
#1. MiEsDigito
#Input: un string
#Output: Booleano indicando si el string se compone de puros números
 # probamos si funciona con puros números
def MiEsDigito (input):
    output=""
    output=input.isdigit()
    return output
print(MiEsDigito("1234"))


#MiEsDigito("abcd") == False # probamos si funciona con puras letras
def MiEsDigito (input):
    output=""
    output=input.isdigit()
    return output
print(MiEsDigito("abcd"))


MiEsDigito("123a") == False # probamos si hay números y letras
def MiEsDigito (input):
    output=""
    output=input.isdigit()
    return output
print(MiEsDigito("123a"))

MiEsDigito("12a4") == False # probamos que la letra esté a la mitad de los números
def MiEsDigito (input):
    output=""
    output=input.isdigit()
    return output
print(MiEsDigito("12a4"))

#para comprobar 
print(MiEsDigito("1234") == True)
print(MiEsDigito("abcd") == False)
print(MiEsDigito("123a") == False)
print(MiEsDigito("12a4") == False)

# (1.5 puntos)
# 2. MiConteo
# Input: dos strings, el segundo es sólo un caracter
# Output: un entero con el número de veces que aparece el segundo string en el primer string
# MiConteo("hola mundo","o") == 2
def MiConteo (input,output):
    output=input.count(output)
    return output

print(MiConteo("hola mundo","o") == 2)

print(MiConteo("hola mundo","h") == 1)

print(MiConteo("hola mundo"," ") == 1)

print(MiConteo("hola mundo","r") == 0)

print(MiConteo("hola mundo","!") == 0)

print(MiConteo("hola mundo","") == 0)

print(MiConteo("","A") == 0)

# (2 puntos)
# 3. GCcontent
# Input: un string con una secuencia de ADN
# Output: porcentaje de caracteres que son "G" ó "C"
# GCcontent("ATGC") == .5

def GCcontent(input):
    adn = input.upper() 
    numcaracter = adn.count("G") + adn.count("C")+ adn.count("A")+ adn.count("T")
    if numcaracter == 0:
        return 0 
    
    cantidad = adn.count("G") + adn.count("C")
    output = cantidad / numcaracter
    return output

print((GCcontent("ATGC")))
print(GCcontent("AAAA"))
print(GCcontent("ATGC"))
print(GCcontent("GGCC"))

print(GCcontent("ATGC") == .5)
GCcontent("") == 0
GCcontent("AAAA") == 0
GCcontent("ATgc") == .5
GCcontent("GGCC") == 1

# (2 puntos)
# 4. MiSwapCase
# Input: un string
# Output: un string que invierta las mayúsculas y minúsculas
def MiSwapCase(input):
    output=input.swapcase()
    return output

print(MiSwapCase("hOla"))
print(MiSwapCase("ZkibGAi"))
print(MiSwapCase("sKibiDy"))
# (1 punto)
# 5. MiCapitalize
# Input: un string
# Output: un string que tenga la primera letra en mayúsculas
def MiConteo (input):
    output=input.capitalize()
    return output
# me da la primera letra en mayusculas por la funcion 
print(MiConteo ("input"))
print(MiConteo ("skibidi"))
print(MiConteo ("sjsjhs"))

# (2 puntos)
# 6. EsPar
# Input: Un número entero
# Output: Imprime si el número es par o impar, no debe regresar nada
def EsPar (input):
    if input % 2 == 0 :
        return input
# me sale none porque no es y cuando es , lo imprime
print(EsPar(6))
print(EsPar(5))


