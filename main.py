import tkinter as tk

class TodoAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App")

        self.tasks = []

        # Entry for adding tasks
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Buttons for actions
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=1, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_selected_tasks)
        self.delete_button.grid(row=1, column=1, padx=10, pady=10)

        # Listbox for displaying tasks
        self.tasks_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.MULTIPLE)
        self.tasks_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"text": task, "done": False})
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Empty Task", "Please enter a task.")

    def view_tasks(self):
        if not self.tasks:
            tk.messagebox.showinfo("No Tasks", "No tasks available.")
        else:
            tasks_text = "\n".join(task["text"] for task in self.tasks)
            tk.messagebox.showinfo("Tasks", f"Tasks:\n{tasks_text}")

    def delete_selected_tasks(self):
        selected_task_indices = self.tasks_listbox.curselection()
        if selected_task_indices:
            for index in sorted(selected_task_indices, reverse=True):
                del self.tasks[index]
            self.update_tasks_listbox()
        else:
            tk.messagebox.showwarning("No Task Selected", "Please select a task to delete.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = f"[{'✔' if task['done'] else ' '}] {task['text']}"
            self.tasks_listbox.insert(tk.END, task_text)

def main():
    root = tk.Tk()
    todo_app_gui = TodoAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
