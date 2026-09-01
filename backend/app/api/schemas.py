from pydantic import BaseModel

class ComandoRequest(BaseModel):
    texto: str

class ComandoResponse(BaseModel):
    intencion: str
    accion: str
    parametros: dict = {}
    respuesta_texto: str


