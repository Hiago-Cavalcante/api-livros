from pydantic import BaseModel

class Livro(BaseModel):
    titulo: str
    autor: str
    ano: int