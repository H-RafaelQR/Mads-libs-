def convert_list(palabra, palabra_lista, incognita):
    #generar la incognita
    for i in range(len(palabra)):
        incognita.append("-")
        letra = palabra[i]
        palabra_lista.append(letra) 

if __name__ == '__main__':
    
    palabra = "Peru"
    palabra = palabra.lower() #minusculas
    palabra_lista = []
    incognita = []
    terminado = False

    #Crear las listas
    convert_list(palabra, palabra_lista, incognita)


    #comparar las listas
    while terminado == False:
        print(incognita)
        alternativa = str(input("Por favor digite un caracter: "))
        for y in range(len(palabra)):
            if str(palabra_lista[y]) == str(alternativa):
                incognita[y] = alternativa

        if incognita == palabra_lista: 
            terminado = True
            break
    
    
    print("Exacto la palabra es: " + str(palabra))
    print('Ganaste')