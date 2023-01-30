# API Movimentações Financeiras

Aplicação para parsear arquivos CNAB.txt, armazenando-os em um banco de dados SQLite3.

## **Endpoints**

A API tem um total de 2 endpoints, sendo eles:

- http://127.0.0.1:8000/api/cnab/upload/
- http://127.0.0.1:8000/api/stores/

## Índice:

- [API Movimentações Financeiras](#api-movimentações-financeiras)
  - [**Endpoints**](#endpoints)
  - [Índice:](#índice)
  - [1. **Tecnologias utilizadas**](#1-tecnologias-utilizadas)
  - [2. Instalação](#2-instalação)

## 1. **Tecnologias utilizadas**

- Python 3.0+
- Django Rest Framework
- Django Framework
- SQlite3

## 2. Instalação

- Clone o repositório pela chave SSH.

- Ative o ambiente virtual em seu computador
  - Criando um ambiente virtual
    ```
    python -m venv venv
    ```
  - Ativando no Linux
    ```
    source venv/bin/activate
    ```
  - Ativando no Windows
    ```
    .\venv\Scripts\activate
    ```
- Instalando pacotes utilizados

  ```
  pip install -r requirements.txt
  ```

- Criando banco de dados SQlite3
  ```
    python manage.py migrate
  ```
- Rodando o servidor
  ```
    python manage.py runserver
  ```

| :rotating_light: | Para desativar o ambiente virtual, use:

```
deactivate
```
