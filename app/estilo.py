import tkinter as tk
from tkinter import ttk

# colores principales para la app
colores = {
    "fondo": "#0B1120",
    "panel": "#111B2E",
    "panel_secundario": "#17243A",
    "panel_hover": "#2563EB",
    "azul": "#3B82F6",
    "azul_hover": "#2563EB",
    "verde": "#22C55E",
    "rojo": "#EF4444",
    "amarrillo": "#F59E0B",
    "texto": "#F1F5F9",
    "texto_secundario": "#94A3B8",
    "borde": "#26354D",
    "video_fondo": "#050A12",
}

fuentes = {
    "titulo": ("Segoe UI", 20, "bold"),
    "subtitulo": ("Segoe UI", 14, "bold"),
    "cuerpo": ("Segoe UI", 11),
    "pequeño": ("Segoe UI", 9),
    "boton": ("Segoe UI", 10, "bold")
}

dimensiones = {
    "sidebar_ancho": 230,
    "padding": 16,
    "padding_chico": 8,
    "radio": 12,
    "preview_radio": 16 / 9,
}

def aplicar_estilo(root):
    estilo = ttk.Style(root)
    estilo.theme_use("clam")

    root.configure(bg=colores["fondo"])

    # frames
    estilo.configure(
        "TFrame", 
        background=colores["fondo"]
    )
    estilo.configure(
        "panel.TFrame", 
        background=colores["panel"]
    )
    estilo.configure(
        "PanelSecundario.TFrame",
        background=colores["panel_secundario"]
    )

    # labels
    estilo.configure(
        "TLabel",
        background=colores["fondo"],
        foreground=colores["texto"],
        font=fuentes["cuerpo"],
    )
    estilo.configure(
        "Titulo.TLabel",
        background=colores["fondo"],
        fareground=colores["texto"],
        font=fuentes["cuerpo"],
    )
    estilo.configure(
        "subtitulo.TLabel",
        background=colores["fondo"],
        fareground=colores["texto"],
        font=fuentes["cuerpo"],
    )
    estilo.configure(
        "Secundario.TLabel",
        background=colores["fondo"],
        fareground=colores["texto_secundario"],
        font=fuentes["pequeño"],
    )
    estilo.configure(
        "Panel.TLabel",
        background=colores["panel"],
        foreground=colores["texto"],
        font=fuentes["cuerpo"],
    )
    estilo.configure(
        "PanelSecundario.TLabel",
        background=colores["panel_secundario"],
        foreground=colores["texto"],
        font=fuentes["cuerpo"]
    )

    # botones
    estilo.configure(
        "Primario.TButton",
        background=colores["azul"],
        foreground=colores["texto"],
        font=fuentes["boton"],
        borderwidth=0,
        relief="flat",
        padding=(16,10),
    )
    estilo.map(
        "Primario.TButton",
        background=[
            ("active", colores["azul_hover"]),
            ("disabled", colores["panel_secundario"]),
        ],
        foreground=[(
            "disabled",
            colores["texto_secundario"]
        )],
    )
    estilo.configure(
        "Secundario.TButton",
        background=colores["panel_secundario"],
        fareground=colores["texto"],
        font=fuentes["boton"],
        borderwidth=0,
        relief="flat",
        padding=(16, 10),
    )
    estilo.map(
        "Secundario.TButton",
        background=[(
            "active",
            colores["panel_hover"]
        )],
        fareground=[(
            "disabled",
            colores["texto_secundario"],
        )]
    )

    return estilo