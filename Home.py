from customtkinter import *
from funciones import dda, bresenham, circunferencia, ellipse
import tkinter as tk
from PIL import Image, ImageTk
import os

# Constantes
SIDEBAR_WIDTH = 176
SIDEBAR_HEIGHT = 650
CONTENT_WIDTH = 680
CONTENT_HEIGHT = 650
APP_WIDTH = 856
APP_HEIGHT = 645

# Barra lateral fija
class Sidebar(CTkFrame):
    def __init__(self, master: CTk, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#2A8C55", width=SIDEBAR_WIDTH, height=SIDEBAR_HEIGHT, corner_radius=0)
        self.pack_propagate(0)
        self.pack(fill="y", anchor="w", side="left")

        logo_img_data = Image.open(r"GUI-calculo-de-algoritmos\images\logo.png")
        logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

        CTkLabel(master=self, text="", image=logo_img).pack(pady=(38, 0), anchor="center")


        self.botones = []
        data_boton = [
            {"text": "Presentacion", "image_path": r"GUI-calculo-de-algoritmos\images\analytics_icon.png"},
            {"text": "DDA", "image_path": r"GUI-calculo-de-algoritmos\images\package_icon.png"},
            {"text": "Bresenham", "image_path": r"GUI-calculo-de-algoritmos\images\list_icon.png"},
            {"text": "Circunferencia", "image_path": r"GUI-calculo-de-algoritmos\images\returns_icon.png"},
            {"text": "Elipse", "image_path": r"GUI-calculo-de-algoritmos\images\settings_icon.png"},
            {"text": "Salir", "image_path": r"GUI-calculo-de-algoritmos\images\person_icon.png"}
        ]

        for info_boton in data_boton:
            boton_img_data = Image.open(info_boton["image_path"])
            boton_img = CTkImage(dark_image=boton_img_data, light_image=boton_img_data)
            button = CTkButton(master=self, image=boton_img, text=info_boton["text"], fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w")
            button.pack(anchor="center", ipady=5, pady=(16, 0))
            self.botones.append(button)

        for button in self.botones:
            button.configure(command=lambda texto_boton=button.cget("text"): self.content.change_content(texto_boton))

# Contenido para los algoritmos
class Content(CTkFrame):
    def __init__(self, master: CTk, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#fff", width=CONTENT_WIDTH, height=CONTENT_HEIGHT, corner_radius=0)
        self.pack_propagate(0)
        self.pack(side="left")

        self.label = CTkLabel(master=self, text="Bienvenido 1SF142 ", font=("Arial Black", 25), text_color="#2A8C55")
        self.label.place(relx=0.5, rely=0.5, anchor="center")

    def change_content(self, texto_boton: str):
        self.valores = {}

        for widget in self.winfo_children():
            widget.destroy()

        if texto_boton == "DDA":
            self.show_dda_content()
        elif texto_boton == "Bresenham":
            self.show_bresenham_content()
        elif texto_boton == "Circunferencia":
            self.show_circunferencia_content()
        elif texto_boton == "Elipse":
            self.show_elipse_content()
        elif texto_boton == "Salir":
            self.master.destroy()
        else:
            self.show_welcome_content()
    
    # Contenido de Presentacion
    def show_welcome_content(self):
        self.imagen_presentacion = Image.open(r"GUI-calculo-de-algoritmos\images\Portada.png")
        self.imagen_presentacion.thumbnail((1000, 1600)) 
        self.label = CTkLabel(master=self, text="Presentacion", font=("Arial Black", 25), text_color="#2A8C55")
        self.label.pack(anchor="nw", pady=(29,0), padx=27)

        # Convertir la imagen a un objeto PhotoImage de tkinter
        imagen = ImageTk.PhotoImage(self.imagen_presentacion)

        # Mostrar la imagen en un widget Label
        label_imagen = CTkLabel(master=self, image=imagen)
        label_imagen.pack()

        # Guardar una referencia a la imagen para evitar que se elimine
        label_imagen.image = imagen

    # Mostrar contenido para algoritmo de DDA
    def show_dda_content(self):
        self.label = CTkLabel(master=self, text="Ingrese los puntos para DDA", font=("Arial Black", 25), text_color="#2A8C55")
        self.label.pack(anchor="nw", pady=(29,0), padx=27)
        
        grid = CTkFrame(master=self, fg_color="transparent")
        grid.pack(fill="both", padx=27, pady=(31,0))

        self.label = CTkLabel(master=grid, text="X1", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=0, column=0, sticky="w")
        self.x1_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
        self.x1_entrada.grid(row=1, column=0, ipady=10)

        self.label = CTkLabel(master=grid, text="Y1", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=0, column=1, sticky="w")
        self.y1_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
        self.y1_entrada.grid(row=1, column=1, ipady=10, padx=(24,0))

        self.label = CTkLabel(master=grid, text="X2", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=2, column=0, sticky="w")
        self.x2_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
        self.x2_entrada.grid(row=3, column=0, ipady=10)

        self.label = CTkLabel(master=grid, text="Y2", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=2, column=1, sticky="w")
        self.y2_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
        self.y2_entrada.grid(row=3, column=1, ipady=10, padx=(24,0))

        CTkLabel(master=grid, text="Direccion de la grafica:", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=4, column=0, sticky="w", pady=(38, 0))

        self.direccion = tk.StringVar()

        CTkRadioButton(master=grid, variable=self.direccion, value="derecha", text="De Derecha a Izquierda", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=5, column=0, sticky="w", pady=(16,0))
        CTkRadioButton(master=grid, variable=self.direccion, value="izquierda",text="De Izquierda a Derecha", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=6, column=0, sticky="w", pady=(16,0))

        self.crear_boton_graficar(dda)

    # Mostrar contenido para algoritmo de Bresenham
    def show_bresenham_content(self):
       self.label = CTkLabel(master=self, text="Ingrese los puntos para Bresenham", font=("Arial Black", 25), text_color="#2A8C55")
       self.label.pack(anchor="nw", pady=(29,0), padx=27)    

       grid = CTkFrame(master=self, fg_color="transparent")
       grid.pack(fill="both", padx=27, pady=(31,0))

       self.label = CTkLabel(master=grid, text="X1", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=0, column=0, sticky="w")
       self.x1_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.x1_entrada.grid(row=1, column=0, ipady=10)

       self.label = CTkLabel(master=grid, text="Y1", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=0, column=1, sticky="w")
       self.y1_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.y1_entrada.grid(row=1, column=1, ipady=10, padx=(24,0))

       self.label = CTkLabel(master=grid, text="X2", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=2, column=0, sticky="w")
       self.x2_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.x2_entrada.grid(row=3, column=0, ipady=10)

       self.label = CTkLabel(master=grid, text="Y2", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=2, column=1, sticky="w")
       self.y2_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.y2_entrada.grid(row=3, column=1, ipady=10, padx=(24,0))

       self.crear_boton_graficar(bresenham)

    # Mostrar contenido para algoritmo de la Circunferencia
    def show_circunferencia_content(self):
       self.label = CTkLabel(master=self, text="Ingrese los puntos para la Circunferencia", font=("Arial Black", 25), text_color="#2A8C55")
       self.label.pack(anchor="nw", pady=(29,0), padx=27)    

       grid = CTkFrame(master=self, fg_color="transparent")
       grid.pack(fill="both", padx=27, pady=(31,0))

       self.label = CTkLabel(master=grid, text="Xc", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=0, column=0, sticky="w")
       self.xc_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.xc_entrada.grid(row=1, column=0, ipady=10)

       self.label = CTkLabel(master=grid, text="Yc", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=0, column=1, sticky="w")
       self.yc_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.yc_entrada.grid(row=1, column=1, ipady=10, padx=(24,0))

       self.label = CTkLabel(master=grid, text="r", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=2, column=0, sticky="w")
       self.r_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.r_entrada.grid(row=3, column=0, ipady=10)

       self.crear_boton_circunferencia(circunferencia)

    # Mostrar contenido para algoritmo de la Elipse
    def show_elipse_content(self):
       self.label = CTkLabel(master=self, text="Ingrese los puntos para la Elipse", font=("Arial Black", 25), text_color="#2A8C55")
       self.label.pack(anchor="nw", pady=(29,0), padx=27)    

       grid = CTkFrame(master=self, fg_color="transparent")
       grid.pack(fill="both", padx=27, pady=(31,0))

       self.label = CTkLabel(master=grid, text="RX", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=0, column=0, sticky="w")
       self.rx_entry = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.rx_entry.grid(row=1, column=0, ipady=10)

       self.label = CTkLabel(master=grid, text="RY", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=0, column=1, sticky="w")
       self.ry_entry = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.ry_entry.grid(row=1, column=1, ipady=10, padx=(24,0))

       self.label = CTkLabel(master=grid, text="XC", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=2, column=0, sticky="w")
       self.xc_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.xc_entrada.grid(row=3, column=0, ipady=10)

       self.label = CTkLabel(master=grid, text="YC", font=("Arial Bold", 14), text_color="#52A476", justify="left").grid(row=2, column=1, sticky="w")
       self.yc_entrada = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
       self.yc_entrada.grid(row=3, column=1, ipady=10, padx=(24,0))

       self.crear_boton_elipse(ellipse)

    # Crear boton para graficar algoritmos de DDA y Bresenham
    def crear_boton_graficar(self, funcion):
        actions = CTkFrame(master=self, fg_color="transparent")
        actions.pack(fill="both")
        print("Creando boton de graficar")

        # Obteniendo las variebles para graficar
        boton_graficar = CTkButton(master=actions, text="Graficar", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#2A8C55", hover_color="#eee", border_width=2, text_color="#2A8C55")
        boton_graficar.configure(command=lambda: self.graficar(funcion, {
            'x1': self.x1_entrada.get(),
            'y1': self.y1_entrada.get(),
            'x2': self.x2_entrada.get(),
            'y2': self.y2_entrada.get(),
            'direccion': self.direccion.get()
        }))
        boton_graficar.pack(side="left", anchor="center", pady=(15,0), padx=(27,24))
        print(boton_graficar['command'])

    # Crear boton para graficar algoritmo de la Circunferencia
    def crear_boton_circunferencia(self, funcion):
        actions = CTkFrame(master=self, fg_color="transparent")
        actions.pack(fill="both")
        print("Creando boton de graficar")

        # Botón para graficar
        boton_graficar = CTkButton(master=actions, text="Graficar", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#2A8C55", hover_color="#eee", border_width=2, text_color="#2A8C55")
        boton_graficar.configure(command=lambda: self.graficar(funcion, {
            'Xc': self.xc_entrada.get(),
            'Yc': self.yc_entrada.get(),
            'R': self.r_entrada.get(),
        }))
        boton_graficar.pack(side="left", anchor="center", pady=(15,0), padx=(27,24))
        print(boton_graficar['command'])

    # Crear boton para graficar algoritmo de la Elipse
    def crear_boton_elipse(self, funcion):
        actions = CTkFrame(master=self, fg_color="transparent")
        actions.pack(fill="both")
        print("Creando boton de graficar")

        # Botón para graficar
        boton_graficar = CTkButton(master=actions, text="Graficar", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#2A8C55", hover_color="#eee", border_width=2, text_color="#2A8C55")
        boton_graficar.configure(command=lambda: self.graficar(funcion, {
            'Rx': self.rx_entry.get(),
            'Ry': self.ry_entry.get(),
            'Xc': self.xc_entrada.get(),
            'Yc': self.yc_entrada.get()

        }))
        boton_graficar.pack(side="left", anchor="center", pady=(15,0), padx=(27,24))
        print(boton_graficar['command'])
            
        
    def graficar(self, funcion, valores):
        if 'direccion' in valores:  # Verificar si 'direccion' esta en el diccionario
            direccion = valores.pop('direccion')  
        else:
            direccion = None

        # El  diccionario solo contiene valores de x1,y1,x2,y2
        valores = {key: self.convertir_a_entero(valor) for key, valor in valores.items()}
        if direccion is not None:
            valores['direccion'] = direccion
        
        funcion(**valores)
        print("Graficando...")

    def convertir_a_entero(self, valor):
        try:
            return int(valor)
        except ValueError:
            # Manejar el caso en que no se pueda convertir a entero
            print(f"Error: No se pudo convertir '{valor}' a entero.")
            return 0 


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.resizable(0, 0)
        set_appearance_mode("light")

        self.sidebar = Sidebar(self)
        self.content = Content(self)

        for button in self.sidebar.botones:
            button.configure(command=lambda texto_boton=button.cget("text"): self.content.change_content(texto_boton))

if __name__ == "__main__":
    print(os.getcwd())
    app = App()
    app.mainloop()