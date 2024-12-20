from pathlib import Path
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from agregarClientes import agregarClientes

def clientes():

    def cargar_clientes():
        """Cargar los clientes desde el archivo JSON"""
        try:
            with open("clientes.json", "r") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []

    def eliminar_cliente(cliente):
        """Eliminar un cliente de la lista"""
        # Cargar los clientes desde el archivo
        clientes = cargar_clientes()
        
        # Eliminar el cliente seleccionado
        clientes = [c for c in clientes if cliente not in c.values()]
        
        # Guardar los cambios en el archivo
        with open("clientes.json", "w") as archivo:
            json.dump(clientes, archivo, indent=4)
        
        # Actualizar la vista
        actualizar_lista()

    def mostrar_detalles(cliente):
        """Mostrar detalles del cliente (puede modificarse para editar)"""
        messagebox.showinfo("Detalles del Cliente", f"Detalles del cliente: {cliente}")

    def actualizar_lista():
        """Actualizar la lista de clientes en el Treeview"""
        # Limpiar el Treeview
        for item in treeview.get_children():
            treeview.delete(item)

        # Cargar clientes y agregar a la lista
        clientes = cargar_clientes()
        for cliente in clientes:
            nombre = list(cliente.keys())[0]
            # Agregar la fila con botones para "Eliminar" y para mostrar detalles
            treeview.insert("", "end", values=(nombre, "Eliminar"))

    def on_treeview_item_click(event):
        """Detectar clic en el Treeview y realizar acciones"""
        item = treeview.identify('item', event.x, event.y)
        column = treeview.identify_column(event.x)
        
        # Si el clic fue en la columna 'Acción' (índice 2)
        if column == "#2":
            cliente_nombre = treeview.item(item)['values'][0]
            eliminar_cliente(cliente_nombre)
        
        # Si el clic fue en la columna 'Nombre' (índice 1)
        elif column == "#1":
            cliente_nombre = treeview.item(item)['values'][0]
            mostrar_detalles(cliente_nombre)

    clientes_window = Tk()
    clientes_window.geometry("600x550")
    clientes_window.configure(bg="#FFFFFF")

    canvas = Canvas(
        clientes_window,
        bg="#FFFFFF",
        height=550,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    canvas.create_text(
        74.0,
        45.0,
        anchor="nw",
        text="Lista de clientes",
        fill="#000000",
        font=("Inter", 32 * -1)
    )

    # Crear el Treeview para mostrar la lista de clientes
    treeview = ttk.Treeview(clientes_window, columns=("Nombre", "Acción"), show="headings", height=15)
    treeview.place(x=22, y=100, width=550, height=300)

    # Definir las columnas
    treeview.heading("Nombre", text="Nombre")
    treeview.heading("Acción", text="Acción")

    # Crear un botón para actualizar la lista
    button_1 = Button(
        clientes_window,
        text="Actualizar lista",
        font=("Arial", 14),
        bg="#4CAF50",  # Color de fondo
        fg="white",  # Color del texto
        relief="flat",
        command=actualizar_lista
    )
    button_1.place(x=269.0, y=479.0, width=121.0, height=42.0)

    # Botón para abrir la ventana de agregar cliente
    button_2 = Button(
        clientes_window,
        text="Agregar cliente",
        font=("Arial", 14),
        bg="#008CBA",  # Color de fondo
        fg="white",  # Color del texto
        relief="flat",
        command=lambda: [clientes_window.destroy(), agregarClientes()]
    )
    button_2.place(x=22.0, y=479.0, width=156.39669799804688, height=42.0)

    # Cargar y mostrar los clientes al iniciar
    actualizar_lista()

    # Vincular el clic en el Treeview a la función de eliminar o mostrar detalles
    treeview.bind("<ButtonRelease-1>", on_treeview_item_click)

    clientes_window.resizable(False, False)
    clientes_window.mainloop()
