import tkinter as tk
import tkinter

window = tkinter.Tk()
portee = tk.IntVar()

tk.Label(window, 
         text="""Tu genero favorito:""",
         justify = tk.LEFT,
         padx = 20).pack()

def reset():
    gn1.deselect()
    gn2.deselect()
    gn3.deselect()
    gn4.deselect()



gn1=tk.Radiobutton(window, 
                   text="Rock",
                   padx = 20, 
                   variable= portee,
                   value=1).pack(anchor=tk.W)
gn2 =  tk.Radiobutton(window, 
                   text="Rap",
                   padx = 20, 
                   variable= portee, 
                   value=2).pack(anchor=tk.W)
gn3 =  tk.Radiobutton(window, 
                   text="Pop",
                   padx = 20, 
                   variable= portee, 
                   value=3).pack(anchor=tk.W)

gn4 =  tk.Radiobutton(window, 
                   text="Jazz",
                   padx = 20, 
                   variable= portee, 
                   value=4).pack(anchor=tk.W)




reset_button = tk.Button(window,text="Reseteo",padx=20,command=reset).pack()


window.mainloop()




