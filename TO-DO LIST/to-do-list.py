import tkinter as tk
from tkinter import messagebox
class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")

        self.tasks = []

        # Create UI elements
        self.task_label = tk.Label(root, text="Enter a task:", font=("Arial", 14))
        self.task_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task, font=("Arial", 12))
        self.add_button.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", width=20, command=self.delete_task, font=("Arial", 12))
        self.delete_button.pack(pady=10)

        self.clear_button = tk.Button(root, text="Clear All Tasks", width=20, command=self.clear_tasks, font=("Arial", 12))
        self.clear_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_tasks(self):
        self.tasks.clear()
        self.task_listbox.delete(0, tk.END)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
