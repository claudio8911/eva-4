import tkinter as tk
from tkinter import ttk

def crear_barra_herramientas(ventana, funciones):
    barra_herramientas = ttk.Frame(ventana)
    barra_herramientas.pack(side=tk.TOP, fill=tk.X)

    for texto, comando in funciones.items():
        boton = ttk.Button(barra_herramientas, text=texto, command=comando)
        boton.pack(side=tk.LEFT, padx=2, pady=2)

    return barra_herramientas

