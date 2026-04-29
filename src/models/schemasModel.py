from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=8, max_length=100)
    email: EmailStr
    apellido: str = Field(min_length=1, max_length=100)

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class TareaSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    descripcion: Optional[str] = Field(None, max_length=200)
    prioridad: str = "media"
    clasificacion: str = "personal"