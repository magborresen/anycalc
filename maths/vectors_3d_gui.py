import tkinter as tk
import main_gui
import matplotlib
import pandas as pd
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


TITLE_FONT = ("Verdana", 20, "bold")

class VectorsThreePage(tk.Frame):

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

        title_label = tk.Label(self.top_frame, text="Vectors In 3D Basics",
                               font=TITLE_FONT)
        title_label.pack(side=tk.TOP)

        back_button = tk.Button(self.top_frame, text="Back",
                                command=lambda:
                                master.switch_frame(main_gui.StartPage))
        back_button.pack(side=tk.TOP)

        reset_button = tk.Button(self.top_frame, text="Reset",
                                 command=lambda: self.reset())
        reset_button.pack(side=tk.RIGHT)

        point_entry_label = tk.Label(self.top_frame, text="Enter a point: ")
        point_entry_label.pack(side=tk.LEFT)

        self.vector_label_text = 65
        self.vector_label = tk.Label(self.top_frame,
                                     text=chr(self.vector_label_text) + " =")
        self.vector_label.pack(side=tk.LEFT)

        self.point_entry = tk.Entry(self.top_frame, width=20)
        self.point_entry.pack(side=tk.LEFT)

        add_point_btn = tk.Button(self.top_frame, text="Add Point",
                                  command=lambda:
                                  [self.get_points(self.ax,
                                   self.point_entry),
                                   self.clear_text()])
        add_point_btn.pack(side=tk.LEFT)

        calc_vectors_btn = tk.Button(self.top_frame, text="Calculate Vectors",
                                     command=lambda:
                                     [self.calc_vectors(),
                                      self.show_vectors()])
        calc_vectors_btn.pack(side=tk.LEFT)

        self.fig = plt.figure(1)
        self.ax = plt.axes(projection="3d")
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.bottom_frame)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM,
                                         fill=tk.BOTH,
                                         expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.bottom_frame)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.df = pd.DataFrame(columns=['Vector', 'a', 'b', 'c'])

        self.df2 = pd.DataFrame(columns=['Name', 'Calculated Vector', 'Origin'])

    def get_points(self, ax1, point_entry):
        points = point_entry.get()

        if len(points) > 0:
            new_list = []
            xs = []
            ys = []
            zs = []

            for p in points:
                if p.isdigit():
                    new_list.append(int(p))

            xs.append(new_list[0])
            ys.append(new_list[1])
            zs.append(new_list[2])

            np_x = np.array(xs)
            np_y = np.array(ys)
            np_z = np.array(zs)
            self.refresh_figure(np_x, np_y, np_z)
        else:
            pass

    def refresh_figure(self, x, y, z):

        xmin, xmax = self.ax.get_xlim()
        ymin, ymax = self.ax.get_ylim()
        zmin, zmax = self.ax.get_zlim()

        if xmax < x or ymax < y or zmax < z:
            self.ax.set_xlim(0, x+5)
            self.ax.set_ylim(0, y+5)
            self.ax.set_zlim(0, z+5)
        else:
            pass
        plt.plot(x, y, z, 'ro')
        self.df = self.df.append({'Vector': self.vector_label['text'][0],
                                  'x': x, 'y': y, 'z': z},
                                 ignore_index=True)
        self.canvas.draw()
        self.vector_label_text += 1
        self.vector_label['text'] = chr(self.vector_label_text) + " ="

    def calc_vectors(self):

        for index, row in self.df.iterrows():
            if len(self.df.index) > 2:
                if index < len(self.df.index)-1:
                    index_one = self.df.loc[index]
                    index_two = self.df.loc[index+1]
                    vector_name = index_one['Vector'] + index_two['Vector']
                    new_vector = np.array([index_two['x'] - index_one['x'],
                                           index_two['y'] - index_one['y'],
                                           index_two['z'] - index_one['z']])
                    origin = np.array([index_one['x'],
                                       index_one['y'],
                                       index_one['z']])
                else:
                    index_one = self.df.loc[index]
                    index_two = self.df.loc[index-len(self.df.index)+1]
                    vector_name = index_one['Vector'] + index_two['Vector']
                    new_vector = np.array([index_two['x'] - index_one['x'],
                                           index_two['y'] - index_one['y'],
                                           index_two['z'] - index_one['z']])
                    origin = np.array([index_one['x'],
                                       index_one['y'],
                                       index_one['z']])
            else:
                if index < 1:
                    index_one = self.df.loc[index]
                    index_two = self.df.loc[index+1]
                    vector_name = index_one['Vector'] + index_two['Vector']
                    new_vector = np.array([index_two['x'] - index_one['x'],
                                           index_two['y'] - index_one['y'],
                                           index_two['z'] - index_one['z']])
                    origin = np.array([index_one['x'],
                                       index_one['y'],
                                       index_one['z']])
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
                                              text="{} = {}".format(name,
                                                                    vector))
            self.calc_vector_label.pack(side=tk.LEFT)

    def show_vectors(self):

        for v in self.df2.index:
            origin = self.df2.at[v, 'Origin']
            vector = self.df2.at[v, 'Calculated Vector']
            name = self.df2.at[v, 'Name']
            self.ax.quiver(origin[0], origin[1], origin[2],
                           vector[0], vector[1], vector[2],
                           arrow_length_ratio=0.15)

    def clear_text(self):
        self.point_entry.delete(0, 'end')

    def reset(self):

        self.ax.clear()
        self.canvas.draw()

        self.vector_label_text = 65
        self.vector_label['text'] = chr(self.vector_label_text) + " ="

        self.df = self.df.iloc[0:0]
        self.df2 = self.df2.iloc[0:0]

        self.calc_vector_label['text'] = ""
