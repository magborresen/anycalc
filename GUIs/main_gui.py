import tkinter as tk
import sys
sys.path.insert(0, '/Users/magnusborresen/formulapy/maths')
import vectors_gui
import vectors_3d_gui
import grapher


TITLE_FONT = ("Verdana", 20, "bold")


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "AnyGrapher")

        container = tk.Frame(self)
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        #  Destroys the old frame and packs new frame  #
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)


class StartPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Welcome to AnyGrapher",
                         font=TITLE_FONT)
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Vectors in 2D",
                            command=lambda: master.switch_frame(
                                vectors_gui.VectorsTwoPage))
        button1.pack(fill="x")

        button2 = tk.Button(self, text="Vectors in 3D",
                            command=lambda: master.switch_frame(
                                vectors_3d_gui.VectorsThreePage))
        button2.pack(fill="x")

        button3 = tk.Button(self, text="Plot A Graph",
                            command=lambda: master.switch_frame(
                                grapher.GraphPlot))
        button3.pack(fill='x')


if __name__ == '__main__':
    app = Window()
    app.resizable(False, False)
    app.mainloop()
