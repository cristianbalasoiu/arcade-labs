def extraer_pregunta (pregunta: str) -> dict:
    
    lista = []
    lista += pregunta.split("|")

    if len(lista) < 2: raise ValueError("Faltan partes: se necesita 'pregunta|correcta|opciones...'")

    return {"pregunta": lista[0],
           
           "correcta": lista[1],
           
           "opciones": lista[2:]}

with open ("arcade-labs/lab03-preguntas/preguntas.txt", encoding = "utf-8") as file: 

    lista_peguntas = []

    for linea in file:
        print (linea.strip()) 
        lista_peguntas.append(extraer_pregunta(linea))

    salir = False

    for pregunta in lista_peguntas:
        salir = False
        print(f"{pregunta["pregunta"]}")
        print (f"{pregunta["opciones"]}")
        while not salir:
            respuesta = input (print(f"Cual es la respuesta a esta pregunta: "))
            if respuesta == pregunta["correcta"]:
                print (f"Enhorabuena la respues correcta es: {pregunta["correcta"]}")
                salir = True
            else:
                print(f"Oooh la respuesta es incorrecta, prueba otra vez: ")
                salir = False









    


