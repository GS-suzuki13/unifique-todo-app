import { useEffect, useState } from "react";
import {
  getTasks,
  createTask,
  updateTask,
  deleteTask,
} from "./api";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [editingTask, setEditingTask] = useState(null);

  const loadTasks = async () => {
    const res = await getTasks();
    setTasks(res.data);
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const handleCreate = async (data) => {
    if (editingTask) {
      await updateTask(editingTask.id, { ...data });
      setEditingTask(null);
    } else {
      await createTask(data);
    }
    loadTasks();
  };

  const handleDelete = async (id) => {
    await deleteTask(id);
    loadTasks();
  };

  const handleToggle = async (task) => {
    const newStatus = task.status === "pendente" ? "concluída" : "pendente";
    await updateTask(task.id, { status: newStatus });
    loadTasks();
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6 flex flex-col items-center">
      <div className="max-w-2xl w-full flex flex-col gap-6">
        <h1 className="text-3xl font-bold text-center text-blue-700">
          Gerenciador de Tarefas
        </h1>

        <TaskForm onSubmit={handleCreate} editingTask={editingTask} />

        <TaskList
          tasks={tasks}
          onEdit={setEditingTask}
          onDelete={handleDelete}
          onToggle={handleToggle}
        />
      </div>
    </div>
  );
}
