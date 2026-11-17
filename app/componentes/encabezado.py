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

        badge = tk.Frame(contenedor, bg=colores["panel_secundario"])
        badge.pack()

        tk.Label(
            badge,
            text="●",
            bg=colores["panel_secundario"],
            fg=colores["verde"],
            font=("Segoe UI", 8),
        ).pack(
            side="left", 
            padx=(10, 6), 
            pady=5
        )

        tk.Label(
            badge,
            text="camara conectada",
            bg=colores["panel_secundario"],
            fg=colores["texto_secundario"],
            font=("Segoe UI", 9),
        ).pack(
            side="left",
            padx=(0, 10),
            pady=5
        )