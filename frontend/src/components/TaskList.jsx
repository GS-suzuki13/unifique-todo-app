import TaskItem from "./TaskItem";

export default function TaskList({ tasks, onEdit, onDelete, onToggle }) {
  if (!tasks.length)
    return <p className="text-center text-gray-500">Nenhuma tarefa ainda.</p>;

  return (
    <div className="flex flex-col gap-3">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          onEdit={onEdit}
          onDelete={onDelete}
          onToggle={onToggle}
        />
      ))}
    </div>
  );
}
