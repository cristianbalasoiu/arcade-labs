with open ("lab03-preguntas/preguntas.txt", "r", encoding = "utf-8") as file: #abrir el archivo 

    for linea in file: #se recorre linea por linea
        print (linea.strip()) #quita el salto de linea


def extraer_pregunta (pregunta: str) -> dict:
    
    lista = []
    lista += pregunta.split("|")

   return {"pregunta": "lista[0]",
           
           "correcta": "lista[1]",
           
           "opciones": "lista[2:]"}


    


