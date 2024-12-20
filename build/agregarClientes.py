from pathlib import Path
import json
from tkinter import Tk, Canvas, Entry, Button


def agregarClientes():
    
    def guardarCliente():
        clientes_data = []
        with open("clientes.json", "r") as archivo: 
            clientes_data = json.load(archivo)
        
        item = {}    
        item["nombre"] = entry_1.get()
        item["ci"] = entry_2.get()
        clientes_data.append(item)
        print(clientes_data)
        
        with open("clientes.json", "w") as archivo:
            json.dump(clientes_data, archivo, indent=4)
        
        agregarCliente.destroy()

    def abrirClientes():
        from  clientes import clientes
        clientes()  # Llama a la función 'clientes' para abrir la ventana

    # Ventana de agregar cliente
    agregarCliente = Tk()
    agregarCliente.geometry("400x550")
    agregarCliente.configure(bg = "#FFFFFF")

    canvas = Canvas(
        agregarCliente,
        bg = "#FFFFFF",
        height = 550,
        width = 400,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)
    
    canvas.create_text(
        86.0,
        42.0,
        anchor="nw",
        text="Agregar cliente",
        fill="#000000",
        font=("Inter", 32 * -1)
    )

    # Botón para abrir la ventana de clientes
    button_1 = Button(
        agregarCliente,
        text="Abrir Clientes",
        font=("Arial", 14),
        bg="#4CAF50",  # Color de fondo
        fg="white",  # Color del texto
        relief="flat",
        command=lambda: print("button_1 clicked")  # Cambiar el comando según sea necesario
    )
    button_1.place(x=171.0, y=412.0, width=155.0, height=42.0)

    # Botón para guardar el cliente y abrir la ventana de clientes
    button_2 = Button(
        agregarCliente,
        text="Guardar y Ver Clientes",
        font=("Arial", 14),
        bg="#008CBA",  # Color de fondo
        fg="white",  # Color del texto
        relief="flat",
        command=lambda: [guardarCliente(), abrirClientes()]
    )
    button_2.place(x=74.0, y=344.0, width=143.0, height=42.0)

    # Campo de entrada para el nombre
    entry_1 = Entry(
        agregarCliente,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Arial", 14)
    )
    entry_1.place(x=74.0, y=187.0, width=252.0, height=22.0)

    # Campo de entrada para la cédula
    entry_2 = Entry(
        agregarCliente,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Arial", 14)
    )
    entry_2.place(x=74.0, y=251.0, width=252.0, height=22.0)

    # Etiquetas de texto para los campos de entrada
    canvas.create_text(76.0, 161.0, anchor="nw", text="Nombre", fill="#000000", font=("Inter", 20 * -1))
    canvas.create_text(76.0, 225.0, anchor="nw", text="Cédula", fill="#000000", font=("Inter", 20 * -1))

    agregarCliente.resizable(False, False)
    agregarCliente.mainloop()
