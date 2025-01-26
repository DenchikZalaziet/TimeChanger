import tkinter as tk
from main import setup


class App(tk.Tk):
    def __init__(self):
        super().__init__()


app = App()
app.title("Custom Time Converter")
setup(app)
app.mainloop()
