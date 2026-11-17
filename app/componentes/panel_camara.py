import tkinter as tk
from app.estilo import colores, dimensiones

class PanelCamara(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=colores["panel"])
        self._crear_area_video()

    def _crear_area_video(self):
        self.area_video = tk.Frame(self, bg=colores["video_fondo"])
        self.area_video.place(
            relx=0.5, 
            rely=0.5, 
            anchor="center"
        )

        self.bind("<Configure>", self._ajustar_ratio)

    def _ajustar_ratio(self, evento):
        margen = dimensiones["padding"]
        ancho_disponible = evento.width - margen * 2
        alto_disponible = evento.height - margen * 2

        if ancho_disponible <= 0 or alto_disponible <= 0:
            return

        ancho = ancho_disponible
        alto = ancho / dimensiones["preview_ratio"]

        if alto > alto_disponible:
            alto = alto_disponible
            ancho = alto * dimensiones["preview_ratio"]

        self.area_video.place_configure(
            width=int(ancho),
            height=int(alto),
        )