from pydantic import BaseModel
from typing import Optional


class UsuarioShema(BaseModel):
    nombre: str
    apellido: Optional[str] = None
    email: str
    password: str
    telefono: Optional[str] = None
    fecha: Optional[str] = None


class TareaSchema(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    prioridad: Optional[str] = "media"
    clasificacion: Optional[str] = "personal"