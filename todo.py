import tkinter as tk
        #create a class
class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do List App')
        self.root.geometry('800x600+200+100')

        # Configure the background color
        self.root.configure(bg='light gray')

        # Create a custom font
        custom_font = ('Aileron', 18, 'bold')   

        # Create labels with custom styling
        self.label = tk.Label(self.root, text='To-Do List', font=custom_font, bd=10, bg='light gray', fg='black')
        self.label.pack(side='top', fill=tk.BOTH)

        self.label2 = tk.Label(self.root, text='Add Task', font=custom_font, bd=5, bg='gray', fg='black')
        self.label2.place(x=50, y=50)

        self.label3 = tk.Label(self.root, text='Tasks', font=custom_font, bd=5, bg='gray', fg='black')
        self.label3.place(x=400, y=70)

        # Create a Listbox with a custom font
        self.main_text = tk.Listbox(self.root, height=10, bd=5, width=30, font=custom_font)
        self.main_text.place(x=400, y=100)

        # Create a Text widget with a custom font
        self.text = tk.Text(self.root, bd=5, height=2, width=20, font=custom_font)
        self.text.place(x=50, y=100)

        # Configure buttons with custom styling
        self.button = tk.Button(self.root, text="Add Task", font=custom_font, bd=5, bg='green', fg='white', command=self.add)
        self.button.place(x=50, y=250)

        self.button2 = tk.Button(self.root, text="Delete Task", font=custom_font, bd=5, bg='red', fg='white', command=self.delete)
        self.button2.place(x=200, y=250)

    def add(self):
        content = self.text.get(1.0, tk.END)
        self.main_text.insert(tk.END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
        self.text.delete(1.0, tk.END)

    def delete(self):
        delete = self.main_text.curselection()
        self.main_text.delete(delete)

def main():
    root = tk.Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()   
