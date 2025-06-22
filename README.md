# Fast Zero

Fast Zero é uma aplicação web desenvolvida com [FastAPI](https://fastapi.tiangolo.com/), focada em performance, organização e boas práticas de desenvolvimento. Este projeto utiliza o gerenciador de pacotes [Poetry](https://python-poetry.org/) e segue uma estrutura moderna de projeto Python com ferramentas integradas para desenvolvimento, testes, lint e formatação de código.

## 📦 Requisitos

- Python `>=3.12,<4.0`
- [Poetry](https://python-poetry.org/docs/#installation) instalado

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/fast-zero.git
cd fast-zero
```

Instale as dependências do projeto:

```bash
poetry install
```

## 💻 Execução em modo desenvolvimento

Para rodar o projeto localmente com recarregamento automático:

```bash
poetry run task dev
```

O servidor será iniciado em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🧪 Testes

Executar testes com `pytest` e gerar relatório de cobertura:

```bash
poetry run task test
```

Abrir o relatório de cobertura no navegador (HTML):

```bash
open htmlcov/index.html  # MacOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

## 🧹 Lint e Formatação

Verificar problemas com `ruff`:

```bash
poetry run task lint
```

Corrigir problemas automaticamente e formatar o código:

```bash
poetry run task format
```

## 📂 Estrutura do Projeto

```
fast-zero/
├── migrations/
│   └── versions/
│       └── 46eaae30d094_create_users_table.py
│   └── env.py
│   └── README.md
│   └── script.py.mako
├── src/
│   └── fast_zero/
│       └── app.py
│       └── models.py
│       └── schemas.py
│       └── settings.py
├── tests/
│   └── conftest.py
│   └── test_app.py
│   └── test_models.py
├── .env.example
├── .gitignore
├── .python-version
├── alembic.ini
├── poetry.lock
├── pyproject.toml
└── README.md
```

## ⚙️ Ferramentas e Bibliotecas

- **FastAPI**: Framework web assíncrono de alta performance
- **Uvicorn**: ASGI server para rodar a aplicação
- **Pytest**: Framework de testes
- **Ruff**: Linter e formatter rápido para Python
- **Httpx**: Cliente HTTP assíncrono
- **Taskipy**: Gerenciador de tarefas com integração ao Poetry

## 👤 Autor

- **Fábio Mattes**  
  [fabiomattes2007@gmail.com](mailto:fabiomattes2007@gmail.com)

---

> Este projeto está em desenvolvimento contínuo. Sinta-se à vontade para sugerir melhorias ou reportar problemas.