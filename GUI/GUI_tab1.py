import tkinter as tk
from tkinter import ttk


class Tab1(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

        heading_label = tk.Label(self, text="Modmanager", font=("Helvetica", 16, "bold"))
        heading_label.grid(row=0, column=0, padx=10, pady=10, sticky="n", columnspan=2)

        savegame_label = tk.Label(self, text="Savegame")
        savegame_label.grid(row=1, column=0, padx=25, pady=10, sticky="w")

        savegame_options = ["Savegame1", "Savegame2", "Savegame3", "Savegame4"]
        savegame_dropdown = ttk.Combobox(self, values=savegame_options)
        savegame_dropdown.grid(row=1, column=1, padx=25, pady=10, sticky="e")
