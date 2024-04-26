import tkinter as tk
from tkinter import messagebox

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo de Aplicacion")
        self.geometry("400x200")

        # Etiqueta
        self.etiqueta = tk.Label(self, text="Carlos Martinez Tobinson")
        self.etiqueta.pack()

        # Cuadro de entrada
        self.cuadro_texto = tk.Entry(self)
        self.cuadro_texto.pack()

        # Botón
        self.boton = tk.Button(self, text="Ingresa lo que quieras ;)", command=self.mostrar_texto)
        self.boton.pack()

        # Botón de salida
        self.boton_salir = tk.Button(self, text="Salir", command=self.salir)
        self.boton_salir.pack()

    def mostrar_texto(self):
        texto = self.cuadro_texto.get()
        messagebox.showinfo("Texto ingresado", f"Aqui veras lo que escribiste ;): {texto}")

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?"):
            self.destroy()

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
