def calcular_parametros(tipo_deporte, nivel_entrenamiento, objetivo):
    # Definir parámetros base
    tasa_exp_base = 0.01
    factor_log_base = 0.2
    factor_poli_base = 0.001
    
    # Ajustar según el tipo de deporte
    if tipo_deporte == "Carrera" or tipo_deporte == "Natación":
        tasa_exp_base *= 0.9
        factor_log_base *= 1.1
        factor_poli_base *= 1.2
    elif tipo_deporte == "Ciclismo":
        tasa_exp_base *= 1.1
        factor_log_base *= 0.9
        factor_poli_base *= 0.8
    elif tipo_deporte == "Levantamiento de Pesas":
        tasa_exp_base *= 1.2
        factor_log_base *= 0.8
        factor_poli_base *= 1.5
    
    # Ajustar según el nivel de entrenamiento
    if nivel_entrenamiento == "Principiante":
        tasa_exp_base *= 1.2
        factor_log_base *= 1.3
        factor_poli_base *= 0.8
    elif nivel_entrenamiento == "Intermedio":
        tasa_exp_base *= 1.0
        factor_log_base *= 1.0
        factor_poli_base *= 1.0
    elif nivel_entrenamiento == "Avanzado":
        tasa_exp_base *= 0.8
        factor_log_base *= 0.7
        factor_poli_base *= 1.2
    
    # Ajustar según el objetivo
    if objetivo == "Mejora Gradual":
        tasa_exp_base *= 1.0
        factor_log_base *= 1.0
        factor_poli_base *= 1.0
    elif objetivo == "Competición":
        tasa_exp_base *= 1.2
        factor_log_base *= 0.8
        factor_poli_base *= 1.3
    elif objetivo == "Mantenimiento":
        tasa_exp_base *= 0.8
        factor_log_base *= 1.2
        factor_poli_base *= 0.7
    
    return tasa_exp_base, factor_log_base, factor_poli_base

