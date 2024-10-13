#for
#Sintaxis
#for elemento in iterable

edades = [12, 34, 64, 21, 32, 18, 20]

#for elemento in edades: 
#   print(elemento)

#----------------------------------------------------------------------------------------------

minimo = edades[0]
maximo = edades[0]

for edad in edades:
    if edad > maximo:
        maximo = edad
    if edad < minimo:
        minimo = edad

    print(maximo)
    print(minimo)
