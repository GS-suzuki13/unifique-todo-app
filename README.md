# 🗂️ Unifique To-Do App

**Unifique To-Do App** é uma aplicação web completa para gerenciamento de tarefas, desenvolvida com **React (frontend)** e **FastAPI (backend)**.  
O objetivo é oferecer uma interface simples, responsiva e funcional para criar, editar, listar, concluir e excluir tarefas, utilizando uma arquitetura moderna e escalável.

---

## 🚀 Funcionalidades

### ✅ Frontend (React + TailwindCSS)
- Listar todas as tarefas
- Criar novas tarefas
- Editar tarefas existentes
- Marcar como concluídas / pendentes
- Excluir tarefas
- Comunicação com o backend via **Axios**
- Interface responsiva e intuitiva

### ⚙️ Backend (FastAPI + SQLite)
- API REST completa para CRUD de tarefas (`/tasks`)
- Banco de dados local SQLite com SQLAlchemy
- Estrutura modular (models, schemas, crud, routes)
- Middleware CORS configurado para integração com o frontend

---

## 🧱 Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|-------------|
| **Frontend** | React, Vite, Axios, TailwindCSS |
| **Backend** | FastAPI, Uvicorn, SQLAlchemy, SQLite |
| **Infraestrutura** | Docker, Docker Compose |
| **Testes** | Pytest |
| **Linguagens** | Python 3.11+, JavaScript (ES6+) |

---

## 🧩 Estrutura do Projeto

unifique-todo-app/
│
├── backend/
│ ├── app/
│ │ ├── crud.py
│ │ ├── database.py
│ │ ├── main.py
│ │ ├── models.py
│ │ ├── schemas.py
│ │ └── database.db
│ │
│ ├── tests/
│ │ ├── test_tasks.py
│ │ ├── conftest.py
│ │ └── init.py
│ │
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/
│ ├── public/
│ │ └── vite.svg
│ ├── src/
│ │ ├── assets/
│ │ ├── components/
│ │ ├── api.js
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ └── index.css
│ │
│ ├── package.json
│ ├── tailwind.config.js
│ └── Dockerfile
│
├── docker-compose.yml
└── README.md


---

## 🐳 Como Executar com Docker (recomendado)

> Certifique-se de ter o **Docker** e o **Docker Compose** instalados em seu sistema.

### 1️⃣ Build e inicialização dos containers:
```bash
docker compose up --build

2️⃣ Acesse a aplicação:

    Frontend: http://localhost:5173

Backend (API): http://localhost:8000/tasks
💡 Execução Manual (sem Docker)
Backend

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend

cd frontend
npm install
npm run dev

🧠 Testes Automatizados

Para rodar os testes do backend:

cd backend
pytest -v

📜 Licença

Este projeto foi desenvolvido para fins educacionais e demonstração de arquitetura full-stack com React + FastAPI + Docker.
Sinta-se à vontade para clonar, adaptar e evoluir o projeto conforme necessário.
✨ Autor

Desenvolvido por Gustavo Suzuki — Projeto Unifique To-Do App 🧩
