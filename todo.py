import tkinter as tk
from tkinter import ttk

# Linked list implementation
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

head = None
size = 0

def add_task(task):
    global head, size
    new_node = Node(task)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
    size += 1

def remove_task(task):
    global head, size
    if head is None:
        return
    if head.task == task:
        head = head.next
        size -= 1
        return
    current = head
    while current.next:
        if current.next.task == task:
            current.next = current.next.next
            size -= 1
            return
        current = current.next

def print_list():
    global head
    current = head
    print("To-Do List:")
    while current:
        print("- " + current.task)
        current = current.next
    print(f"Total tasks: {size}")

# GUI implementation
def add_task_gui():
    task = task_input.get().strip()
    if task:
        add_task(task)
        task_input.delete(0, tk.END)
        refresh_list()

def remove_task_gui():
    selected = task_list.selection()
    if selected:
        task = task_list.item(selected)['values'][0]
        remove_task(task)
        refresh_list()

def refresh_list():
    task_list.delete(*task_list.get_children())
    current = head
    while current:
        task_list.insert("", "end", text="", values=(current.task,))
        current = current.next

root = tk.Tk()
root.title("To-Do List")

task_input = ttk.Entry(root)
task_input.grid(row=0, column=0, padx=5, pady=5)

add_button = ttk.Button(root, text="Add Task", command=add_task_gui)
add_button.grid(row=0, column=1, padx=5, pady=5)

remove_button = ttk.Button(root, text="Remove Task", command=remove_task_gui)
remove_button.grid(row=0, column=2, padx=5, pady=5)

task_list = ttk.Treeview(root)
task_list['columns'] = ('Task',)
task_list.column("#0", width=100)
task_list.column("Task", width=200)
task_list.heading("#0", text="")
task_list.heading("Task", text="Task")
task_list.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

refresh_list()

root.mainloop()