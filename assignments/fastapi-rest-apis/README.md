# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Nesta tarefa, você criará uma API REST completa usando o framework FastAPI. Você aprenderá como definir rotas, lidar com requisições HTTP, validar dados, e implementar um banco de dados simples para armazenar informações.

## 📝 Tarefas

### 🛠️ Task 1: Configurar o Projeto FastAPI

#### Description
Configure um novo projeto Python com FastAPI instalado e crie uma aplicação básica que responda a uma requisição GET simples.

#### Requirements
Completed program should:

- Ter o FastAPI instalado e importado corretamente
- Criar uma aplicação FastAPI básica
- Definir uma rota GET que retorna uma mensagem de saudação
- Executar a aplicação em um servidor local (usando Uvicorn)


### 🛠️ Task 2: Implementar um Modelo de Dados

#### Description
Crie um modelo de dados usando Pydantic para representar um recurso (por exemplo, um usuário, um livro ou um produto). Use este modelo para validar dados de entrada na sua API.

#### Requirements
Completed program should:

- Definir um modelo Pydantic com pelo menos 3 campos
- Implementar validação de tipos de dados
- Usar o modelo em uma rota POST para criar novos recursos
- Retornar uma resposta apropriada com o recurso criado


### 🛠️ Task 3: Implementar Operações CRUD

#### Description
Estenda sua API para implementar as operações completas de CRUD (Create, Read, Update, Delete) em um armazenamento em memória (lista ou dicionário).

#### Requirements
Completed program should:

- Ter uma rota POST para criar recursos
- Ter uma rota GET para listar todos os recursos
- Ter uma rota GET com parâmetro de ID para buscar um recurso específico
- Ter uma rota PUT para atualizar um recurso existente
- Ter uma rota DELETE para remover um recurso
- Retornar códigos de status HTTP apropriados (200, 201, 404, etc.)


### 🛠️ Task 4: Adicionar Tratamento de Erros

#### Description
Implemente tratamento robusto de erros na sua API, incluindo validação de entrada e tratamento de casos onde recursos não são encontrados.

#### Requirements
Completed program should:

- Validar que os dados enviados correspondem ao modelo Pydantic
- Retornar erros 404 quando um recurso não é encontrado
- Retornar erros 400 para dados inválidos
- Usar HTTPException para retornar mensagens de erro claras
- Fornecer mensagens de erro informativas ao usuário
