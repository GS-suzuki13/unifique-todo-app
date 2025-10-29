from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post("/tasks", json={
        "title": "Tarefa de teste",
        "description": "Testando criação de tarefa"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Tarefa de teste"
    assert data["description"] == "Testando criação de tarefa"
    assert data["status"] == "pendente"


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_task():
    # Cria uma tarefa primeiro
    response = client.post("/tasks", json={
        "title": "Atualizar tarefa",
        "description": "Antes da atualização"
    })
    task_id = response.json()["id"]

    # Atualiza a tarefa
    update_response = client.put(f"/tasks/{task_id}", json={
        "title": "Tarefa Atualizada",
        "description": "Depois da atualização",
        "status": "concluída"
    })
    assert update_response.status_code == 200
    updated = update_response.json()
    assert updated["title"] == "Tarefa Atualizada"
    assert updated["status"] == "concluída"


def test_delete_task():
    # Cria uma tarefa
    response = client.post("/tasks", json={
        "title": "Excluir tarefa",
        "description": "Será excluída"
    })
    task_id = response.json()["id"]

    # Deleta a tarefa
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Tarefa removida com sucesso"


def test_task_not_found():
    response = client.get("/tasks/9999")
    assert response.status_code in [404, 400]
