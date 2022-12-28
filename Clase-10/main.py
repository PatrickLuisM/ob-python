import tkinter

window = tkinter.Tk()


label_saludo = tkinter.Label(window,text="hola",bg="green",fg="black")
label_saludo.pack(ipadx=50,ipady=50,fill="both")


label_adios = tkinter.Label(window,text="Adios",bg="pink",fg="black")
label_adios.pack(ipadx=50,ipady=50)


window.mainloop()