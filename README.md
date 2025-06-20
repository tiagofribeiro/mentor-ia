# Mentor-IA

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

Assistente de aprendizado (ainda que sempre aprendendo...)

<br>

## Introdução

Este projeto almeja criar um assistente virtual acadêmico utilizando LLMs.  
  
  
Aplicação desenvolvida em [Python](https://www.python.org/), usando [Django](https://www.djangoproject.com/) e [DRF](https://www.django-rest-framework.org/).

<br>

## Como executar

> É necessário ter instalado o [Docker](https://www.docker.com/) (e o compose) para execução dos containers e criação automática da estrutura e uma key para execução

<br>

Crie um arquivo `.env` na raíz do projeto com a mesma estrutura de [`.env.example`](/.env.example).  

> Também é necessária uma chave para autenticação com um LLM OpenAI (por enquanto).  
> A variável se chama: `OPENROUTER_API_KEY`, mas não é obrigatório o uso do [OpenRouter](https://openrouter.ai/).

<br>

Ainda na raíz do diretório, execute:
```bash
docker compose up --build 
```

<br>

Esse comando já executa a imagem do banco, o servidor para o Django e realiza as operações iniciais necessárias (criação de usuários e tabelas, instalação de pacote etc).

<br>

A partir daí, a API deve estar em execução na porta 8000.  
Para verificar o funcionamento e ver os endpoints disponíveis, acesse: [127.0.0.1:8000/api/swagger](http://127.0.0.1:8000/api/swagger)

> As credenciais para realizar o login e obter o token pela primeira vez são as váriaveis `DJANGO_SUPERUSER_` no `.env`

<br>

## Desenvolvimento

Para auxiliar no desenvolvimento do projeto, fiz uns rascunhos no FigJam. Você pode acessá-lo clicando [aqui](https://www.figma.com/board/krnC8naMoXhWwbJ3ASpnHn/mentor-ia?node-id=0-1&t=lUAq6zyc0ziU33qE-1)!


<br>
<br>
<br>

> ##### Em breve novas atualizações! [Você pode dar uma olhadas nas minhas outras ideias enquanto isso...](https://github.com/tiagofribeiro)
