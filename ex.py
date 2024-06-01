import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("450x700+400+100")
root.resizable(False, False)

task_list = []

def openTaskFile():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task.strip() != '':
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        with open("tasklist.txt", 'w') as file:
            file.close()

def add_task():
    task_content = task_entry.get()
    if task_content:
        task_list.append(task_content)
        listbox.insert(END, task_content)
        task_entry.delete(0, END)
        save_tasks()

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        task_list.pop(selected_task_index)
        save_tasks()
    except IndexError:
        pass  # Do nothing if no task is selected

def save_tasks():
    with open("tasklist.txt", "w") as taskfile:
        for task in task_list:
            taskfile.write(task + "\n")


Image_icon = PhotoImage(file="ICON/task.png")
root.iconphoto(False, Image_icon)


TopImage = PhotoImage(file="ICON/topbar.png")
Label(root, image=TopImage).pack()
dockImage = PhotoImage(file="ICON/dock.png")
Label(root, image=dockImage, bg="#FFDDC1").place(x=30, y=25)
heading = Label(root, text="ALL TASKS", font="Arial 24 bold", fg="white", bg="#FF6F61")
heading.place(x=130, y=20)


frame = Frame(root, width=450, height=50, bg="white")
frame.place(x=0, y=200)
task = StringVar()
task_entry = Entry(frame, width=22, font="Arial 18", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()
button = Button(frame, text="ADD", font="Arial 18 bold", width=6, bg="#FF6F61", fg="#fff", bd=0, command=add_task)
button.place(x=350, y=0)


frame1 = Frame(root, bd=3, width=450, height=400, bg="#B0E0E6")
frame1.pack(pady=(160, 0))
listbox = Listbox(frame1, font=('Arial', 14), width=40, height=16, bg="#B0E0E6", fg="black", cursor="hand2", selectbackground="#FF6F61")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()


Delete_icon = PhotoImage(file="ICON/delete.png")
Button(root, image=Delete_icon, bd=0, command=delete_task).pack(side=BOTTOM, pady=20)

root.mainloop()
