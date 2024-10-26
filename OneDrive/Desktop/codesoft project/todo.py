import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []

        # UI Elements
        self.task_entry = tk.Entry(root, width=35)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10)

        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            self.tasks_listbox.insert(tk.END, f"{idx}. {task['task']} - [{status}]")

    def mark_complete(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark complete.")

    def delete_task(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
