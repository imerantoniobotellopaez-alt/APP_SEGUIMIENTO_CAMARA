import tkinter as tk
from app.estilo import colores

class Encabezado(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=colores["panel"])
        self._crear_titulo()
        self._crear_estado()

    def _crear_titulo(self):
        tk.Label(
            self,
            text="▣",
            bg=colores["panel"],
            fg=colores["azul"],
            font=("Segoe UI", 16),
        ).pack(
            side="left", 
            padx=(16, 8),
            pady=12
        )
    
        tk.Label(
            self,
            text="Seguimiento",
            bg=colores["panel"],
            fg=colores["texto"],
            font=("Segoe UI", 16, "bold"),
        ).pack(
            side="left",
            pady=12
        )
    
    def _crear_estado(self):
        contenedor = tk.Frame(self, bg=colores["panel"])
        contenedor.pack(
            side="right",
            padx=16,
            pady=12
        )
        