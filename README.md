# Aplicação CRUD de Veículos

Esta é uma aplicação Django REST API que permite realizar operações CRUD (Criar, Ler, Atualizar, Excluir) em objetos Veículo.

## Funcionalidades

- Criar novos veículos
- Recuperar uma lista de todos os veículos
- Recuperar um veículo específico pela sua placa
- Recuperar veículos por modelo
- Atualizar um veículo existente
- Excluir um veículo

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework

## Instalação

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/crud-veiculos.git
```

2. Navegue até o diretório do projeto:

```
cd crud-veiculos
```

3. Crie um ambiente virtual e ative-o:

```
python -m venv env
source env/bin/activate  # No Windows, use `env\Scripts\activate`
```

4. Instale as dependências necessárias:

```
pip install -r requirements.txt
```

5. Aplique as migrações do banco de dados:

```
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

A API estará acessível em `http://localhost:8000/`.

## Endpoints da API

### Veículos

- `GET /api/veiculos/` - Recuperar uma lista de todos os veículos
- `GET /api/veiculos/?placa=<placa>` - Recuperar um veículo específico pela sua placa
- `GET /api/veiculos/modelo/<modelo>` - Recuperar veículos por modelo
- `POST /api/veiculos/` - Criar um novo veículo
- `PUT /api/veiculos/` - Atualizar um veículo existente
- `DELETE /api/veiculos/` - Excluir um veículo

## Exemplos de Requisições

### Criar um Veículo

```
POST /api/veiculos/
Content-Type: application/json

{
    "modelo": "Toyota Corolla",
    "placa": "ABC-1234",
    "ano": 2020,
    "cor": "Preto"
}
```

### Recuperar Todos os Veículos

```
GET /api/veiculos/
```

### Recuperar um Veículo pela Placa

```
GET /api/veiculos/?placa=ABC-1234
```

### Recuperar Veículos por Modelo

```
GET /api/veiculos/modelo/Toyota%20Corolla
```

### Atualizar um Veículo

```
PUT /api/veiculos/
Content-Type: application/json

{
    "modelo": "Toyota Corolla",
    "placa": "ABC-1234",
    "ano": 2021,
    "cor": "Branco"
}
```

### Excluir um Veículo

```
DELETE /api/veiculos/?placa=ABC-1234
```

## Tamo junto!
