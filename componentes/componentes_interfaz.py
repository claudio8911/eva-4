import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

def crear_marco_entrada(padre, validar_flotante, validar_entero):
    marco_entrada = ttk.LabelFrame(
        padre,
        text="Datos del Atleta",
        padding="10"
    )
    marco_entrada.grid(
        row=0,
        column=0,
        sticky=(tk.W, tk.E, tk.N, tk.S),
        padx=5,
        pady=5
    )

    # Deporte
    ttk.Label(marco_entrada, text="Deporte:").grid(row=0, column=0, sticky=tk.W)
    tipo_deporte = tk.StringVar()
    combo_deporte = ttk.Combobox(
        marco_entrada,
        textvariable=tipo_deporte,
        state="readonly"
    )
    combo_deporte['values'] = (
        'Natación (400m)', 
        'Natación (100m)', 
        'Carrera (5km)', 
        'Carrera (10km)',
        'Press de Banca',
        'Peso Muerto',
        'Sentadillas',
        'Clean & Jerk',
        'Snatch'
    )
    combo_deporte.grid(row=0, column=1, sticky=(tk.W, tk.E))
    combo_deporte.bind('<<ComboboxSelected>>', lambda e: actualizar_etiqueta_rendimiento(e, tipo_deporte, etiqueta_rendimiento))

    # Rendimiento Actual (dinámico según el deporte)
    etiqueta_rendimiento = ttk.Label(marco_entrada, text="Tiempo Actual (minutos):")
    etiqueta_rendimiento.grid(row=1, column=0, sticky=tk.W)
    entrada_rendimiento = ttk.Entry(
        marco_entrada,
        validate="key",
        validatecommand=(padre.register(validar_flotante), '%P')
    )
    entrada_rendimiento.grid(row=1, column=1, sticky=(tk.W, tk.E))

    # Período
    ttk.Label(marco_entrada, text="Período (semanas):").grid(row=2, column=0, sticky=tk.W)
    entrada_periodo = ttk.Entry(
        marco_entrada,
        validate="key",
        validatecommand=(padre.register(validar_entero), '%P')
    )
    entrada_periodo.grid(row=2, column=1, sticky=(tk.W, tk.E))

    # Nivel
    ttk.Label(marco_entrada, text="Nivel:").grid(row=3, column=0, sticky=tk.W)
    nivel_entrenamiento = tk.StringVar()
    combo_nivel = ttk.Combobox(
        marco_entrada,
        textvariable=nivel_entrenamiento,
        state="readonly"
    )
    combo_nivel['values'] = (
        'Principiante (1-2 sesiones/sem)',
        'Intermedio (3-4 sesiones/sem)',
        'Avanzado (4-6 sesiones/sem)'
    )
    combo_nivel.grid(row=3, column=1, sticky=(tk.W, tk.E))

    # Objetivo
    ttk.Label(marco_entrada, text="Objetivo:").grid(row=4, column=0, sticky=tk.W)
    objetivo = tk.StringVar()
    combo_objetivo = ttk.Combobox(
        marco_entrada,
        textvariable=objetivo,
        state="readonly"
    )
    combo_objetivo['values'] = ('Mejora Gradual', 'Competición', 'Mantenimiento')
    combo_objetivo.grid(row=4, column=1, sticky=(tk.W, tk.E))
    objetivo.set("Mejora Gradual")

    return entrada_rendimiento, entrada_periodo, tipo_deporte, nivel_entrenamiento, objetivo

def crear_marco_grafico(padre):
    marco_grafico = ttk.LabelFrame(
        padre,
        text="Gráfico de Rendimiento",
        padding="10"
    )
    marco_grafico.grid(
        row=0,
        column=1,
        rowspan=2,
        sticky=(tk.W, tk.E, tk.N, tk.S),
        padx=5,
        pady=5
    )
    return marco_grafico

def crear_marco_recomendacion(padre):
    marco_rec = ttk.LabelFrame(
        padre,
        text="Análisis y Recomendaciones",
        padding="10"
    )
    marco_rec.grid(
        row=1,
        column=0,
        sticky=(tk.W, tk.E, tk.N, tk.S),
        padx=5,
        pady=5
    )

    texto_recomendacion = scrolledtext.ScrolledText(
        marco_rec,
        wrap=tk.WORD,
        width=40,
        height=10
    )
    texto_recomendacion.pack(expand=True, fill='both')
    return texto_recomendacion

def mostrar_error(mensaje):
    messagebox.showerror("Error", mensaje)

def mostrar_mensaje_bienvenida(titulo="Bienvenida", mensaje=None):
    if mensaje is None:
        mensaje = """
¡Bienvenido al Analizador de Rendimiento Deportivo!

Este programa utiliza modelos matemáticos (exponencial, logarítmico y polinómico) para:
1. Analizar tu progreso deportivo
2. Visualizar diferentes fases de entrenamiento
3. Generar recomendaciones personalizadas
4. Exportar datos para análisis en GeoGebra

Para comenzar:
1. Selecciona tu deporte
2. Ingresa tu tiempo actual
3. Define el período de entrenamiento
4. Elige tu nivel y objetivo
5. Haz clic en "Analizar Rendimiento"
"""
    messagebox.showinfo(titulo, mensaje)

def actualizar_etiqueta_rendimiento(event, tipo_deporte, etiqueta):
    if any(deporte in tipo_deporte.get() for deporte in ['Natación', 'Carrera']):
        etiqueta.config(text="Tiempo Actual (minutos):")
    else:
        etiqueta.config(text="Peso Actual (kg):")

