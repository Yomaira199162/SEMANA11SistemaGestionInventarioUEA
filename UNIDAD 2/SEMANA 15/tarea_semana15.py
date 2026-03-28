import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas - GUI")
        self.root.geometry("400x450")

        # --- Interfaz Gráfica ---

        # Campo de entrada (Entry) para nuevas tareas
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        # Vincular la tecla Enter para añadir tareas
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Botones de acción
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.add_button = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(btn_frame, text="Marcar Completada", command=self.mark_completed, bg="#2196F3",
                                         fg="white")
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task, bg="#f44336",
                                       fg="white")
        self.delete_button.grid(row=0, column=2, padx=5)

        # Componente de lista (Listbox)
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Evento opcional: Doble clic para marcar como completada
        self.tasks_listbox.bind('<Double-1>', lambda event: self.mark_completed())

    # --- Lógica de la Aplicación y Manejo de Eventos ---

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

    def mark_completed(self):
        """Cambia visualmente el estado de la tarea seleccionada."""
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)

            # Si ya está completada, no hacemos nada o avisamos
            if "✔" in task:
                return

            # Modificar el texto para reflejar que está completada
            completed_task = f"{task} ✔"
            self.tasks_listbox.delete(index)
            self.tasks_listbox.insert(index, completed_task)

            # Cambiar color de fondo del ítem (opcional visual)
            self.tasks_listbox.itemconfig(index, fg="gray")
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para marcarla.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()