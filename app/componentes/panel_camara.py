import tkinter as tk
import cv2
from PIL import Image, ImageOps, ImageTk
from app.estilo import colores, dimensiones

class PanelCamara(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=colores["panel"])
        self.image_tk = None
        self._crear_area_video()

    def _crear_area_video(self):
        self.area_video = tk.Frame(self, bg=colores["video_fondo"])
        self.area_video.place(
            relx=0.5, 
            rely=0.5, 
            anchor="center"
        )

        self.video_label = tk.Label(self.area_video, bg=colores["video_fondo"])
        self.video_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.bind("<Configure>", self._ajustar_ratio)
        self._crear_placeholder()

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
    
    def _crear_placeholder(self):
        self.placeholder = tk.Frame(self.area_video, bg=colores["video_fondo"])
        self.placeholder.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            self.placeholder,
            text="▶",
            bg=colores["video_fondo"],
            fg=colores["texto_secundario"],
            font=("Segoe UI", 28),
        ).pack()

        tk.Label(
            self.placeholder,
            text="vista previa del seguimiento",
            bg=colores["video_fondo"],
            fg=colores["texto"],
            font=("Segoe UI", 12, "bold"),
        ).pack(pady=(8, 0))

        tk.Label(
            self.placeholder,
            text="video en tiempo real",
            bg=colores["video_fondo"],
            fg=colores["texto_secundario"],
            font=("Segoe UI", 9),
        ).pack(pady=(2, 0))

    def mostrar_frame(self, frame):
        ancho = self.area_video.winfo_width()
        alto = self.area_video.winfo_height()

        if ancho < 2 or alto < 2:
            return

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imagen = Image.fromarray(rgb)
        imagen = ImageOps.fit(imagen, (ancho, alto), Image.LANCZOS)

        self.image_tk = ImageTk.PhotoImage(imagen)
        self.video_label.configure(image=self.image_tk)

        if self.placeholder.winfo_ismapped():
            self.placeholder.place_forget