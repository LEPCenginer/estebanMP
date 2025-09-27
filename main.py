import numpy as np
from fastapi import FastAPI

from routers import diabetes_router
from schemas.diabetes_schemas import PatientData

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()
app.include_router(diabetes_router.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # quién puede hacer peticiones
    allow_credentials=True,
    allow_methods=["*"],             # permite todos los métodos: GET, POST, PUT, DELETE
    allow_headers=["*"],             # permite todas las cabeceras
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


