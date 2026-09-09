from fastapi import APIRouter
from app.commands.executor import CommandExecutor
from app.api.schemas import ComandoRequest, ComandoResponse
from app.nlu.intent_parser import IntentParser


router = APIRouter()
command_executor = CommandExecutor()
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



@router.post("/comando")
def interpretar_comando_endpoint(comando: ComandoRequest):
    comando_interpretado = intent_parser.interpretar(comando.texto)

    resultado = command_executor.ejecutar(comando_interpretado)

    return {
        "comando": comando_interpretado,
        "resultado": resultado,
    }