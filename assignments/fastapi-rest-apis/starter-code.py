"""
FastAPI REST API Starter Code
Este arquivo contém um template inicial para construir uma API REST com FastAPI.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Criar a aplicação FastAPI
app = FastAPI()

# TODO: Defina seu modelo de dados usando Pydantic
# Exemplo:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None


# Armazenamento em memória (substitua por um banco de dados real em produção)
items_db = {}
next_id = 1


# TODO: Implemente as rotas da sua API

# Rota GET simples para testar se a API está funcionando
@app.get("/")
def read_root():
    """Rota raiz que retorna uma mensagem de saudação."""
    return {"message": "Bem-vindo à minha API REST com FastAPI!"}


# TODO: Adicione as rotas para:
# - POST /items (criar um novo item)
# - GET /items (listar todos os itens)
# - GET /items/{item_id} (buscar um item específico)
# - PUT /items/{item_id} (atualizar um item)
# - DELETE /items/{item_id} (deletar um item)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
