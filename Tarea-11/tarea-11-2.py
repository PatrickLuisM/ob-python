import tkinter as tk


window = tk.Tk()
lista = ["Rap", "Rock","Jazz","Lofi","Electro","Pop"]

listbox = tk.Listbox(window)
label = tk.Label(text="Lista de generos musicales")
label.pack()
for item in lista:
 listbox.insert(tk.END, item)
listbox.pack()


window.mainloop()