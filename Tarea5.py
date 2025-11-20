#Tarea 5.
# Dado el archivo fasta, hacer un programa con las siguientes funcioens
#print(fasta.read())
# (1 punto)
# 1. Para todos los encabezados, lo imprima en el formato
# "Organismo <el nombre del fasta>, contig <el contenido del encabezado, sin el ">""
fasta=open("ejemplo.fasta","r")
#for linea in fasta:
    #if ">chr"is linea :   # hay una funcion q especifica si empieza con #startswith()
        #linea.replace(">chr ","ejemplo.fasta")
    #else:
        #print(linea)
nombre="Lepidoptera"#me lo invente , puse el nombre de una mariposa 
for linea in fasta :
    if  linea.startswith(">chr"):
        quitarsigno=linea.lstrip(">") # encontre esta funcion q quita esos caracteres o cualquie otro 
        lineaa = (f"Organismo {nombre}, contig  {quitarsigno} ")
        print(lineaa)
    else:
       print(linea)
    
#print(fasta.readline())

#linea.strip() es para limpiar las lineas pero en este caso no lo vi necesario  tampoco #with open('nombre_real_del_archivo.txt', 'r') as...:
 
# (2 punto)
# 2. Para cada línea de secuencia genómica, imprima su contenido de GC en el formato "GC línea <número de línea>: <GC"
#Tengo ya una funcion para contar el numero , tomada de la tarea pasada 
import os 
def GCcontent(input):
    adn = input.strip().upper()
    numcaracter = adn.count("G") + adn.count("C")+ adn.count("A")+ adn.count("T")
    if numcaracter == 0:
        return 0.0
    
    cantidad = adn.count("G") + adn.count("C")
    output = cantidad / numcaracter
    return output

#para contar las lineas y que diga "linea:1"
fasta=open("ejemplo.fasta","r")
def ContadorLinea(archivo):
    contador = 0
    for linea in archivo:
            contador += 1
            print((f"Línea {contador}: {linea.strip()}") )
    return contador

ContadorDeLineas=ContadorLinea(fasta)
# me era mas dificil añadir esta funcion  para el objetivo final , pero me ayudo a encontar otra forma 

print(ContadorLinea(fasta))
#nombre_del_archivo = "mi_archivo.fasta"
#total_lineas = contar_lineas_fasta(nombre_del_archivo)
#print(f"El archivo FASTA tiene {total_lineas} líneas en total.")

#print(GCcontent("AGGCC"))
fasta=open("ejemplo.fasta","r")
for linea in fasta :
    if  linea.startswith(">chr"):
        quitarsigno=linea.lstrip(">") # encontre esta funcion q quita esos caracteres o cualquie otro 
        lineaa = (f"Organismo {nombre}, contig  {quitarsigno} ")
        print(lineaa)
    else:
       print(GCcontent(linea))
#hasta aqui ya tengo el GC contenido 

fasta=open("ejemplo.fasta","r")
contador=0
for linea in fasta :
    if  linea.startswith(">chr"):
        quitarsigno=linea.lstrip(">") # encontre esta funcion q quita esos caracteres o cualquie otro 
        lineaa = (f"Organismo {nombre}, contig  {quitarsigno} ")
        print(lineaa)
    else:
        contador+= 1
        contenido_gc = GCcontent(linea)
        print (f"Línea {contador}:{contenido_gc}, <GC")

#resultado final 






# (2 puntos)
# 3. Para la primera secuencia de cada segmento, imprima su secuencia complementaria

# fasta=open("ejemplo.fasta","r")
# for line in fasta :
#      lineanueva= linea.strip()
# if linea_limpia.startswith('>'):
#             lineaok=True
# if lineaok== True:
#             for letra in linea_limpia:
#                 dic = letra.replace("A","T") + letra.replace("T","A") + letra.replace("G","C")  + letra.replace("C","G") 
#                 elif
#             break
    # vi que la funcion no funcionaba en algunos casos , por lo que debo usar "try" y un "diccionario"
fasta=open("ejemplo.fasta","r")
def secuenciaComplementaria(fasta):
    bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    encabezado= False
    
    try:
        with fasta :
            for linea in fasta:
                lineanueva= linea.strip()
                if not lineanueva:
                    continue
                if lineanueva.startswith('>'):
                    if encabezado:
                        break 
                    
                    encabezado= True
                    continue
                if encabezado:
                    secuencia_original = lineanueva
                    SecuenciaComplementaria = "".join([
                        bases.get(base.upper(), base) 
                        for base in secuencia_original
                    ])
                    
                    return SecuenciaComplementaria

    except FileNotFoundError:
        return "Error: Archivo no encontrado."
    
    return "Error:No se encontro secuencia."

complemento = secuenciaComplementaria(fasta)
print(complemento)

# (2 punto)
# 4. Imprima el número de línea donde encuentre el codón "ATG" en el formato "ATG en línea <número de línea>"
fasta=open("ejemplo.fasta","r")
contador=0
for lines in fasta :
    if lines.startswith("ATG"):
        contador+= 1
        print(f" ATG en linea <{contador}>")
        # resultado final 

# (1 punto)
# 5. Calcule el contenido GC total del archivo y lo imprima al final en formato "GC total del archivo: <GC>"
suma=""
fasta=open("ejemplo.fasta","r")
for linea in fasta :
    if  linea.startswith(">chr"):
        quitarsigno=linea.lstrip(">") # encontre esta funcion q quita esos caracteres o cualquie otro 
        lineaa = (f"Organismo {nombre}, contig  {quitarsigno} ")
        print(lineaa)
    else:
       adn = linea.strip().upper()
       numcaracter = adn.count("G") + adn.count("C")+ adn.count("A")+ adn.count("T")
       if numcaracter == 0:
           break
       else:
        cantidad = adn.count("G") + adn.count("C")
        output = cantidad / numcaracter
        suma+=output
        print(f"GC total del archivo: < {suma} >")


# ejemplo:
# fasta se usa para representar secuencias genómicas
# puede contener las secuencias de muchos organismos, cada una separada con un encabezado que comienza con ">"
# después del encabezado puede haber cualquier número de líneas con secuencias que pueden ser de nucleótidos o de aminoácidos

# Ejemplo:
# Archivo fasta: "humano.fasta"
# >chr 1
# AAAAATGTTTT
# AAAAAAAAAAA
# >chr 2
# GGGGGGGGGGG
# ATGCCCCCCCC
# AAAAAACCCCC
# atgCCCCCCCC

# nos debe de imprimir:
# Organismo humano, contig chr1
# GC línea 2: .09
# TTTTTACAAAA
# ATG en línea 2
# GC línea 3: 0
# Organismo humano, contig chr2
# GC línea 5: 1
# CCCCCCCCCCC
# GC línea 6: .81
# ATG en línea 6
# GC línea 7: .45
# GC línea 8: .81
# ATG en línea 8
# GC total del archivo: .53

# (2 a 8 puntos según la dificultad)
# 6. Para el formato que te toca, explicar el nombre, extensión del archivo, para qué se usa, en qué consiste (qué reglas debe seguir el archivo para cumplir el formato) y un ejemplo. 

# (2) fna
# (2) faa
# (3) genbank
# (4) fastq
# (4) gff3
# (6) Multiple Alignment Format
# (6) Newick
#(6) ClustalW
#(6) sam
#(8) json
#(8) xml
