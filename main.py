from fastapi import FastAPI
from test import Test, devolver

app = FastAPI()

@app.post('/reversa')
def reversa(contenido: Test):
    contenido = devolver()
    return {
        'contenido': contenido
    }
