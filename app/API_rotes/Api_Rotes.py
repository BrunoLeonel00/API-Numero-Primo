from app.Aplicacao.functions import proximo_primo
from fastapi import APIRouter, HTTPException


router = APIRouter()

@router.get("/entrada/{numero}")
def read_user(numero: int):
    if numero < 0:
        raise   HTTPException(status_code=400, detail="O campo informado deve ser um inteiro positivo.")
    resultado = proximo_primo(numero)
    return resultado


