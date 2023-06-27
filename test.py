from API.API import *
from pydantic import BaseModel

class Test(BaseModel):
    string: str = ""

def devolver():
    contenido = API.devolver(
        frase='Hola Mundo'
    )
    return contenido

