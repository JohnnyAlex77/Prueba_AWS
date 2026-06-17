========================================
CUESTIONARIO AWS ACADEMY
Sistema de Practica para AWS Cloud Architecting
========================================

DESCRIPCION
-----------
Aplicacion de escritorio para practicar preguntas del curso AWS Academy 
Cloud Architecting. El programa selecciona aleatoriamente 25 preguntas 
de un banco de mas de 60 preguntas y permite al usuario responderlas a 
traves de una interfaz grafica.

CARACTERISTICAS
---------------
- Interfaz grafica con Tkinter
- Seleccion aleatoria de 25 preguntas
- Preguntas de seleccion unica (una sola respuesta correcta)
- Guardado automatico de respuestas
- Navegacion entre preguntas (Anterior/Siguiente)
- Resultados detallados al finalizar
- Revision completa con todas las preguntas y respuestas
- Exportacion de la revision a PDF (opcional)
- Indicador de progreso

REQUISITOS
----------
- Python 3.6 o superior
- Tkinter (incluido por defecto en Python)
- ReportLab (opcional, solo para exportar a PDF)

ESTRUCTURA DEL PROYECTO
-----------------------
/

├── main.py              # Codigo principal de la aplicacion

├── questions.json       # Banco de preguntas en formato JSON

├── requirements.txt     # Lista de dependencias (opcional)

└── README.txt           # Este archivo

INSTALACION
-----------
1. Descarga los archivos main.py y questions.json en la misma carpeta.

2. (Opcional) Si deseas exportar la revision a PDF, instala ReportLab:
   pip install reportlab

   O usando requirements.txt:
   pip install -r requirements.txt

EJECUCION
---------
Para iniciar el programa, ejecuta desde la terminal:
   python main.py

O si tienes varias versiones de Python:
   python3 main.py

USO DEL PROGRAMA
----------------
1. Al iniciar, se mostrara la primera pregunta de 25 seleccionadas 
   aleatoriamente.
2. Selecciona tu respuesta haciendo clic en el radio button 
   correspondiente a la opcion que consideres correcta.
3. Usa los botones "Anterior" y "Siguiente" para navegar entre preguntas.
4. El boton "Limpiar" elimina la respuesta seleccionada para la pregunta 
   actual.
5. Cuando hayas respondido todas las preguntas, haz clic en "Finalizar".
6. Se mostrara tu puntuacion y se abrira una ventana con la revision 
   detallada.
7. En la ventana de revision, puedes hacer clic en "Guardar como PDF" 
   para exportar el informe (requiere ReportLab instalado).

ESTRUCTURA DEL ARCHIVO QUESTIONS.JSON
-------------------------------------
El archivo questions.json contiene un array de objetos, donde cada 
objeto representa una pregunta con los siguientes campos:

{
    "id": 1,
    "text": "Enunciado de la pregunta",
    "options": [
        "Opcion A",
        "Opcion B",
        "Opcion C",
        "Opcion D"
    ],
    "correct": ["B"],
    "justification": "Explicacion de la respuesta correcta (opcional)"
}

Campos:
- id: Identificador unico de la pregunta
- text: Enunciado o texto de la pregunta
- options: Lista de opciones (A, B, C, D, ...)
- correct: Lista con una sola letra indicando la respuesta correcta
- justification: Explicacion de la respuesta (campo opcional)


SOLUCION DE PROBLEMAS
---------------------
- Error "No se encuentra el archivo questions.json":
  Asegurate de que el archivo este en la misma carpeta que main.py.
- Error "No se puede importar reportlab":
  Instala el modulo con: pip install reportlab
- Error "TclError" o problemas con la interfaz:
  Verifica que tienes Tkinter instalado. En Linux, puede necesitar:
  sudo apt-get install python3-tk
- El programa no inicia:
  Verifica que tienes Python instalado: python --version

NOTAS ADICIONALES
-----------------
- El programa funciona completamente offline
- No requiere conexion a internet
- Las preguntas estan basadas en el contenido oficial de AWS Academy
- Cada ejecucion selecciona preguntas diferentes aleatoriamente

========================================
AWS Academy Cloud Architecting
Sistema de Practica
========================================
