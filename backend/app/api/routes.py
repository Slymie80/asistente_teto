from fastapi import APIRouter

from app.api.schemas import ComandoRequest, ComandoResponse
from app.nlu.intent_parser import IntentParser


router = APIRouter()

intent_parser = IntentParser()


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "mensaje": "El backend está vivo"
    }


@router.get("/")
def root():
    return {
        "mensaje": "Asistente de voz - backend funcionando"
    }


@router.post("/comando", response_model=ComandoResponse)
def interpretar_comando_endpoint(comando: ComandoRequest):
    resultado = intent_parser.interpretar(comando.texto)

    return ComandoResponse(**resultado)