from pydantic import BaseModel ,Field

class ComandoRequest(BaseModel):
    texto: str = Field(..., description="El texto del comando")

class ComandoResponse(BaseModel):
    intencion: str = Field(..., description="La intención del comando")
    accion: str = Field(..., description="La acción a realizar")
    parametros: dict = Field(default_factory=dict, description="Los parámetros del comando")
    respuesta_texto: str = Field(..., description="La respuesta en texto del comando")


