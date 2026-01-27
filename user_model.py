"""
Modelo de usuario para el sistema.
Define enums y el esquema base usando Pydantic.
"""

from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Genero(str, Enum):
    """Enum que representa el género del usuario."""

    masculino = "masculino"  # pylint: disable=invalid-name
    femenino = "femenino"    # pylint: disable=invalid-name
    otro = "otro"            # pylint: disable=invalid-name


class Role(str, Enum):
    """Enum que representa los roles del usuario."""

    admin = "admin"          # pylint: disable=invalid-name
    user = "user"            # pylint: disable=invalid-name
    invitado = "invitado"    # pylint: disable=invalid-name


class Usuario(BaseModel):
    """Modelo principal de usuario."""

    id: Optional[UUID] = Field(default_factory=uuid4)
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
