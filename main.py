"""
Archivo principal de la API.
Define los endpoints CRUD para usuarios usando FastAPI.
"""

from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from user_model import Genero, Role, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Carlos",
        apellidos="Fosado",
        genero=Genero.masculino,
        roles=[Role.admin],
    ),
    Usuario(
        id=uuid4(),
        nombre="Daniela",
        apellidos="León Jimenez",
        genero=Genero.femenino,
        roles=[Role.user],
    ),
    Usuario(
        id=uuid4(),
        nombre="Tania",
        apellidos="Marquéz Cabrera",
        genero=Genero.femenino,
        roles=[Role.admin],
    ),
    Usuario(
        id=uuid4(),
        nombre="Abril",
        apellidos="Guzmán Pazos",
        genero=Genero.femenino,
        roles=[Role.invitado],
    ),
]


@app.get("/")
async def root():
    """Endpoint raíz de prueba."""
    return {"saludo": "Hola 8B IDGS hijos de Rando"}


@app.get("/api/v1/users")
async def get_user():
    """Obtiene la lista de usuarios."""
    return db


@app.post("/api/v1/users", response_model=Usuario)
async def create_user(user: Usuario):
    """Crea un nuevo usuario."""
    db.append(user)
    return user


@app.put("/api/v1/users/{user_id}", response_model=Usuario)
async def update_user(user_id: UUID, user_update: Usuario):
    """Actualiza un usuario existente por su ID."""
    for index, user in enumerate(db):
        if user.id == user_id:
            user_update.id = user_id
            db[index] = user_update
            return user_update
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    """Elimina un usuario por su ID."""
    for user in db[:]:
        if user.id == user_id:
            db.remove(user)
            return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
