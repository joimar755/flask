from pydantic import BaseModel
class User(BaseModel):
    nombre: str
    apellido: str
    sex: str
    role: int
    email: str
    password: str