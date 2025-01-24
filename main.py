# 1. Objetivo- criar uma api que disponibiliza a consulta, criação, ediçao e exclusao de livros
#2 . url base
#3. Endpoints
#3.1. localhost/livros (get)
#3.2. localhost/livros/{id} (get)
#3.3. localhost/livros/(id) (put)
#3.4. localhost/livros/(id) (delete)
#3.5. localhost/livros (post)
#4. Quais recursos - livros



from fastapi import FastAPI
from inDB import generate_books
from livros import Livro

app = FastAPI()

books = generate_books()



@app.get("/livros")
async def get_livros():
    return {"L":books}	



@app.get("/livro/{id}")
async def get_livro(id: int):
    for livro in books:
        if livro["Id"] == id:
            return livro
    return {"Erro":"Livro não encontrado"}




@app.post("/livro")
async def add_livro(livro: Livro):
    new_id = len(books) + 1
    new_book = {
        "Id": new_id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "ano": livro.ano
    }
    books.append(new_book)
    return {"mensagem: livro adicionado com sucesso!, livro": new_book}