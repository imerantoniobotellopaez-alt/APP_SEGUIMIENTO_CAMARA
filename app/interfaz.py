import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

class PresenterAI:
    def __init__(self, root):
        self.root = root
        self.root.title("Seguimiento camara")
        self.root.geometry("1620x720")

        self.camera = None
        self.running = False
        self.image_tk = None

        # interfaz
        self.title_label = ttk.Label(
            root,
            text="Seguimiento Camara",
            font=("Arial", 22, "bold")
        )
        self.title_label.pack(pady=15)

        #Area de la camara
        self.video_label = ttk.Label(root)
        self.video_label.pack(pady=10)

        #Botones
        self.btn_start = ttk.Button(
            root,
            text="Iniciar Camara",
            command=self.start_camera
        )
        self.btn_start.pack(pady=5)
        self.btn_stop = ttk.Button(
            root,
            text="Detener Camara",
            command=self.stop_camera
        )
        self.btn_stop.pack(pady=5)

        # Estado
        self.status_label = ttk.Label(
            root,
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
                text="Conectado, pero sin recibir video"
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
    



if __name__ == "__main__":
    root = tk.Tk()
    app = PresenterAI(root)
    root.mainloop()

