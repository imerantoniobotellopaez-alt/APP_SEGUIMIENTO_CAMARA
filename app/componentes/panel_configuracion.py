import tkinter as tk
from app.estilo import colores

class PanelConfiguracion(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=colores["panel"])
        self._crear_tarjetas()
        
    def _crear_tarjetas(self):
        tk.Label(
            self, 
            text="Configuracion",
            bg=colores["panel"],
            fg=colores["texto"],
            font=("Segoe UI", 13, "bold"),
        ).pack(anchor="w", padx=16, pady=(16, 8))

        contenedor = tk.Frame(self, bg=colores["panel"])
        contenedor.pack(fill="x", padx=6)

        contenedor.grid_columnconfigure(0, weight=1)
        contenedor.grid_columnconfigure(1, weight=1)

        self._crear_tarjeta(contenedor, 0, "Formato de salida", "16:9")
        self._crear_tarjeta(contenedor, 1, "Resolucion", "1280 x 720")

    def _crear_tarjeta(self, parent, columna, etiqueta, valor):
        tarjeta = tk.Frame(parent, bg=colores["panel_secundario"])
        tarjeta.grid(
            row=0,
            column=columna,
            sticky="nsew",
            padx=(0, 6) if columna == 0 else (6, 0),
        )

        tk.Label(
            tarjeta,
            text=etiqueta,
            bg=colores["panel_secundario"],
            fg=colores["texto_secundario"],
            font=("Segoe UI", 9),
        ).pack(anchor="w", padx=12, pady=(10, 0))

        tk.Label(
            tarjeta,
            text=valor,
            bg=colores["panel_secundario"],
            fg=colores["texto"],
            font=("Segoe UI", 13, "bold"),
        ).pack(anchor="w", padx=12, pady=(2, 10))