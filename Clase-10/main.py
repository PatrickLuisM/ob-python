from tkinter import ttk
import tkinter

window = tkinter.Tk()


# label_saludo = tkinter.Label(window,text="hola",bg="green",fg="black")
# label_saludo.pack(ipadx=50,ipady=50,fill="both")


# label_adios = tkinter.Label(window,text="Adios",bg="pink",fg="black")
# label_adios.pack(ipadx=50,ipady=50)

window.columnconfigure(0,weight=1)
window.columnconfigure(0,weight=3)

username_label = ttk.Label(window, text="Username:")
username_label.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1,row=0,sticky=tkinter.W,padx=5,pady=5)

password_label = ttk.Label(window, text="Password:")
password_label.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

password_entry = ttk.Entry(window,show='*')
password_entry.grid(column=1,row=1,sticky=tkinter.W,padx=5,pady=5)

##Boton

login_button = ttk.Button(window,text="Login")
login_button.grid(column=1,row=3,sticky=tkinter.E,padx=5,pady=5)


window.mainloop()