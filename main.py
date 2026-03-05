from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import date, time

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Microservicio de reservas funcionando"}


# Lista para almacenar reservas
reservas_db = []

# Clase usando Pydantic
class Reserva(BaseModel):
    id_reserva: int = Field(..., example=1)
    id_sala: int = Field(..., example=101)
    id_usuario: int = Field(..., example=2001)
    fecha: date = Field(..., example="2026-03-10")
    hora_inicio: time = Field(..., example="08:00:00")
    hora_fin: time = Field(..., example="10:00:00")
    personas: int = Field(..., gt=0, example=25)
    estado: str = Field(..., example="confirmada")

# Endpoint POST para registrar una nueva reserva
@app.post("/reservas", response_model=Reserva)
def crear_reserva(reserva: Reserva):
    
    # Validación adicional: hora_fin debe ser mayor que hora_inicio
    if reserva.hora_fin <= reserva.hora_inicio:
        raise HTTPException(
            status_code=400,
            detail="La hora_fin debe ser mayor que hora_inicio"
        )
    
    reservas_db.append(reserva)
    return reserva

# Endpoint GET para consultar todas las reservas
@app.get("/reservas", response_model=List[Reserva])
def obtener_reservas():
    return reservas_db

