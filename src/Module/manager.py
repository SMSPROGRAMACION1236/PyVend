import tkinter as tk
from Module.sign_frame import SighUpPage
from Module.frames_operations import OperationsFrames
from Module.container import Container



class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Caja Registradora PyVend")
        self.resizable(False, False)
        self.geometry("900x600")
        self.config(bg="#3ba336")
        self.container = tk.Frame(self, bg="#3ba336")
        self.container.pack(fill="both", expand=True)

        self.frames = {
            Container: None,
            OperationsFrames: None,
            SighUpPage: None
        }
        self.load_frames()
        self.show_frames(SighUpPage)

    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Ocupa todo el contenedor

    def show_frames(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

    def show_main_frame(self):
        self.show_frames(OperationsFrames)


def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()