def generar_recomendaciones(tipo_deporte, nivel_entrenamiento, objetivo):
    recomendaciones = "Explicación de las Fases de Entrenamiento:\n"
    recomendaciones += "1. Fase de Adaptación: Período inicial donde tu cuerpo se ajusta a nuevas rutinas.\n"
    recomendaciones += "2. Fase de Mejora: Etapa de progreso constante donde ves ganancias significativas.\n"
    recomendaciones += "3. Fase de Especialización: Período avanzado con ajustes específicos y posibles fluctuaciones.\n\n"
    
    if tipo_deporte == "Natación":
        recomendaciones += "Recomendaciones para Natación:\n"
        recomendaciones += "1. Fase de Adaptación:\n"
        recomendaciones += "   - Enfócate en la técnica de nado y respiración\n"
        recomendaciones += "   - Aumenta gradualmente la distancia y duración de las sesiones\n"
        recomendaciones += "   - Trabaja en la eficiencia de tu brazada\n\n"
        
        recomendaciones += "2. Fase de Mejora:\n"
        recomendaciones += "   - Incorpora entrenamientos de intervalos\n"
        recomendaciones += "   - Mejora tu resistencia con series más largas\n"
        recomendaciones += "   - Trabaja en la velocidad con sprints cortos\n\n"
        
        recomendaciones += "3. Fase de Especialización:\n"
        recomendaciones += "   - Enfócate en tu estilo de nado principal\n"
        recomendaciones += "   - Implementa entrenamientos específicos para competencias\n"
        recomendaciones += "   - Trabaja en las salidas, vueltas y llegadas\n\n"
    elif tipo_deporte == "Carrera":
        recomendaciones += "Recomendaciones para Carrera:\n"
        recomendaciones += "1. Fase de Adaptación:\n"
        recomendaciones += "   - Establece una base aeróbica con carreras lentas y largas\n"
        recomendaciones += "   - Mejora tu técnica de carrera\n"
        recomendaciones += "   - Incorpora ejercicios de fuerza para prevenir lesiones\n\n"
        
        recomendaciones += "2. Fase de Mejora:\n"
        recomendaciones += "   - Aumenta gradualmente la distancia de tus carreras largas\n"
        recomendaciones += "   - Incorpora entrenamientos de ritmo y tempo\n"
        recomendaciones += "   - Trabaja en colinas para mejorar la fuerza\n\n"
        
        recomendaciones += "3. Fase de Especialización:\n"
        recomendaciones += "   - Realiza entrenamientos específicos para tu distancia objetivo\n"
        recomendaciones += "   - Implementa sesiones de intervalos de alta intensidad\n"
        recomendaciones += "   - Practica estrategias de carrera y ritmo\n\n"
    elif tipo_deporte == "Ciclismo":
        recomendaciones += "Recomendaciones para Ciclismo:\n"
        recomendaciones += "1. Fase de Adaptación:\n"
        recomendaciones += "   - Enfócate en desarrollar una cadencia cómoda\n"
        recomendaciones += "   - Mejora tu resistencia con salidas largas a baja intensidad\n"
        recomendaciones += "   - Trabaja en tu posición sobre la bicicleta\n\n"
        
        recomendaciones += "2. Fase de Mejora:\n"
        recomendaciones += "   - Incorpora entrenamientos de intervalos\n"
        recomendaciones += "   - Realiza sesiones de fuerza en colinas\n"
        recomendaciones += "   - Mejora tu eficiencia con entrenamientos de cadencia\n\n"
        
        recomendaciones += "3. Fase de Especialización:\n"
        recomendaciones += "   - Enfócate en tu tipo de evento (ruta, montaña, etc.)\n"
        recomendaciones += "   - Implementa entrenamientos de alta intensidad\n"
        recomendaciones += "   - Practica técnicas específicas (sprints, descensos, etc.)\n\n"
    else:  # Levantamiento de Pesas
        recomendaciones += "Recomendaciones para Levantamiento de Pesas:\n"
        recomendaciones += "1. Fase de Adaptación:\n"
        recomendaciones += "   - Enfócate en la técnica correcta de los movimientos básicos\n"
        recomendaciones += "   - Establece una base de fuerza con series de repeticiones moderadas\n"
        recomendaciones += "   - Trabaja en la flexibilidad y movilidad\n\n"
        
        recomendaciones += "2. Fase de Mejora:\n"
        recomendaciones += "   - Aumenta gradualmente el peso y reduce las repeticiones\n"
        recomendaciones += "   - Incorpora variaciones de los ejercicios principales\n"
        recomendaciones += "   - Implementa métodos de entrenamiento como series descendentes o supersets\n\n"
        
        recomendaciones += "3. Fase de Especialización:\n"
        recomendaciones += "   - Enfócate en tus levantamientos competitivos\n"
        recomendaciones += "   - Implementa ciclos de intensidad variable\n"
        recomendaciones += "   - Trabaja en la velocidad y potencia de tus levantamientos\n\n"
    
    # Recomendaciones basadas en el nivel de entrenamiento
    if nivel_entrenamiento == "Principiante":
        recomendaciones += "Consejos para Principiantes:\n"
        recomendaciones += "- Prioriza la consistencia en tus entrenamientos\n"
        recomendaciones += "- Escucha a tu cuerpo y descansa adecuadamente\n"
        recomendaciones += "- No te compares con otros, enfócate en tu propio progreso\n\n"
    elif nivel_entrenamiento == "Intermedio":
        recomendaciones += "Consejos para Nivel Intermedio:\n"
        recomendaciones += "- Varía tus entrenamientos para evitar mesetas\n"
        recomendaciones += "- Presta atención a tu nutrición y recuperación\n"
        recomendaciones += "- Considera trabajar con un entrenador para mejorar aspectos específicos\n\n"
    else:  # Avanzado
        recomendaciones += "Consejos para Nivel Avanzado:\n"
        recomendaciones += "- Implementa periodización en tu plan de entrenamiento\n"
        recomendaciones += "- Utiliza tecnología para seguir y analizar tu rendimiento\n"
        recomendaciones += "- Enfócate en pequeñas mejoras y detalles técnicos\n\n"
    
    # Recomendaciones basadas en el objetivo
    if objetivo == "Mejora General":
        recomendaciones += "Enfoque para Mejora General:\n"
        recomendaciones += "- Mantén un equilibrio entre diferentes aspectos de tu entrenamiento\n"
        recomendaciones += "- Establece metas realistas a corto y largo plazo\n"
        recomendaciones += "- Disfruta del proceso y celebra tus logros, por pequeños que sean\n\n"
    elif objetivo == "Competición":
        recomendaciones += "Enfoque para Competición:\n"
        recomendaciones += "- Simula condiciones de competencia en tus entrenamientos\n"
        recomendaciones += "- Trabaja en tu mentalidad y manejo del estrés\n"
        recomendaciones += "- Planifica tu temporada incluyendo períodos de descanso y pico de forma\n\n"
    else:  # Recuperación
        recomendaciones += "Enfoque para Recuperación:\n"
        recomendaciones += "- Prioriza el descanso y el sueño de calidad\n"
        recomendaciones += "- Incorpora técnicas de recuperación activa como yoga o natación suave\n"
        recomendaciones += "- Mantén una actitud positiva y paciente durante tu proceso de recuperación\n\n"
    
    return recomendaciones

