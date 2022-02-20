import tkinter as tk
from tkinter import *

class App:
    def __init__(self):

        ## NESSE CONTEXTO, O SELF SERVE PARA DOIS ELEMENTOS QUE SE PODEM TROCAR INFORMAÇÕES, 
        ## COMO UM EXEMPLO, UMA ENTRY QUE PEGA SEU PRÓPRIO VALOR APENAS SE O BOTÃO FOR PRESSIONADO.

        def start(self):
            self.window = tk.Tk()
            self.window.title('janela')
      
        def labels(self):
            initial = Label(self.window, text='Criado')
            initial.place(x=10, y=10)
        
        def entry(self):
            self.entry = Entry(self.window, bg='white', fg='black')
            self.entry.place(x=10, y=80)

        def buttons(self):
            def button_pressed():
                console = self.entry.get()
                print(console)

            btn = Button(self.window, command=button_pressed, text='enviar')
            btn.place(x=10, y= 40)

        def end(self):
            self.window.mainloop()

        start(self)  
        labels(self)
        entry(self)
        buttons(self)
        end(self)  


app = App()
