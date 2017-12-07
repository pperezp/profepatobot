# http://effbot.org/tkinterbook/grid.htm
# https://www.tutorialspoint.com/python/python_gui_programming.htm

# Eventos con bind()
# http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm

# ComboBox
# http://recursospython.com/guias-y-manuales/lista-desplegable-combobox-en-tkinter/

from tkinter import *
from tkinter import ttk
from model.bd.Data import Data

class Application(Frame):

    """
    El constructor no cambia (por ahora)
    """
    def __init__(self, master=None):
        self.tags = None
        self.data = Data()
        self.cont = 1
        self.lista = list()
        super().__init__(master)
        self.pack()
        self.init_components()

    def init_components(self):
        self.lbl1 = Label(self)
        self.lbl1["text"] = "URL:"
        self.lbl1.grid(row=0, column=0, padx=10)
        # padx = relleno hacia afuera en x

        self.lbl2 = Label(self)
        self.lbl2["text"] = "Tags:"
        self.lbl2.grid(row=1, column=0, padx=10)

        self.btn_generar = Button(self)
        self.btn_generar["text"] = "+"
        self.btn_generar.grid(row=1, column=1)
        self.btn_generar.bind("<Button-1>", self.evt_btn_generar)

        # Entry = TextBox
        self.txt_link = Entry(self)
        self.txt_link.grid(
            row=0,
            column=1 ,
            ipadx=100,# ipadx = Relleno interno en x (ver http://effbot.org/tkinterbook/grid.htm)
            pady=10,  # pady = Relleno externo en y  (ver http://effbot.org/tkinterbook/grid.htm)
            padx=10
        )
        self.txt_link.bind("<Return>", self.evt_txt_link) # Evento enter (Alucinante!)

        self.btn_guardar = Button(self)
        self.btn_guardar["text"] = "Registrar"
        self.btn_guardar.grid(row=2, column=1, ipadx=70)
        self.btn_guardar.bind("<Button-1>", self.evt_btn_guardar)

    def evt_btn_guardar(self, evt):
        tags = list()

        for c in self.lista:
            selected_index = c.current()
            tag = self.tags[selected_index]
            tags.append(tag)

        link = self.txt_link.get()

        self.data.crear_link(link, tags)

    def evt_btn_generar(self, evt):
        self.cont = self.cont + 1
        cbo = ttk.Combobox(self, state="readonly")

        if self.tags is None:
            self.tags = self.data.get_tags()

        cbo["values"] = self.tags

        cbo.grid(row=self.cont, column=1)
        #cbo.current(0)

        self.lista.append(cbo)

        self.btn_guardar.grid(row=self.cont+1, column=1, ipadx=70)

    def evt_cbo(self, evt):
        print(evt)


    def evt_txt_link(self, evt):
        print(evt)
        print(self.txt_link.get())

root = Tk()
app = Application(master=root)
app.mainloop()