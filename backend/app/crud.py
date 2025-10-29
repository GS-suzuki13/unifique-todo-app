from .database import get_connection

def get_tasks():
    conn = get_connection()
    tasks = conn.execute("SELECT id, title, description, status FROM tasks").fetchall()
    conn.close()
    return [dict(task) for task in tasks]

def get_task_by_id(task_id: int):
    conn = get_connection()
    task = conn.execute("SELECT id, title, description, status FROM tasks WHERE id=?", (task_id,)).fetchone()
    conn.close()
    return dict(task) if task else None

def create_task(title, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
        (title, description, "pendente")
    )
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {
        "id": task_id,
        "title": title,
        "description": description,
        "status": "pendente"
    }

def update_task(id, title=None, description=None, status=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE tasks SET "
    params = []
    if title is not None:
        query += "title=?, "
        params.append(title)
    if description is not None:
        query += "description=?, "
        params.append(description)
    if status is not None:
        query += "status=?, "
        params.append(status)
    query = query.rstrip(", ") + " WHERE id=?"
    params.append(id)
    cursor.execute(query, params)
    conn.commit()
    conn.close()
    return cursor.rowcount

def delete_task(id):
    conn = get_connection()
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
