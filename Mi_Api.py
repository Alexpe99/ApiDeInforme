
#https://www.youtube.com/watch?v=E3TmQKHtqjE&ab_channel=VladimirGuajardoGonzalez
#Creacion de una API

from cgitb import text
from sre_parse import expand_template
from textwrap import fill
from tkinter import Button, Frame, font
from tkinter.messagebox import YES
from turtle import width
from types import FrameType
from typing_extensions import Self
from _Tkinter import ttk
from Tekinter import *

class Cliente:
    def __init__(self, root):
        self.wind = root
        self.wind.title("Cliente")
        self.wind.geometry("850x600")
        self.wind.config(bg= "teal")

            frame1 =LabelFrame(self.wid, text="Datos del Cliente", font=("Calibri"14))
                frame2 =LabelFrame(self.wid, text="Información del Cliente", font=("Calibri"14))

        Frame1.pack(fill="both", expand= "yes", padx=20, pady=15)
            frame2.pack(fill="both", expand= "yes", padx=20, pady=15)

            lbl1 = labe(frame1, text="ID Cliente", width=20)
        lbl1.grid(row=0, column=0, padx=5, pady=3)
                self.ent1 = entry (frame1)
                   self.ent1.grid (row=0, column=0, padx=5, pady=3)

        lbl2 = labe(frame1, text="ID Cliente", width=20)
            lbl2.grid(row=0, column=0, padx=5, pady=3)
                self.ent2 = entry (frame1)
                    self.ent2.grid (row=0, column=0, padx=5, pady=3)

        lbl3 = labe(frame1, text="ID Cliente", width=20)
          lbl3.grid(row=0, column=0, padx=5, pady=3)
                self.ent3 = entry (frame1)
                  self.ent3.grid (row=0, column=0, padx=5, pady=3)

        lbl4 = labe(frame1, text="ID Cliente", width=20)
            lbl4.grid(row=0, column=0, padx=5, pady=3)
                self.ent4 = entry (frame1)
                    self.ent4.grid (row=0, column=0, padx=5, pady=3)

    btn1 = Button1 (frame1, text= "Agregar", with=12, height=2)
        btn1.grid (row=5, column=0, padx=10, pady=10)

    btn2 = Button1 (frame1, text= "Eliminar", with=12, height=2)
        btn2.grid (row=5, column=1, padx=10, pady=10)

    btn3 = Button1 (frame1, text= "Actualizar", with=12, height=2)
         btn3.grid (row=5, column=2, padx=10, pady=10)


        Self.trv = tkk.Treeview(frame2, colimns=(1,2,3,4), show="headings", height="15")

        Self.trv.heading(1, text= "ID Cliente")
        Self.trv.heading(2, text= "Nombre del Cliente")
        Self.trv.heading(3, text= "Apellido del Cliente")
        Self.trv.heading(4, text= "Dirección del Cliente")


    

if __name__ == "__naim__":
    root = Tk()
    Cliente = Cliente (root)
    root.mainloop

    