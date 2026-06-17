README.txt
===========
CUESTIONARIO AWS ACADEMY - SISTEMA DE PRÁCTICA
==============================================

DESCRIPCIÓN
-----------
Esta aplicación es una herramienta de estudio diseñada para practicar 
preguntas del curso AWS Academy Cloud Architecting. El programa 
selecciona aleatoriamente 25 preguntas de un banco de 80
preguntas y permite al usuario responderlas a través de una interfaz 
gráfica intuitiva.

CARACTERÍSTICAS
---------------
Interfaz gráfica con Tkinter
Selección aleatoria de 25 preguntas
Soporte para preguntas de respuesta única (radio button)
Guardado automático de respuestas
Navegación entre preguntas (Anterior/Siguiente)
Resultados detallados al finalizar
Revisión completa con todas las preguntas y respuestas
Exportación de la revisión a PDF (requiere reportlab)
Indicador de progreso

REQUISITOS
----------
- Python 3.6 o superior
- Tkinter (normalmente incluido con Python)
- ReportLab (para exportar a PDF, opcional)

INSTALACIÓN DE DEPENDENCIAS
---------------------------
Para la funcionalidad completa (incluyendo exportación a PDF):

pip install reportlab

Si no deseas instalar reportlab, el programa funcionará igualmente, 
pero no podrás guardar la revisión en formato PDF.

ESTRUCTURA DEL PROYECTO
-----------------------
/
├── main.py              # Código principal de la aplicación
├── questions.json       # Banco de preguntas en formato JSON
├── README.txt           # Este archivo
└── requirements.txt     # Lista de dependencias (opcional)

CÓMO USAR LA APLICACIÓN
-----------------------
1. Asegúrate de tener los archivos main.py y questions.json en la 
   misma carpeta.
2. Ejecuta el programa:
   python main.py
3. La interfaz mostrará la primera pregunta de 25 seleccionadas 
   aleatoriamente.
4. Selecciona tu respuesta:
   - Para preguntas de respuesta única, haz clic en el radio button 
     correspondiente.
   - Para preguntas de respuesta múltiple, marca todas las opciones 
     que consideres correctas.
5. Usa los botones "Anterior" y "Siguiente" para navegar entre 
   preguntas.
6. El botón "Limpiar" elimina la respuesta seleccionada para la 
   pregunta actual.
7. Cuando hayas respondido todas las preguntas, haz clic en 
   "Finalizar".
8. Se mostrará tu puntuación y se abrirá una ventana con la revisión 
   detallada.
9. En la ventana de revisión, puedes hacer clic en "Guardar como PDF" 
   para exportar el informe (requiere reportlab instalado).

ESTRUCTURA DEL ARCHIVO QUESTIONS.JSON
-------------------------------------
El archivo questions.json contiene un array de objetos, donde cada 
objeto representa una pregunta con los siguientes campos:

{
    "id": 1,                    # Identificador único
    "text": "Enunciado de la pregunta",
    "options": [                # Lista de opciones (A, B, C, D...)
        "Opción A",
        "Opción B",
        "Opción C",
        "Opción D"
    ],
    "correct": ["A", "C"],      # Letras de las respuestas correctas
    "justification": "Explicación de la respuesta correcta (opcional)"
}

NOTAS SOBRE LAS RESPUESTAS MÚLTIPLES
------------------------------------
- Si "correct" contiene una sola letra, la pregunta se mostrará con 
  radio buttons (respuesta única).
- Si "correct" contiene dos o más letras, la pregunta se mostrará con 
  check boxes (respuesta múltiple).
- En preguntas de respuesta múltiple, el usuario debe seleccionar 
  TODAS las opciones correctas para acertar.

EJEMPLO DE USO
--------------
1. Ejecutar el programa
2. Responder las 25 preguntas
3. Hacer clic en "Finalizar"
4. Ver el resultado: "Puntuación: 18 de 25 (72.0%)"
5. Revisar las respuestas incorrectas en la ventana de revisión
6. Guardar el informe como PDF si se desea

SOLUCIÓN DE PROBLEMAS
---------------------
- Si el programa no encuentra questions.json, asegúrate de que el 
  archivo esté en la misma carpeta que main.py.
- Si aparece un error con reportlab al guardar PDF, instala el módulo:
  pip install reportlab
- Si la ventana no se muestra correctamente, verifica que tienes 
  Python instalado correctamente y que Tkinter está disponible.

NOTAS ADICIONALES
-----------------
- Las preguntas se seleccionan aleatoriamente cada vez que se ejecuta 
  el programa, por lo que cada intento es diferente.
- Las respuestas se guardan automáticamente al navegar entre 
  preguntas.
- El programa está diseñado para ser completamente offline, sin 
  necesidad de conexión a internet.
- Todas las preguntas están basadas en el contenido oficial del curso 
  AWS Academy Cloud Architecting.