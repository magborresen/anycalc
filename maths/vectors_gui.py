import tkinter as tk
from main_gui import StartPage
import matplotlib
import pandas as pd
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import sympy as sym
sym.init_printing()


TITLE_FONT = ("Verdana", 20, "bold")


def advanced(df2):
    top_frame = tk.Frame()
    top_frame.columnconfigure(0, weight=1)
    top_frame.grid(row=0, column=0)
    bottom_frame = tk.Frame()
    bottom_frame.columnconfigure(0, weight=1)
    bottom_frame.grid(row=1, column=0)

    top_label = tk.Label(top_frame, text="Advanced Vector Calculation",
                         font=TITLE_FONT)
    top_label.pack()

    vec_one_entry = tk.Entry(top_frame, width=5)
    vec_one_entry.pack()
    vec_two_entry = tk.Entry(top_frame, width=5)
    vec_two_entry.pack()

    for name in df2.index:
        if df2.at['Name'] == vec_one_entry:
            vec_one = df2.loc[name]['Calculated Vector']
        elif df2.at['Name'] == vec_two_entry:
            vec_two = df2.loc[name]['Calculated Vector']
        else:
            pass

    dot_product = np.dot(vec_one, vec_two)
    dot_label = tk.Label(bottom_frame, text=str(dot_product))
    dot_label.pack(side=tk.LEFT)


class VectorsTwoPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.columnconfigure(0, weight=1)
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row=0, column=0)
        self.top_frame.columnconfigure(0, weight=1)
        self.mid_frame = tk.Frame(self)
        self.mid_frame.grid(row=1, column=0)
        self.mid_frame.columnconfigure(0, weight=1)
        bottom_frame = tk.Frame(self)
        bottom_frame.grid(row=2, column=0)
        bottom_frame.columnconfigure(0, weight=1)

        label = tk.Label(self.top_frame, text="Vectors In 2D Basics",
                         font=TITLE_FONT)
        label.pack(pady=10)

        back_button = tk.Button(self.top_frame, text="Back",
                                command=lambda: master.switch_frame(
                                 StartPage))
        back_button.pack(side=tk.TOP)

        reset_button = tk.Button(self.top_frame, text="Reset",
                                 command=lambda: self.reset_figure())
        reset_button.pack(side=tk.RIGHT)

        point_entry_label = tk.Label(self.top_frame, text='Enter a point:')
        point_entry_label.pack(side=tk.LEFT)

        self.vector_label_text = 65
        self.vector_label = tk.Label(self.top_frame,
                                     text=chr(self.vector_label_text) + " =")
        self.vector_label.pack(side=tk.LEFT)

        self.point_entry = tk.Entry(self.top_frame, width=20)
        self.point_entry.pack(side=tk.LEFT)

        self.ax = plt.axes()
        self.fig = plt.figure(1)
        self.ax.set_ylabel('y')
        self.ax.set_xlabel('x')

        add_point_btn = tk.Button(self.top_frame, text="Add Point",
                                  command=lambda: [self.get_points(self.ax,
                                                                   self.point_entry),
                                                   self.clear_text()
                                                   ])
        add_point_btn.pack(side=tk.LEFT)

        calc_vectors_btn = tk.Button(self.top_frame, text="Calculate Vectors",
                                     command=lambda: [self.calc_vectors(),
                                                      self.show_vectors()])
        calc_vectors_btn.pack(side=tk.RIGHT)

        advanced_button = tk.Button(self.top_frame, text="Advanced",
                                    command=lambda: advanced(self.df2))
        advanced_button.pack(side=tk.RIGHT)

        self.canvas = FigureCanvasTkAgg(self.fig, master=bottom_frame)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM,
                                         fill=tk.BOTH,
                                         expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, bottom_frame)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.df = pd.DataFrame(columns=['Vector', 'x', 'y'])

        self.df2 = pd.DataFrame(columns=['Name',
                                         'Calculated Vector',
                                         'Origin'])

    def reset_figure(self):
        self.ax.clear()
        self.canvas.draw()

        self.vector_label_text = 65
        self.vector_label['text'] = chr(self.vector_label_text) + " ="

        self.df = self.df.iloc[0:0]
        self.df2 = self.df2.iloc[0:0]

        self.calc_vector_label['text'] = ""

    def clear_text(self):
        self.point_entry.delete(0, 'end')

    def calc_vectors(self):

        for index, row in self.df.iterrows():
            if len(self.df.index) > 2:
                if index < len(self.df.index)-1:
                    index_one = self.df.loc[index]
                    index_two = self.df.loc[index+1]
                    vector_name = index_one['Vector'] + index_two['Vector']
                    new_vector = np.array([index_two['x'] - index_one['x'],
                                          index_two['y'] - index_one['y']])
                    origin = np.array([index_one['x'], index_one['y']])
                else:
                    index_one = self.df.loc[index]
                    index_two = self.df.loc[index-len(self.df.index)+1]
                    vector_name = index_one['Vector'] + index_two['Vector']
                    new_vector = np.array([index_two['x'] - index_one['x'],
                                          index_two['y'] - index_one['y']])
                    origin = np.array([index_one['x'], index_one['y']])
            else:
                if index < 1:
                    index_one = self.df.loc[index]
                    index_two = self.df.loc[index+1]
                    vector_name = index_one['Vector'] + index_two['Vector']
                    new_vector = np.array([index_two['x'] - index_one['x'],
                                          index_two['y'] - index_one['y']])
                    origin = np.array([index_one['x'], index_one['y']])
                else:
                    break

            self.df2 = self.df2.append({'Name': vector_name,
                                        'Calculated Vector': new_vector,
                                        'Origin': origin},
                                       ignore_index=True)

        for i in self.df2.index:
            name = self.df2.at[i, 'Name']
            vector = self.df2.at[i, 'Calculated Vector']
            self.calc_vector_label = tk.Label(self.mid_frame,
                                              text="{} = {}".format(name, vector))
            self.calc_vector_label.pack(side=tk.LEFT)

    def show_vectors(self):

        for v in self.df2.index:
            origin = self.df2.at[v, 'Origin']
            vector = self.df2.at[v, 'Calculated Vector']
            name = self.df2.at[v, 'Name']
            print ("Origin = %s %s" % (origin[0], origin[1]))
            print ("Vector = %s %s" % (vector[0], vector[1]))
            self.ax.quiver(origin[0], origin[1], vector[0], vector[1],
                           angles='xy', units='xy', scale=1)


    def refresh_figure(self, x, y):

        xmin, xmax = plt.xlim()
        ymin, ymax = plt.ylim()

        if xmax < x or ymax < y:
            plt.xlim(0, x+5)
            plt.ylim(0, y+5)
        else:
            pass
        plt.plot(x, y, 'ro')
        self.df = self.df.append({'Vector': self.vector_label['text'][0],
                                  'x': x, 'y': y}, ignore_index=True)
        self.canvas.draw()
        self.vector_label_text += 1
        self.vector_label['text'] = chr(self.vector_label_text) + " ="

    def get_points(self, ax1, point_entry):
        points = point_entry.get()

        if len(points) > 0:
            new_list = []
            xs = []
            ys = []

            for p in points:
                if p.isdigit():
                    new_list.append(int(p))

            xs.append(new_list[0])
            ys.append(new_list[-1])

            np_x = np.array(xs)
            np_y = np.array(ys)
            self.refresh_figure(np_x, np_y)
        else:
            pass
