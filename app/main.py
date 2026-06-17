# main.py
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import random
from datetime import datetime


class QuizApp:
    def __init__(self, root, questions_file="questions.json"):
        self.root = root
        self.root.title("Cuestionario AWS Academy - 25 preguntas aleatorias")
        self.root.geometry("900x700")
        self.root.resizable(True, True)

        # Cargar preguntas desde archivo JSON
        self.questions = self.load_questions(questions_file)
        if not self.questions:
            messagebox.showerror(
                "Error",
                "No se pudieron cargar las preguntas. Verifica que el archivo questions.json exista."
            )
            self.root.destroy()
            return

        # Asegurar que self.questions es una lista
        if isinstance(self.questions, dict):
            self.questions = list(self.questions.values())
        elif not isinstance(self.questions, list):
            messagebox.showerror(
                "Error",
                "El formato de questions.json no es valido. Debe ser una lista o diccionario."
            )
            self.root.destroy()
            return

        # Seleccionar 25 preguntas aleatorias
        self.selected_questions = random.sample(self.questions, min(25, len(self.questions)))
        self.total = len(self.selected_questions)
        self.current_index = 0

        # Almacenar respuestas del usuario
        self.user_answers = ["" for _ in range(self.total)]

        # Variables para los widgets
        self.question_label = None
        self.options_frame = None
        self.radio_var = None
        self.progress_label = None

        # Construir interfaz
        self.build_widgets()
        self.show_question()

    def load_questions(self, filename):
        """Carga las preguntas desde un archivo JSON."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo '{0}' no encontrado.".format(filename))
            return []
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", "Error al leer el archivo JSON: {0}".format(e))
            return []

    def build_widgets(self):
        """Construye la interfaz de usuario."""
        # Marco principal
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Titulo
        title_label = ttk.Label(
            main_frame,
            text="Cuestionario AWS Academy Cloud Architecting",
            font=("Arial", 14, "bold")
        )
        title_label.pack(pady=(0, 15))

        # Marco para la pregunta
        question_frame = ttk.Frame(main_frame)
        question_frame.pack(fill=tk.X, pady=(0, 10))

        # Pregunta
        self.question_label = ttk.Label(
            question_frame,
            text="",
            wraplength=850,
            font=("Arial", 11)
        )
        self.question_label.pack(anchor="w")

        # Progreso
        self.progress_label = ttk.Label(
            question_frame,
            text="",
            font=("Arial", 10)
        )
        self.progress_label.pack(anchor="e", pady=(5, 0))

        # Marco para opciones
        self.options_frame = ttk.Frame(main_frame)
        self.options_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Marco para botones de navegacion
        nav_frame = ttk.Frame(main_frame)
        nav_frame.pack(pady=15)

        self.prev_btn = ttk.Button(
            nav_frame,
            text="Anterior",
            command=self.prev_question
        )
        self.prev_btn.pack(side=tk.LEFT, padx=5)

        self.next_btn = ttk.Button(
            nav_frame,
            text="Siguiente",
            command=self.next_question
        )
        self.next_btn.pack(side=tk.LEFT, padx=5)

        self.submit_btn = ttk.Button(
            nav_frame,
            text="Finalizar",
            command=self.submit_quiz
        )
        self.submit_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = ttk.Button(
            nav_frame,
            text="Limpiar",
            command=self.clear_current_answer
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)

        # Barra de estado
        self.status_label = ttk.Label(
            main_frame,
            text="Selecciona una opcion para cada pregunta",
            font=("Arial", 9),
            foreground="gray"
        )
        self.status_label.pack(pady=(5, 0))

    def show_question(self):
        """Muestra la pregunta actual y sus opciones."""
        # Limpiar frame de opciones
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        q = self.selected_questions[self.current_index]
        self.question_label.config(text="{0}. {1}".format(self.current_index + 1, q['text']))
        self.progress_label.config(
            text="Pregunta {0} de {1}".format(self.current_index + 1, self.total)
        )

        # Variable para el RadioButton
        self.radio_var = tk.StringVar(value="")

        # Cargar respuesta previa si existe
        if self.user_answers[self.current_index]:
            self.radio_var.set(self.user_answers[self.current_index])

        # Crear opciones
        for idx, opt in enumerate(q['options']):
            letter = chr(65 + idx)  # A, B, C, D...
            rb = tk.Radiobutton(
                self.options_frame,
                text="{0}. {1}".format(letter, opt),
                variable=self.radio_var,
                value=letter,
                font=("Arial", 10),
                anchor="w",
                justify="left",
                wraplength=850
            )
            rb.pack(anchor="w", padx=20, pady=3)

        # Actualizar estado de botones
        if self.current_index > 0:
            self.prev_btn.config(state=tk.NORMAL)
        else:
            self.prev_btn.config(state=tk.DISABLED)

        if self.current_index < self.total - 1:
            self.next_btn.config(state=tk.NORMAL)
        else:
            self.next_btn.config(state=tk.DISABLED)

        # Actualizar estado
        if self.user_answers[self.current_index]:
            self.status_label.config(text="Respuesta guardada")
        else:
            self.status_label.config(text="Selecciona una opcion")

    def clear_current_answer(self):
        """Limpia la respuesta actual."""
        self.radio_var.set("")
        self.user_answers[self.current_index] = ""
        self.status_label.config(text="Respuesta eliminada")

    def save_current_answer(self):
        """Guarda la seleccion actual."""
        self.user_answers[self.current_index] = self.radio_var.get()

    def next_question(self):
        """Avanza a la siguiente pregunta."""
        self.save_current_answer()
        if self.current_index < self.total - 1:
            self.current_index += 1
            self.show_question()

    def prev_question(self):
        """Retrocede a la pregunta anterior."""
        self.save_current_answer()
        if self.current_index > 0:
            self.current_index -= 1
            self.show_question()

    def submit_quiz(self):
        """Finaliza el cuestionario, calcula puntuacion y muestra revision."""
        self.save_current_answer()

        # Verificar preguntas sin responder
        unanswered = []
        for i, ans in enumerate(self.user_answers):
            if not ans:
                unanswered.append(i + 1)

        if unanswered:
            msg = "Las preguntas {0} no tienen respuesta.\n\nDeseas finalizar de todas formas?".format(
                ', '.join(map(str, unanswered))
            )
            if not messagebox.askyesno("Preguntas sin responder", msg):
                return

        # Calcular respuestas correctas
        correct_count = 0
        incorrect_questions = []

        for i, q in enumerate(self.selected_questions):
            user_ans = self.user_answers[i]
            correct_ans = q['correct'][0]
            if user_ans == correct_ans:
                correct_count += 1
            else:
                incorrect_questions.append(i + 1)

        porcentaje = (correct_count / self.total) * 100

        # Construir mensaje de resultado
        mensaje = "Puntuacion: {0} de {1}\n".format(correct_count, self.total)
        mensaje += "Porcentaje: {0:.1f}%\n\n".format(porcentaje)

        if porcentaje >= 80:
            mensaje += "Excelente! Has demostrado un gran conocimiento."
        elif porcentaje >= 60:
            mensaje += "Bien hecho. Revisa los temas donde fallaste."
        else:
            mensaje += "Te recomendamos repasar los materiales del curso."

        if incorrect_questions:
            mensaje += "\n\nPreguntas incorrectas: {0}".format(
                ', '.join(map(str, incorrect_questions))
            )

        messagebox.showinfo("Resultado", mensaje)
        self.show_review()

    def show_review(self):
        """Ventana con todas las preguntas y respuestas."""
        review_window = tk.Toplevel(self.root)
        review_window.title("Revision de Respuestas")
        review_window.geometry("950x750")
        review_window.transient(self.root)

        # Marco superior con botones
        top_frame = ttk.Frame(review_window)
        top_frame.pack(fill=tk.X, padx=10, pady=5)

        label = ttk.Label(
            top_frame,
            text="Revision Detallada",
            font=("Arial", 12, "bold")
        )
        label.pack(side=tk.LEFT)

        save_pdf_btn = ttk.Button(
            top_frame,
            text="Guardar como PDF",
            command=lambda: self.save_review_to_pdf(review_window)
        )
        save_pdf_btn.pack(side=tk.RIGHT, padx=5)

        text_area = scrolledtext.ScrolledText(
            review_window,
            wrap=tk.WORD,
            font=("Arial", 10)
        )
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        for i, q in enumerate(self.selected_questions):
            user_ans = self.user_answers[i]
            correct_ans = q['correct'][0]
            is_correct = (user_ans == correct_ans)

            if is_correct:
                status = "CORRECTO"
            else:
                status = "INCORRECTO"

            text_area.insert(tk.END, "\n{0}\n".format('=' * 85))
            text_area.insert(tk.END, "PREGUNTA {0}: {1}\n".format(i + 1, q['text']))
            text_area.insert(tk.END, "{0}\n".format('-' * 85))
            text_area.insert(
                tk.END,
                "  Tu respuesta: {0}\n".format(user_ans if user_ans else '(ninguna)')
            )
            text_area.insert(tk.END, "  Correcta: {0}\n".format(correct_ans))
            text_area.insert(tk.END, "  Estado: {0}\n".format(status))

            if 'justification' in q and q['justification']:
                text_area.insert(tk.END, "  Justificacion: {0}\n".format(q['justification']))

        text_area.config(state=tk.DISABLED)
        review_window.text_area = text_area

        close_btn = ttk.Button(review_window, text="Cerrar", command=review_window.destroy)
        close_btn.pack(pady=10)

    def save_review_to_pdf(self, review_window):
        """Guarda la revision en formato PDF."""
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
            from reportlab.lib.enums import TA_CENTER

            # Obtener el texto de la revision
            text_content = review_window.text_area.get("1.0", tk.END)

            # Generar nombre de archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = "revision_cuestionario_{0}.pdf".format(timestamp)

            # Crear PDF
            doc = SimpleDocTemplate(filename, pagesize=A4)
            styles = getSampleStyleSheet()

            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=16,
                alignment=TA_CENTER,
                spaceAfter=20
            )
            question_style = ParagraphStyle(
                'QuestionStyle',
                parent=styles['Normal'],
                fontSize=11,
                spaceAfter=6,
                spaceBefore=12
            )
            normal_style = ParagraphStyle(
                'Normal',
                parent=styles['Normal'],
                fontSize=10,
                spaceAfter=4
            )

            story = []
            story.append(Paragraph("Revision de Cuestionario AWS Academy", title_style))
            story.append(Paragraph(
                "Fecha: {0}".format(datetime.now().strftime('%d/%m/%Y %H:%M')),
                normal_style
            ))
            story.append(Spacer(1, 0.2 * inch))

            # Procesar lineas del texto
            lines = text_content.split('\n')
            for line in lines:
                line = line.strip()
                if not line:
                    story.append(Spacer(1, 0.1 * inch))
                    continue

                if line.startswith('PREGUNTA '):
                    clean_line = line.replace('', '').strip()
                    story.append(Paragraph(clean_line, question_style))
                elif line.startswith('  Tu respuesta:') or line.startswith('  Correcta:') or line.startswith('  Estado:'):
                    clean_line = line.replace('', '')
                    story.append(Paragraph(clean_line, normal_style))
                elif line.startswith('  Justificacion:'):
                    clean_line = line.replace('', 'Nota:')
                    story.append(Paragraph(clean_line, normal_style))
                elif '=' in line or '-' in line:
                    continue
                else:
                    story.append(Paragraph(line, normal_style))

            # Construir PDF
            doc.build(story)
            messagebox.showinfo("Exito", "PDF guardado como: {0}".format(filename))

        except ImportError:
            messagebox.showerror(
                "Error",
                "No se encontro el modulo reportlab.\n\nInstalalo con: pip install reportlab"
            )
        except Exception as e:
            messagebox.showerror("Error", "Error al guardar PDF: {0}".format(str(e)))

    def run(self):
        """Inicia la aplicacion."""
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root, "questions.json")
    app.run()