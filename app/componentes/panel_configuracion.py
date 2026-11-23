import tkinter as tk
from tkinter import ttk 
from app.estilo import colores

class PanelConfiguracion(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=colores["panel"])
        self._crear_tarjetas()
        self._crear_estado()
        self._crear_botones()
        self.set_activo(False)

    def _crear_tarjetas(self):
        tk.Label(
            self, 
            text="Configuracion",
            bg=colores["panel"],
            fg=colores["texto"],
            font=("Segoe UI", 13, "bold"),
        ).pack(anchor="w", padx=16, pady=(16, 8))

        contenedor = tk.Frame(self, bg=colores["panel"])
        contenedor.pack(fill="x", padx=16)

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

    def _crear_estado(self):
        contenedor = tk.Frame(self, bg=colores["panel"])
        contenedor.pack(fill="x", padx=16, pady=(16, 8))

        self._crear_fila(
            contenedor,
            "seguimiento Automatico",
            "Activado",
            colores["verde"],
        )
        self._crear_fila(
            contenedor,
            "Deteccion de expositor",
            "YOLO",
        )
    
    def _crear_fila(self, parent, etiqueta, valor, color=None):
        fila = tk.Frame(parent, bg=colores["panel"])
        fila.pack(fill="x", pady=5)

        tk.Label(
            fila,
            text=etiqueta,
            bg=colores["panel"],
            fg=colores["texto_secundario"],
            font=("Segoe UI", 10),
        ).pack(side="left")

        badge = tk.Frame(fila, bg=colores["panel_secundario"])
        badge.pack(side="right")

        tk.Label(
            badge,
            text=valor,
            bg=colores["panel_secundario"],
            fg=color or colores["texto"],
            font=("Segoe UI", 9, "bold"),
        ).pack(padx=8, pady=3)

    def _crear_botones(self):
        contenedor = tk.Frame(self, bg=colores["panel"])
        contenedor.pack(side="bottom", fill="x", padx=16, pady=16)

        contenedor.grid_columnconfigure(0, weight=1)
        contenedor.grid_columnconfigure(1, weight=1)

        self.btn_iniciar = ttk.Button(
            contenedor,
            text="Iniciar seguimiento",
            style="Primario.TButton",
        )
        self.btn_iniciar.grid(row=0, column=0, sticky="ew", padx=(0, 6))

        self.btn_detener = ttk.Button(
            contenedor,
            text="Detener",
            style="Secundario.TButton",
        )
        self.btn_detener.grid(row=0, column=1, sticky="ew", padx=(6, 0))

    def set_activo(self, activo):
        self.btn_iniciar.configure(
            state="disable" if activo else "normal"
        )
        self.btn_detener.configure(
            state="normal" if activo else "disable"
        )