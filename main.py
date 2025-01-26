from tkinter import *
from tkinter import font, ttk
import datetime


def number_to_base(n, b) -> list:
    if n == 0:
        return [0]
    digits = []
    if b > 1:
        while n:
            digits.append(int(n % b))
            n //= b
    else:
        digits = [0] * n
    return digits[::-1]


def button_press() -> None:
    current = datetime.datetime.now()
    text = entry_box.get()
    if len(text) == 0:
        text = '-'

    text = list(map(str, text.split()))
    new.change(text)
    alphabet['text'] = "Символы: " + new.get_base() + " | " + new.get_list()
    time["text"] = new.convert(current.hour) + " : " + new.convert(current.minute)
    letter_weight["text"] = inf_weight(new.get_base())
    time_normalised["text"] = str(current.hour) + " : " + str(current.minute)


def inf_weight(num) -> str:
    i = 1
    while 2 ** i < int(num):
        i += 1
    arr = str(i) + " бит"
    if (2 <= i % 10 <= 4) and (i < 10 or i > 20):
        arr += 'a'
    return arr


class NewTime:
    def __init__(self) -> None:
        self.coding_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.base = len(self.coding_list)

    def change(self, ch) -> None:
        self.coding_list = ch
        self.base = len(self.coding_list)

    def get_list(self) -> str:
        arr = ""
        for i in self.coding_list:
            arr = arr + i + ' '
        arr = arr[:len(arr) - 1]
        return arr

    def get_base(self) -> str:
        return str(self.base)

    def convert(self, num) -> str:
        res = ""
        arr = number_to_base(num, self.base)
        for i in arr:
            res += self.coding_list[i]
        return res


def setup(app):
    global new, time, time_normalised, alphabet, entry_box, letter_weight, font_g, font_italic, filepath
    font_g = font.Font(weight='bold')
    font_italic = font.Font(slant='italic')
    new = NewTime()
    current = datetime.datetime.now()

    frame_time = ttk.Frame(relief=RAISED, padding=[8, 10], cursor="dot")
    frame_main = ttk.Frame(padding=7)

    time = Label(master=frame_time, text=new.convert(current.hour) + " : " + new.convert(current.minute), font=font_g)
    time_normalised = Label(master=frame_time, text=str(current.hour) + " : " + str(current.minute))
    alphabet = Label(master=frame_main, text="Символы: " + new.get_base() + " | " + new.get_list())
    letter_weight = Label(master=frame_main, text=inf_weight(new.get_base()))
    entry_box = Entry(master=frame_main)
    entry_box.insert(0, new.get_list())
    button = Button(master=frame_main, text="Change", command=button_press)

    time.pack()
    time_normalised.pack()
    alphabet.pack()
    letter_weight.pack()
    entry_box.pack()
    button.pack(pady=5)

    frame_time.pack(pady=10, padx=10)
    frame_main.pack(pady=10, padx=10)
