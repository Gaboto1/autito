import tkinter
def imprimir():
    print("Hola Mundo")
ventana = tkinter.Tk()
ventana.title("ejemplo de botones")
ventana.geometry("300x300")


etiqueta = tkinter.Label(ventana, text="Hola mundo")
etiqueta.grid(column=0, row=0)
entrada = tkinter.Entry(ventana)
entrada.grid(column=1, row=0)
etiqueta=tkinter.Label(ventana, text="¿que lenguajes de programacion conoces?")
etiqueta.grid(column=0, row=1)
lista=tkinter.Listbox(ventana)
lista.grid(column=1, row=1)
lista.insert(1, "Python")
lista.insert(2, "Java")
lista.insert(3, "C++")
boton = tkinter.Button(ventana, text="Aceptar", command=imprimir)
boton.grid(columnspan=2, row=2)
checkbox = tkinter.Checkbutton(ventana, text="Acepto los terminos y condiciones")
checkbox.grid(columnspan=2, row=3)
radio = tkinter.Radiobutton(ventana, text="Masculino")
radio.grid(column=0, row=4)
radio = tkinter.Radiobutton(ventana, text="Femenino")
radio.grid(column=1, row=4)

ventana.mainloop()






