import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        estaciones = self.combobox_estaciones.get()
        precio = self.combobox_destino.get()
        
        match estaciones, precio:
            case ("Verano", "Bariloche"): 
                precio_1 = int(15000 * 20/100)
                precio_final = int(15000 - precio_1)
                mensaje = f"en Verano Bariloche cuenta con un precio de {precio_final}"
        
            case ("Invierno", "Bariloche"):
                precio_2 = int(15000 * 20/100) 
                precio_final = int(15000 + precio_2)
                mensaje = f"en Verano Bariloche cuenta con un precio de {precio_final}"
            
            case ("Primavera", "Bariloche"):
                precio_3 = int(15000 * 10/100)
                precio_final = int(15000 + precio_3)    
                mensaje = f"en primavera Bariloche cuenta con un precio de {precio_final}"
            
            case ("Otoño", "Bariloche"):
                precio_4 = int(15000 * 10/100)
                precio_final = int(15000 + precio_4)    
                mensaje = f"en otoño Bariloche cuebta con un precio de {precio_final}"
            
            case ("Verano", "Mar del plata"): 
                precio_1 = int(15000 * 20/100)
                precio_final = int(15000 + precio_1)
                mensaje = f"en Verano Bariloche cuenta con un precio de {precio_final}"
            
            case ("Invierno", "Mar del plata"):
                precio_2 = int(15000 * 20/100) 
                precio_final = int(15000 - precio_2)
                mensaje = f"en Verano Bariloche cuenta con un precio de {precio_final}"
            
            case ("Primavera", "Mar del plata"):
                precio_3 = int(15000 * 10/100)
                precio_final = int(15000 + precio_3)    
                mensaje = f"en primavera Bariloche cuenta con un precio de {precio_final}"
            
            case ("Otoño", "Mar del plata"):
                precio_4 = int(15000 * 10/100)
                precio_final = int(15000 + precio_4)    
                mensaje = f"en Otoño Bariloche cuebta con un precio de {precio_final}"  
        
        alert ("costo", mensaje)          
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()