import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import namedtuple

# Importaciones desde los módulos del proyecto
from componentes.componentes_interfaz import (
    crear_marco_entrada,
    crear_marco_grafico,
    crear_marco_recomendacion,
    mostrar_error,
    mostrar_mensaje_bienvenida
)
from utilidades.funciones_matematicas import calcular_parametros
from utilidades.utilidades_grafico import generar_grafico
from utilidades.recomendaciones import generar_recomendaciones

class AnalizadorRendimiento:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Rendimiento Deportivo")
        self.root.geometry("800x600")
        
        self.datos_grafico = None
        self.crear_interfaz()
        
    def crear_interfaz(self):
        marco_principal = ttk.Frame(self.root, padding="10")
        marco_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Crear componentes usando las funciones del módulo componentes_interfaz
        entradas = crear_marco_entrada(marco_principal, self.validar_flotante, self.validar_entero)
        self.entrada_rendimiento, self.entrada_periodo, self.var_tipo_deporte, \
        self.var_nivel_entrenamiento, self.var_objetivo = entradas
        
        # Botón de análisis
        ttk.Button(marco_principal, text="Analizar Rendimiento", 
                  command=self.analizar_rendimiento).grid(row=2, column=0, pady=10)
        
        # Marco de gráfico
        self.marco_grafico = crear_marco_grafico(marco_principal)
        
        # Marco de recomendaciones
        self.texto_recomendacion = crear_marco_recomendacion(marco_principal)
        
        # Botón para exportar datos
        ttk.Button(marco_principal, text="Exportar Datos para GeoGebra", 
                  command=self.exportar_datos_geogebra).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Configurar el peso de las columnas y filas
        marco_principal.columnconfigure(1, weight=1)
        marco_principal.rowconfigure(0, weight=1)
        marco_principal.rowconfigure(1, weight=1)
        
    def validar_flotante(self, valor):
        if valor == "":
            return True
        try:
            float(valor)
            return True
        except ValueError:
            return False
        
    def validar_entero(self, valor):
        if valor == "":
            return True
        try:
            int(valor)
            return True
        except ValueError:
            return False
        
    def analizar_rendimiento(self):
        if not self.validar_entradas():
            return
        
        rendimiento_actual = float(self.entrada_rendimiento.get())
        semanas = int(self.entrada_periodo.get())
        tipo_deporte = self.var_tipo_deporte.get()
        nivel_entrenamiento = self.var_nivel_entrenamiento.get()
        objetivo = self.var_objetivo.get()
        
        dias = np.arange(0, semanas * 7 + 1)
        
        tasa_exp, factor_log, factor_poli = calcular_parametros(tipo_deporte, nivel_entrenamiento, objetivo)
        
        es_carrera_o_natacion = "Carrera" in tipo_deporte or "Natación" in tipo_deporte
        
        exponencial = rendimiento_actual * np.exp((-tasa_exp if es_carrera_o_natacion else tasa_exp) * dias / 7)
        logaritmica = rendimiento_actual * (1 - factor_log * np.log(dias / 7 + 1) / np.log(semanas + 1)) if es_carrera_o_natacion else rendimiento_actual * (1 + factor_log * np.log(dias / 7 + 1) / np.log(semanas + 1))
        polinomica = rendimiento_actual * (1 - factor_poli * (dias / 7)**2 + 0.1 * factor_poli * (dias / 7)) if es_carrera_o_natacion else rendimiento_actual * (1 + factor_poli * (dias / 7)**2 - 0.1 * factor_poli * (dias / 7))
        
        DatosGrafico = namedtuple('DatosGrafico', ['dias', 'exponencial', 'logaritmica', 'polinomica', 'tipo_deporte'])
        self.datos_grafico = DatosGrafico(dias, exponencial, logaritmica, polinomica, tipo_deporte)
        
        generar_grafico(self.marco_grafico, self.datos_grafico)
        recomendaciones = generar_recomendaciones(tipo_deporte, nivel_entrenamiento, objetivo)
        self.texto_recomendacion.delete('1.0', tk.END)
        self.texto_recomendacion.insert(tk.END, recomendaciones)
        
    def validar_entradas(self):
        try:
            rendimiento_actual = float(self.entrada_rendimiento.get())
            semanas = int(self.entrada_periodo.get())
            
            if rendimiento_actual <= 0:
                mostrar_error("El rendimiento actual debe ser un número positivo.")
                return False
            
            if semanas <= 0 or semanas > 52:
                mostrar_error("El período debe estar entre 1 y 52 semanas.")
                return False
            
            if not self.var_tipo_deporte.get():
                mostrar_error("Por favor, seleccione un deporte.")
                return False
            
            if not self.var_nivel_entrenamiento.get():
                mostrar_error("Por favor, seleccione un nivel de entrenamiento.")
                return False
            
            if not self.var_objetivo.get():
                mostrar_error("Por favor, seleccione un objetivo.")
                return False
            
            return True
        except ValueError:
            mostrar_error("Por favor, complete todos los campos correctamente.")
            return False
    
    def exportar_datos_geogebra(self):
        if not self.datos_grafico:
            mostrar_error("Primero debes generar un análisis de rendimiento.")
            return

        try:
            # Tomar menos puntos para el archivo de GeoGebra
            indices = np.arange(0, len(self.datos_grafico.dias), 7)  # Un punto por semana
            
            # Generar tablas de puntos
            tabla_exponencial = np.column_stack((
                self.datos_grafico.dias[indices],
                self.datos_grafico.exponencial[indices]
            ))
            tabla_logaritmica = np.column_stack((
                self.datos_grafico.dias[indices],
                self.datos_grafico.logaritmica[indices]
            ))
            tabla_polinomica = np.column_stack((
                self.datos_grafico.dias[indices],
                self.datos_grafico.polinomica[indices]
            ))

            # Preparar funciones para GeoGebra
            valor_inicial = float(self.datos_grafico.exponencial[0])
            dias_max = float(self.datos_grafico.dias[-1])
            tasa_exp, factor_log, factor_poli = calcular_parametros(
                self.var_tipo_deporte.get(),
                self.var_nivel_entrenamiento.get(),
                self.var_objetivo.get()
            )

            es_carrera_o_natacion = "Carrera" in self.datos_grafico.tipo_deporte or "Natación" in self.datos_grafico.tipo_deporte
            
            # Formatear números con punto decimal para GeoGebra
            tasa_exp_str = "{:.6f}".format(tasa_exp)
            factor_log_str = "{:.6f}".format(factor_log)
            factor_poli_str = "{:.6f}".format(factor_poli)
            valor_inicial_str = "{:.2f}".format(valor_inicial)
            
            # Construir funciones con formato correcto para GeoGebra
            funciones = [
                f"f(x) = {valor_inicial_str} * e^({'-' if es_carrera_o_natacion else ''}{tasa_exp_str} * x / 7)",
                f"g(x) = {valor_inicial_str} * (1 {'-' if es_carrera_o_natacion else '+'} {factor_log_str} * log(x / 7 + 1) / log({dias_max / 7 + 1:.4f}))",
                f"h(x) = {valor_inicial_str} * (1 {'-' if es_carrera_o_natacion else '+'} {factor_poli_str} * (x/7)^2 {'+' if es_carrera_o_natacion else '-'} {0.1 * factor_poli:.6f} * (x/7))"
            ]

            # Guardar datos en un archivo
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")],
                title="Guardar datos para GeoGebra"
            )
        
            if filename:
                with open(filename, 'w', newline='', encoding='utf-8') as file:
                    file.write("INSTRUCCIONES PARA GEOGEBRA\n")
                    file.write("=========================\n\n")
                    
                    file.write("1. COPIAR PUNTOS\n")
                    file.write("---------------\n")
                    file.write("a) Abre GeoGebra y muestra la Hoja de Cálculo (Ver > Hoja de Cálculo)\n")
                    file.write("b) Copia y pega cada tabla de puntos en columnas separadas\n")
                    file.write("c) Selecciona los datos y crea un gráfico de dispersión\n\n")
                    
                    file.write("2. COPIAR FUNCIONES\n")
                    file.write("------------------\n")
                    file.write("a) Copia cada función en la barra de entrada de GeoGebra\n")
                    file.write("b) Presiona Enter después de cada función\n\n")
                    
                    file.write("DATOS PARA COPIAR:\n")
                    file.write("=================\n\n")
                    
                    # Escribir tablas de puntos
                    file.write("--- FUNCIÓN EXPONENCIAL ---\n")
                    file.write("Días,Rendimiento\n")
                    np.savetxt(file, tabla_exponencial, delimiter=',', fmt='%.6f')
                    file.write("\n")
                    
                    file.write("--- FUNCIÓN LOGARÍTMICA ---\n")
                    file.write("Días,Rendimiento\n")
                    np.savetxt(file, tabla_logaritmica, delimiter=',', fmt='%.6f')
                    file.write("\n")
                    
                    file.write("--- FUNCIÓN POLINÓMICA ---\n")
                    file.write("Días,Rendimiento\n")
                    np.savetxt(file, tabla_polinomica, delimiter=',', fmt='%.6f')
                    file.write("\n")
                    
                    # Escribir funciones
                    file.write("FUNCIONES:\n")
                    file.write("---------\n")
                    for i, funcion in enumerate(funciones, 1):
                        file.write(f"{i}. {funcion}\n")
                    
                    file.write(f"\nDominio: 0 ≤ x ≤ {dias_max}\n")

                mostrar_mensaje_bienvenida("Exportación exitosa", 
                    "Los datos han sido exportados correctamente.\n\n" +
                    "El archivo contiene:\n" +
                    "1. Instrucciones paso a paso\n" +
                    "2. Tablas de puntos listas para copiar\n" +
                    "3. Funciones en formato GeoGebra\n\n" +
                    "Sigue las instrucciones en el archivo para visualizar los datos."
                )

        except Exception as e:
            self.manejar_error(e)

    def manejar_error(self, error):
        if isinstance(error, UnicodeEncodeError):
            mensaje = ("Error de codificación al guardar el archivo.\n"
                      "Por favor, utilice un nombre de archivo sin caracteres especiales.")
        elif isinstance(error, PermissionError):
            mensaje = ("Error de permisos al guardar el archivo.\n"
                      "Asegúrese de tener permisos de escritura en la carpeta seleccionada.")
        elif isinstance(error, OSError):
            mensaje = ("Error al guardar el archivo.\n"
                      "Verifique que la ruta sea válida y tenga permisos de escritura.")
        else:
            mensaje = f"Ha ocurrido un error: {type(error).__name__}\n{str(error)}"
        
        mostrar_error(mensaje)

