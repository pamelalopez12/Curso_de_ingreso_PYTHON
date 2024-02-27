import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt ("", "NUMERO INGRESADO")
        
        numero_1 = int(numero)
        
        numeros_divisibles = 0
        
        for contador in range(1,numero_1+1): 

            if numero_1 % contador == 0:
                
                print (contador)
                
                numeros_divisibles += 1
        
        print(numeros_divisibles)

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()