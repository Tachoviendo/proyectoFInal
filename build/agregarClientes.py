from pathlib import Path
import json
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def agregarClientes():
    
    def guardarCliente():
        clientes_data = []
        with open("clientes.json", "r") as archivo: 
            clientes_data = json.load(archivo)
        
        item = {}    
        item[entry_1.get()] = entry_2.get()  
        clientes_data.append(item)
        print(clientes_data)
        
        
        with open("clientes.json", "w") as archivo:
            json.dump(clientes_data, archivo, indent=4)
        
        
        agregarCliente.destroy()

        
        
    
    def abrirClientes():
        from  clientes import clientes
        clientes()# Llama a la función 'clientes' para abrir la ventana

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Ignacio\Documents\proyectoFInal\build\assets\frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

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

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(x=171.0, y=412.0, width=155.0, height=42.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [guardarCliente(), abrirClientes()],
        relief="flat"
    )
    button_2.place(x=74.0, y=344.0, width=143.0, height=42.0)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(200.0, 199.0, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_1.place(x=74.0, y=187.0, width=252.0, height=22.0)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(200.0, 263.0, image=entry_image_2)
    entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_2.place(x=74.0, y=251.0, width=252.0, height=22.0)

    canvas.create_text(76.0, 161.0, anchor="nw", text="Nombre", fill="#000000", font=("Inter", 20 * -1))
    canvas.create_text(76.0, 225.0, anchor="nw", text="Cédula", fill="#000000", font=("Inter", 20 * -1))

    agregarCliente.resizable(False, False)
    agregarCliente.mainloop()
