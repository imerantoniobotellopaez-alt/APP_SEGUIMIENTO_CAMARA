self.root.title("Seguimiento camara")
self.root.geometry("1620x720")

self.camera = None
self.running = False
self.image_tk = None
# contenedor principal
self.main_container = tk.Frame(
    self.root, 
    bg=colores["fondo"]
)
self.main_container.pack(fill="both", expand=True)
self.Sidebar = sidebar(self.main_container)
self.Sidebar.pack(side="left", fill="y")

# Area principal
self.content = tk.Frame(
    self.main_container,
    bg=colores["fondo"]
)
self.content.pack(side="left", fill="both", expand=True)
    
# interfaz
self.title_label = ttk.Label(
    self.content,
    text="Seguimiento Camara",
    font=("Arial", 22, "bold")
)
self.title_label.pack(pady=15)

#Area de la camara
self.video_label = ttk.Label(self.content)
self.video_label.pack(pady=10)

#Botones
self.btn_start = ttk.Button(
    self.content,
    text="Iniciar Camara",
    command=self.start_camera
)
self.btn_start.pack(pady=5)
self.btn_stop = ttk.Button(
    self.content,
    text="Detener Camara",
    command=self.stop_camera
)
self.btn_stop.pack(pady=5)

# Estado
self.status_label = ttk.Label(
    self.content,
    text="Camara Detenida"
)
self.status_label.pack(pady=10)
self.root.protocol("WM_DELETE_WINDOW", self.close_app)

def start_camera(self):
    if self.running:
        return

self.camera = cv2.VideoCapture(0, cv2.CAP_ANY)

if not self.camera.isOpened():
    self.status_label.config(
        text="Error al iniciar camara"
    )
    self.camera.release()
    self.camera = None
    return

self.running = True
self.status_label.config(text="Camara activa")

self.update_frame()

def update_frame(self):
    if not self.running:
        return    
    
ret, frame = self.camera.read()  

if ret and frame is not None:
    # Convertr BGR A RGB

    frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Convertir a imagen compatible con tkinter
    image = Image.fromarray(frame)

    self.image_tk = ImageTk.PhotoImage(image)

    self.video_label.config(
        image=self.image_tk
    )

    self.status_label.config(
        text="Camara activa"
    )

else:
    self.status_label.config(
        text="No se recibio un frame valido"
    )

#actualizar cada 15ms
self.root.after(15, self.update_frame)

def stop_camera(self):
    self.running = False

if self.camera is not None:
    self.camera.release()
    self.camera = None
    
self.video_label.config(image="")
self.image_tk = None

self.status_label.config(
    text="Camara Detenida"
)

def close_app(self):
    self.stop_camera()
    self.root.destroy()

