from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field # Importa Field para el tip extra abajo
from enum import Enum

class Genero(str, Enum):
    # CORREGIDO: Usar = en lugar de :
    masculino = "masculino"
    femenino = "femenino"
    otro = "otro"

class Role(str, Enum):
    # CORREGIDO: Usar = en lugar de :
    admin = "admin"
    user = "user"
    invitado = "invitado"

class Usuario(BaseModel):
    # NOTA IMPORTANTE: Ver explicación abajo sobre default_factory
    id: Optional[UUID] = Field(default_factory=uuid4) 
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]