import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

def exit_editor():
    root.quit()

root = tk.Tk()
root.title("SB text editor")
root.geometry("400x400")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)

file_menu.add_command(label="New", command=open_file)
file_menu.add_command(label="Save", command=save_file)

file_menu.add_command(label="Save as", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

text = tk.Text(root, wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH)

root.mainloop()
