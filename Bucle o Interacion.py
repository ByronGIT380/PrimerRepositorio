#Bucle o Interacion
#while (mientras en español)

edades = [12, 34, 64, 21, 32, 18, 20]

actual=0
indice=0
while actual != edades[-1]:
    print(edades[indice])

    indice = indice + 1
    actual = edades[indice-1]