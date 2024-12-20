from pathlib import Path
from clientes import clientes
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button

def menu():
    menu = Tk()

    menu.geometry("400x550")
    menu.configure(bg = "#FFFFFF")

    canvas = Canvas(
        menu,
        bg = "#FFFFFF",
        height = 550,
        width = 400,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        16.0,
        0.0,
        anchor="nw",
        text="ROB\nER\nTO",
        fill="#000000",
        font=("Inter", 96 * -1)
    )

    canvas.create_text(
        240.0,
        178.0,
        anchor="nw",
        text="almacén",
        fill="#000000",
        font=("Inter", 32 * -1)
    )

    # Reemplazar botón con imagen por botón normal
    button_1 = Button(
        menu,
        text="Button 1",  # Cambia este texto por el que desees
        font=("Arial", 14),
        bg="#4CAF50",  # Color de fondo
        fg="white",  # Color del texto
        relief="flat",
        command=lambda: print("button_1 clicked")
    )
    button_1.place(
        x=95.0,
        y=440.0,
        width=209.0,
        height=42.0
    )

    # Reemplazar el segundo botón con imagen por otro botón normal
    button_2 = Button(
        menu,
        text="Clientes",  # Cambia este texto por el que desees
        font=("Arial", 14),
        bg="#008CBA",  # Color de fondo
        fg="white",  # Color del texto
        relief="flat",
        command=lambda: [menu.destroy(), clientes()]
    )
    button_2.place(
        x=95.0,
        y=380.0,
        width=209.0,
        height=42.0
    )

    menu.resizable(False, False)
    menu.mainloop()
