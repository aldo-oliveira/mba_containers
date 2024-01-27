from fastapi import FastAPI
import os

TESTE = os.environ.get('TESTE')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Estou dentro do container"}

@app.get("/variavel_ambiente")
async def verificar_variavel_de_ambiente():
    return {"TESTE": TESTE}