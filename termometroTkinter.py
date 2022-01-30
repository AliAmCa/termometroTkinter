from tkinter import *
from tkinter import ttk


class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Termómetro")
        self.geometry("200x150")
        self.configure(bg="#ECECEC")
        self.resizable(0,0)
        self.temperatura = StringVar(value="")
        self.tipoUnidad = StringVar(value = "C")
        
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self,textvariable=self.temperatura).place(x=5,y=10)
        
        self.lblUnidad = ttk.Label(self, text="Grados:").place(x=10, y=50)
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable = self.tipoUnidad, value ="F").place(x=40, y= 70)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable = self.tipoUnidad, value ="C").place(x=40, y= 90)
        
    def start(self):
        self.mainloop()
        




if __name__ == '__main__':
    
    app= mainApp()
    app.start()