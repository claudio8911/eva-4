import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from matplotlib.backend_bases import key_press_handler

def generar_grafico(marco_grafico, datos_grafico):
    # Limpiar el marco
    for widget in marco_grafico.winfo_children():
        widget.destroy()

    # Crear figura con DPI más bajo para mejor rendimiento
    fig, ax = plt.subplots(figsize=(6, 4), dpi=80)

    # Configurar el estilo para mejor rendimiento
    plt.style.use('fast')

    # Reducir el número de puntos para mejor rendimiento
    paso = max(1, len(datos_grafico.dias) // 100)  # Limitar a ~100 puntos
    dias = datos_grafico.dias[::paso]
    
    # Plotear con menos puntos pero líneas suaves
    ax.plot(dias, datos_grafico.exponencial[::paso], label='Fase de Adaptación', linewidth=1.5)
    ax.plot(dias, datos_grafico.logaritmica[::paso], label='Fase de Mejora', linewidth=1.5)
    ax.plot(dias, datos_grafico.polinomica[::paso], label='Fase de Especialización', linewidth=1.5)
    
    # Configurar etiquetas y título
    ax.set_xlabel('Días de Entrenamiento')
    ax.set_ylabel('Rendimiento')
    ax.set_title('Proyección de Rendimiento durante el Ciclo de Entrenamiento')
    ax.legend()
    
    # Ajustar márgenes para mejor visualización
    plt.tight_layout()
    
    # Crear el canvas con el backend TkAgg
    canvas = FigureCanvasTkAgg(fig, master=marco_grafico)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    
    # Añadir la barra de herramientas de navegación
    toolbar_frame = tk.Frame(marco_grafico)
    toolbar_frame.pack(fill=tk.X)
    toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
    toolbar.update()
    
    # Configurar eventos de zoom y pan
    def on_key_press(event):
        key_press_handler(event, canvas, toolbar)
    
    canvas.mpl_connect('key_press_event', on_key_press)
    
    # Habilitar el modo pan por defecto
    toolbar.pan()
    
    return canvas

