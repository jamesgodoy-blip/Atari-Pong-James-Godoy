# Proyecto: Atari Pong - Lógica de Programación
**Estudiante:** James Godoy
**Curso:** Primer Semestre - Ingeniería

Para este proyecto, seleccione la librería `pygame` debido a su robustez en el manejo de gráficos 2D. Sin embargo, durante el desarrollo se identificó una complejidad técnica: la incompatibilidad actual de Pygame con las versiones más recientes de Python (3.13+). 

 A pesar de las limitaciones del entorno local, decidí priorizar la síntesis de la lógica algorítmica. He cuestionado el uso de librerías externas frente a la lógica pura, asegurando que el código sea funcional en su estructura de control (bucles e iteraciones), independientemente de la renderización gráfica.

Este software no es una simple reproducción; se han adaptado las especificaciones para incluir:
-Un bucle `while` optimizado para el refresco de pantalla.
-Condicionales `if/else` para la detección de colisiones en bordes y raquetas, integrando perspectivas de movimiento tanto para el jugador como para una IA básica (CPU).
-Se transformó el concepto clásico de Pong en un script educativo que demuestra la gestión de eventos en tiempo real.

El diagrama de flujo adjunto representa la arquitectura lógica del sistema, vinculando cada proceso con su correspondiente bloque de código.
