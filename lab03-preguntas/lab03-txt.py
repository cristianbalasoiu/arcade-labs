def extraer_pregunta (pregunta: str) -> dict:
    
    lista = []
    lista += pregunta.strip().split("|")

    if len(lista) < 2: raise ValueError("Faltan partes: se necesita 'pregunta|correcta|opciones...'")

    return {"pregunta": lista[0],
           
           "correcta": lista[1],
           
           "opciones": lista[1:]}

with open ("arcade-labs/lab03-preguntas/preguntas.txt", "r", encoding = "utf-8") as file: 

    lista_peguntas = []

    for linea in file:
        lista_peguntas.append(extraer_pregunta(linea))

for pregunta in lista_peguntas:
        salir = False
        print(f"{pregunta["pregunta"]}")
        print (f"Las opciones son: {pregunta["opciones"]}")

        salir = False

        while not salir:
            respuesta = input ("Cual es la respuesta a esta pregunta??: ")
            if respuesta.lower() == pregunta["correcta"].lower():
                print (f"Enhorabuena la respuesta correcta es: {pregunta["correcta"]}")
                salir = True
            else:
                print(f"Oooh la respuesta es incorrecta, prueba otra vez: ")
                salir = False









    


