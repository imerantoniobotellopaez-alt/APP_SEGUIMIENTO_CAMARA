import cv2

class Camera:
    def __init__(self, indice=0):
        self.indice = indice
        self.captura = None
            
    def abrir(self):
        if self.captura is not None:
            return True

        self.captura = cv2.VideoCapture(self.indice, cv2.CAP_ANY)
        if not self.captura.isOpened():
            self.captura.release()
            self.captura = None
            return False

        return True
    
    def leer(self):
        if self.captura is None:
            return None

        ok, frame = self.captura.read()
        if not ok or frame is None:
            return None

        return frame

    def cerrar(self):
        if self.captura is not None:
            self.captura.release()
            self.captura = None

    @property
    def abierta(self):
        return self.captura is not None