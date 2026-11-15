import ctypes
import tkinter as tk
from app.estilo import aplicar_estilo
from app.interfaz import PresenterAI

def activar_dpi():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(
            1
        )
    except Exception:
        pass

def main():
    activar_dpi()

    root = tk.Tk()
    root.title("Iglesia Emanuel")
    root.geometry("1440x860")
    root.minsize(1024, 640)
    aplicar_estilo(root)
    app = PresenterAI(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()