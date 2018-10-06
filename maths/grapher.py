import tkinter as tk
import main_gui
import matplotlib
import pandas as pd
import numpy as np
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import sympy
sympy.init_printing(use_unicode=True)

TITLE_FONT = ("Verdana", 20, "bold")


class GraphPlot(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.columnconfigure(0, weight=1)
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row=0, column=0)
        self.top_frame.columnconfigure(0, weight=1)
        self.mid_frame = tk.Frame(self)
        self.mid_frame.grid(row=1, column=0)
        self.mid_frame.columnconfigure(0, weight=1)
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.grid(row=2, column=0)
        self.bottom_frame.columnconfigure(0, weight=1)

        self.ax = plt.axes()
        self.fig = plt.figure(1)
        self.ax.set_ylabel('y')
        self.ax.set_xlabel('x')

        label = tk.Label(self.top_frame, text="Graph Plotter", font=TITLE_FONT)
        label.pack(pady=10)

        back_button = tk.Button(self.top_frame, text="Back",
                                command=lambda: master.switch_frame(
                                 main_gui.StartPage))
        back_button.pack(side=tk.TOP)

        function_entry_label = tk.Label(self.top_frame, text="Enter Function:")
        function_entry_label.pack(side=tk.LEFT)

        self.func_entry = tk.Entry(self.top_frame, width=20)
        self.func_entry.pack(side=tk.LEFT)
        self.func_entry.insert(0, 'Ex. f(x)=x+2')

        plot_button = tk.Button(self.top_frame, text="Plot",
                                command=lambda: self.get_func(self.func_entry))
        plot_button.pack(side=tk.LEFT)

        diff_button = tk.Button(self.top_frame, text="Differentiate",
                                command=lambda: self.diff_func(
                                 self.func_entry, range(-10, 10)))
        diff_button.pack(side=tk.LEFT)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.bottom_frame)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM,
                                         fill=tk.BOTH,
                                         expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.bottom_frame)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def get_func(self, func):
        get_function = func.get()
        function_name = get_function[0:3]
        function_expression = get_function[5:]
        self.plot_graph(function_expression, function_name, range(-10, 10))

    def plot_graph(self, func, func_name, x_range):
        x = np.array(x_range)
        y = eval(func)
        plt.plot(x, y, label=func_name)
        self.canvas.draw()

    def diff_func(self, func, x_range):
        func_var = func.get()[2]
        function_expression = func.get()[5:]
        x = np.array(x_range)
        sym = str(sympy.diff(function_expression, func_var))
        y = eval(sym)
        plt.plot(x, y)
        self.canvas.draw()
