import tkinter as tk
from app.estilo import colores, dimensiones

class Sidebar(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            width=dimensiones["sidebar_ancho"],
            bg=colores["panel"],
        )
        self.pack_propagate(False)
        self._crear_logo()
    
    def _crear_logo(self):
        contenedor = tk.Frame(
        self, 
        bg=colores["panel"]
    )   
        contenedor.pack(
            fill="x",
            padx=18,
            pady=(24, 28)    
        )

        tk.Label(
            contenedor,
            text="◉",
            bg=colores["panel"],
            fg=colores["azul"],
            font=("Segoe UI", 20),
        ).pack(side="left")

        tk.Label(
            contenedor,
            text="Presenter AI",
            bg=colores["panel"],
            fg=colores["texto"],
            font=("Segoe UI", 14, "bold"),
        ).pack(side="left", padx=(8, 0))