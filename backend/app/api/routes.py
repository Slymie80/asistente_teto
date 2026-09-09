


from fastapi import FastAPI, APIRouter
from fastapi.responses import Response
from app.nlu.intent_parser import IntentParser
from app.api.schemas import ComandoRequest, ComandoResponse
from app.tts.sintetizador import sintetizar_texto

router = APIRouter()

intent_parser = IntentParser()
    
@router.get("/health")
def health_check():
    return {"status": "ok", "mensaje": "El backend está vivo"}

@router.get("/")
def root():
    return {"mensaje": "Asistente de voz - backend funcionando"}

@router.post("/comando", response_model=ComandoResponse)
def interpretar_comando_endpoint(comando: ComandoRequest):
    """
    Endpoint para interpretar un comando de texto.

    Args:
        comando (ComandoRequest): El comando de texto a interpretar.

    Returns:
        ComandoResponse: La respuesta con la intención, acción, parámetros y respuesta de texto.
    """
    resultado = intent_parser.interpretar(comando.texto)
    return ComandoResponse(**resultado)

@router.post("/comando/audio")
def interpretar_comando_audio(request:ComandoRequest):
    """
    Interpretar un comando de voz y devolver el audio sintetizado.

    Args:
        request (ComandoRequest): El comando de texto a interpretar.

    Returns:
        Response: La respuesta con el audio sintetizado.
    """
    resultado = interpretar_comando(request.texto)
    audio_bytes = sintetizar_texto(resultado["respuesta_texto"])
    return Response(content=audio_bytes,media_type="audio/wav")

