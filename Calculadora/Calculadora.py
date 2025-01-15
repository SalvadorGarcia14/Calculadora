import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x600")
        self.resizable(False, False)

        # Variables
        self.operacion = ""
        self.resultado = tk.StringVar()
        self.historial = []  # Lista para almacenar el historial de operaciones
        self.es_nuevo_resultado = False  # Bandera para controlar el reinicio al ingresar un número

        # Crear los widgets
        self.crear_widgets()
    
    def crear_widgets(self):
        # Pantalla
        pantalla = tk.Entry(self, textvariable=self.resultado, font=("Arial", 24), justify="right", bd=10)
        pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Configurar las filas y columnas para que se expandan correctamente
        for i in range(4):
            self.grid_columnconfigure(i, weight=1, uniform="equal")
        self.grid_rowconfigure(0, weight=1)

        # Botones
        botones = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+",
            "↩"  # Botón para regresar a la operación anterior
        ]

        for i, boton in enumerate(botones):
            tk.Button(
                self, text=boton, font=("Arial", 18), height=2, width=5,
                command=lambda b=boton: self.evento_click(b)
            ).grid(row=1 + i // 4, column=i % 4, padx=5, pady=5, sticky="nsew")

    def evento_click(self, boton: str):
        if boton == "C":
            # Resetear todo
            self.operacion = ""
            self.resultado.set("")
            self.es_nuevo_resultado = False
        elif boton == "=":
            # Evaluar la operación
            try:
                if self.operacion:
                    resultado_actual = str(eval(self.operacion))
                    self.historial.append(self.operacion)  # Guardar operación actual en el historial
                    self.operacion = resultado_actual
                    self.resultado.set(self.operacion)
                    self.es_nuevo_resultado = True  # Marcar como nuevo resultado
            except:
                self.resultado.set("Error")
                self.operacion = ""
        elif boton == "↩":
            # Regresar a la operación anterior
            if self.historial:
                self.operacion = self.historial.pop()  # Recuperar la última operación del historial
                self.resultado.set(self.operacion)
            else:
                self.operacion = ""
                self.resultado.set("0")
        elif boton in "+-*/":
            # Si es un operador, continuar con la operación
            if self.es_nuevo_resultado:
                self.es_nuevo_resultado = False
            self.operacion += boton
            self.resultado.set(self.operacion)
        else:
            # Si es un número
            if self.es_nuevo_resultado:
                # Reiniciar la operación si estamos en un nuevo resultado
                self.operacion = ""
                self.es_nuevo_resultado = False
            self.operacion += boton
            self.resultado.set(self.operacion)