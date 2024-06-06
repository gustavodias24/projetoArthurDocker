# Projeto Checklist com Flask e MongoDB

Este é um projeto simples de checklist construído com Flask para a API e MongoDB como banco de dados. Ele inclui uma interface de usuário básica utilizando HTML e JavaScript.

## Pré-requisitos

Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina. Você pode encontrar instruções de instalação no site oficial do [Docker](https://docs.docker.com/get-docker/) e do [Docker Compose](https://docs.docker.com/compose/install/).

## Configuração

1. Clone este repositório para sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/projetoArthurDocker.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd projetoArthurDocker
    ```

3. Certifique-se de que os arquivos Dockerfile e docker-compose.yml estejam presentes nos diretórios `api/` e `frontend/`.

## Construção e Execução

1. Construa as imagens dos contêineres utilizando o Docker Compose:

    ```bash
    docker-compose build
    ```

2. Inicie os serviços com o Docker Compose:

    ```bash
    docker-compose up
    ```

3. Acesse a aplicação em um navegador da web:

    [http://localhost](http://localhost)

## Como Funciona

- A API Flask é executada no contêiner denominado `api`, exposta na porta `5000`.
- O front-end estático (HTML, JavaScript) é servido por um servidor Nginx no contêiner denominado `frontend`, exposto na porta `80`.
- O MongoDB é executado em um contêiner denominado `mongo`, exposto na porta `27017`.

## Personalização

- Para adicionar mais funcionalidades à aplicação, você pode modificar os arquivos `app.py` na pasta `api/` e `index.html` na pasta `frontend/`.
- Certifique-se de ajustar as configurações do Dockerfile e docker-compose.yml, conforme necessário.

