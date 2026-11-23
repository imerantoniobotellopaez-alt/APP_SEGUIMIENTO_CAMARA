import tkinter as tk
from tkinter import ttk
from app.estilo import colores, dimensiones
from app.componentes.sidebar import Sidebar
from app.componentes.encabezado import Encabezado
from app.componentes.panel_camara import PanelCamara
from app.componentes.panel_configuracion import PanelConfiguracion
from logica.camera import Camera


class PresenterAI:
    def __init__(self, root):
        self.root = root
        self.camera = Camera()
        self.video_activo = False
        self._configurar_ventana()
        self._construir_layout()
        self._conectar_eventos()
        self.root.protocol("WM_DELETE_WINDOW", self._cerrar)

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

    def _crear_encabezado(self):
        self.encabezado = Encabezado(self.main_container,)
        self.encabezado.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=dimensiones["padding"],
            pady=(dimensiones["padding"], 0),
        )

    def _crear_cuerpo(self):
        self.cuerpo = ttk.Frame(self.main_container, style="TFrame")

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

        self.panel_camara = PanelCamara(self.cuerpo)
        self.panel_camara.grid(
            row=0, 
            column=0,
            sticky="nsew",
            padx=(0,8)
        )

        self.panel_configuracion = PanelConfiguracion(self.cuerpo)
        self.panel_configuracion.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(8, 0),     
        )

    def _conectar_eventos(self):
        self.panel_configuracion.btn_iniciar.configure(
            command=self._iniciar_video
        )
        self.panel_configuracion.btn_detener.configure(
            command=self._detener_video
        )

    def _iniciar_video(self):
        if self.video_activo:
            return

        if not self.camera.abrir():
            return

        self.video_activo = True
        self.encabezado.set_estado(True)
        self.panel_configuracion.set_activo(True)
        self._actualizar_video()

    def _detener_video(self):
        self.video_activo = False
        self.camera.cerrar()
        self.panel_camara.mostrar_placeholder()
        self.encabezado.set_estado(False)
        self.panel_configuracion.set_activo(False)

    def _actualizar_video(self):
        if not self.video_activo:
            return

        frame = self.camera.leer()
        if frame is not None:
            self.panel_camara.mostrar_frame(frame)

        self.root.after(30, self._actualizar_video)
    
    def _cerrar(self):
        self._detener_video()
        self.root.destroy()