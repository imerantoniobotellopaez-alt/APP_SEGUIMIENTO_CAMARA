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
        self._items = {}
        self._crear_logo()
        self._crear_navegacion()
        self._crear_pie()
        
    
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
            text="Presenter",
            bg=colores["panel"],
            fg=colores["texto"],
            font=("Segoe UI", 14, "bold"),
        ).pack(side="left", padx=(8, 0))

    def _crear_navegacion(self):
        items = [
            ("◉", "Inicio", True),
            ("▣", "Seguimiento", False),
            ("⚙", "Ajustes", False),
        ]
        for icono, texto, activo in items:
            self._crear_item(icono, texto, activo)

    def _crear_item(self, icono, texto, activo=False):
        fondo = colores["azul"] if activo else colores["panel"]
        color = colores["texto"] if activo else colores["texto_secundario"]

        fila = tk.Frame(
            self, 
            bg=fondo, 
            cursor="hand2"
        )
        fila.pack(
            fill="x", 
            padx=10, 
            pady=2
        )

        etiqueta_icono = tk.Label(
            fila,
            text=icono,
            bg=fondo,
            fg=color,
            font=("Segoe UI", 12),
        )
        etiqueta_icono.pack(
            side="left", 
            padx=(12, 10), 
            pady=10
        )

        etiqueta_texto = tk.Label(
            fila,
            text=texto,
            bg=fondo,
            fg=color,
            font=("Segoe UI", 11),
        )
        etiqueta_texto.pack(
            side="left"
        )     

        self._items[texto] = {
            "widgets": (
                fila, 
                etiqueta_icono,
                etiqueta_texto    
            ),
            "activo": activo,
        }

        for widget in (fila, etiqueta_icono, etiqueta_texto):
            widget.bind(
                "<Enter>",
                lambda evento, t=texto: self._resaltar(t, True),
            )
            widget.bind(
                "<Leave>",
                lambda evento, t=texto: self._resaltar(t, False)
            )

    def _resaltar(self, texto, encima):
        item = self._items[texto]

        if item["activo"]:
            return

        fondo = colores["panel_hover"] if encima else colores["panel"]
        for widget in item["widgets"]:
            widget.configure(bg=fondo)
        

    def _crear_pie(self):
        tk.Label(
            self,
            text="V0.1  Presenter",
            bg=colores["panel"],
            fg=colores["texto_secundario"],
            font=("Segoe UI", 9),
        ).pack(side="bottom", pady=(0,16))

        tk.Frame(
            self,
            bg=colores["borde"],
            height=1,
        ).pack(
            side="bottom", 
            fill="x", 
            padx=16, 
            pady=(0, 12)
        )