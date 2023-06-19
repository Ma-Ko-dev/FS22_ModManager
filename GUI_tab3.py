import tkinter as tk
from tkinter import ttk


class Tab3(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ttk.Label(self, text="Label im Tab 3")
        self.label.pack()
