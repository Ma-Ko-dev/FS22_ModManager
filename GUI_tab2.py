from tkinter import Tk, Label, OptionMenu, StringVar, Frame


class Tab2(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        label = Label(self, text="Fenstergröße:")
        label.grid(row=0, column=0, padx=10, pady=10)
        self.size_label = Label(self)
        self.size_label.grid(row=0, column=1, padx=10, pady=10)

        self.update_size_label()

        self.grid_columnconfigure(1, weight=1)
        self.master.bind("<Configure>", self.on_window_resize)

    def on_window_resize(self, event):
        self.update_size_label()

    def update_size_label(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        size_text = f"{width} x {height}"
        self.size_label.config(text=size_text)

