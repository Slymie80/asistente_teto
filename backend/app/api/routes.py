from fastapi import FastAPI, APIRouter
from fastapi.responses import Response
from app.nlu.intent_parser import interpretar_comando
from app.api.schemas import ComandoRequest, ComandoResponse
from app.tts.sintetizador import sintetizar_texto

router = APIRouter()
    
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
    resultado = interpretar_comando(comando.texto)
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

