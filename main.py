import tkinter as tk
from analizador_atleta import AnalizadorRendimiento
from componentes.componentes_interfaz import mostrar_mensaje_bienvenida

def main():
    root = tk.Tk()
    app = AnalizadorRendimiento(root)
    mostrar_mensaje_bienvenida()
    root.mainloop()

if __name__ == "__main__":
    main()

