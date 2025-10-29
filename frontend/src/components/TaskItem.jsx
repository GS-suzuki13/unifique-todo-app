export default function TaskItem({ task, onEdit, onDelete, onToggle }) {
  const statusColor =
    task.status === "concluída" ? "text-green-600" : "text-gray-500";

  return (
    <div className="flex justify-between items-center bg-gray-100 p-3 rounded-md shadow-sm">
      <div>
        <h3 className={`text-lg font-semibold ${statusColor}`}>
          {task.title}
        </h3>
        <p className="text-sm text-gray-600">{task.description}</p>
        <p className="text-xs italic text-gray-400">
          Status: {task.status}
        </p>
      </div>

      <div className="flex gap-2">
        <button
          onClick={() => onToggle(task)}
          className="text-sm bg-yellow-500 text-white px-2 py-1 rounded hover:bg-yellow-600"
        >
          {task.status === "pendente" ? "Concluir" : "Reabrir"}
        </button>

        <button
          onClick={() => onEdit(task)}
          className="text-sm bg-blue-500 text-white px-2 py-1 rounded hover:bg-blue-600"
        >
          Editar
        </button>

        <button
          onClick={() => onDelete(task.id)}
          className="text-sm bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
        >
          Excluir
        </button>
      </div>
    </div>
  );
}
