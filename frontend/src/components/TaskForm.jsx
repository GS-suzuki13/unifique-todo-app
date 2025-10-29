import { useState, useEffect } from "react";

export default function TaskForm({ onSubmit, editingTask }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    if (editingTask) {
      setTitle(editingTask.title);
      setDescription(editingTask.description || "");
    } else {
      setTitle("");
      setDescription("");
    }
  }, [editingTask]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ title, description });
    setTitle("");
    setDescription("");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white shadow-md rounded-lg p-4 flex flex-col gap-3"
    >
      <h2 className="text-xl font-semibold text-gray-800">
        {editingTask ? "Editar Tarefa" : "Nova Tarefa"}
      </h2>

      <input
        type="text"
        placeholder="Título"
        className="border rounded px-3 py-2"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />

      <textarea
        placeholder="Descrição"
        className="border rounded px-3 py-2"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <button
        type="submit"
        className="bg-blue-600 hover:bg-blue-700 text-white rounded py-2"
      >
        {editingTask ? "Salvar Alterações" : "Adicionar"}
      </button>
    </form>
  );
}
