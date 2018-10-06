import tkinter as tk
import main_gui
import math.vectors_gui


TITLE_FONT = ("Verdana", 20, "bold")


class VectorsTwoPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Vectors in 2D", font=TITLE_FONT)
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Basics",
                            command=lambda: master.switch_frame(
                             math_guis.vectors_gui.BasicsPage))
        button1.pack(fill="x")

        button2 = tk.Button(self, text="Dot Product",
                            command=lambda: master.switch_frame(DotPage))
        button2.pack(fill="x")

        button3 = tk.Button(self, text="Scalar Product",
                            command=lambda: master.switch_frame(ScalarPage))
        button3.pack(fill="x")

        button4 = tk.Button(self, text="Back",
                            command=lambda: master.switch_frame(main_gui.MathPage))
        button4.pack(fill="x")


class VectorsThreePage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Vectors in 3D", font=TITLE_FONT)
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Basics",
                            command=lambda: master.switch_frame(BasicsThreePage))
        button1.pack(fill="x")

        button2 = tk.Button(self, text="Back",
                            command=lambda: master.switch_frame(main_gui.MathPage))
        button2.pack(fill="x")
