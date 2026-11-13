import tkinter as tk
from tkinter import ttk
from app.estilo import colores, dimensiones
from app.componentes.sidebar import Sidebar


class PresenterAI:
    def __init__(self, root):
        self.root = root
        self._configurar_ventana()
        self._construir_layout()

    def _configurar_ventana(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def _construir_layout(self):
        self.main_container = ttk.Frame(
            self.root,
            style="TFrame"
        )
        self.main_container.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.main_container.grid_rowconfigure(1, weight=1)
        self.main_container.grid_columnconfigure(1, weight=1)

        self._crear_sidebar()
        self._crear_encabezado()
        self._crear_cuerpo()

    def _crear_sidebar(self):
        self.sidebar = Sidebar(
            self.main_container
        )
        self.sidebar.grid(
            row=0, 
            column=0, 
            rowspan=2, 
            sticky="ns"
        )
        self.sidebar.grid_propagate(False)

        tk.Label(
            self.sidebar,
            text="SIDEBAR",
            bg=colores["panel"],
            fg=colores["texto"],
            font=("Segoe UI", 12, "bold"),
        ).pack(pady=24)

    def _crear_encabezado(self):
        self.encabezado = ttk.Frame(
            self.main_container,
            style="panel.TFrame"
        )
        self.encabezado.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=dimensiones["padding"],
            pady=(dimensiones["padding"], 0),
        )
        self.encabezado.grid_columnconfigure(0, weight=1)

        ttk.Label(
            self.encabezado,
            text="ENCABEZADO",
            style="Panel.TLabel",
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=14,
            pady=14
        )

    def _crear_cuerpo(self):
        self.cuerpo = ttk.Frame(
            self.main_container,
            style="TFrame"
        )
        self.cuerpo.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=dimensiones["padding"],
            pady=dimensiones["padding"],
        )
        self.cuerpo.grid_rowconfigure(0, weight=1)
        self.cuerpo.grid_columnconfigure(0, weight=3)
        self.cuerpo.grid_columnconfigure(1, weight=2)

        self.panel_camara = ttk.Frame(
            self.cuerpo,
            style="panel.TFrame"
        )
        self.panel_camara.grid(
            row=0, 
            column=0,
            sticky="nsew",
            padx=(0,8)
        )
        ttk.Label(
            self.panel_camara,
            text="PANEL CAMARA",
            style="Panel.TLabel",
        ).pack(expand=True)

        self.panel_configuracion = ttk.Frame(
            self.cuerpo,
            style="panel.TFrame"                
        )
        self.panel_configuracion.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(8,0)
        )
        ttk.Label(
            self.panel_configuracion,
            text="PANEL CONFIGURACION",
            style="Panel.TLabel",
        ).pack(expand=True)




    