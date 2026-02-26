with open ("lab03-preguntas/preguntas.txt", "r", encoding = "utf-8") as file: #abrir el archivo 

    for linea in file: #se recorre linea por linea
        print (linea.strip()) #quita el salto de linea


def extraer_pregunta (pregunta: str) -> dict:
    
    lista = []
    lista += pregunta.split("|")

    if len(lista) < 2: raise ValueError("Faltan partes: se necesita 'pregunta|correcta|opciones...'")

    return {"pregunta": lista[0],
           
           "correcta": lista[1],
           
           "opciones": lista[2:]}




    


