from tkinter import *

def convert():
    miles = float(entry.get())
    km = miles*1.609
    label_number.config(text=f"{km}")


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.grid(row=0, column=1)

label_miles = Label(text="miles")
label_miles.grid(row=0, column=2)

label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_number = Label(text=0)
label_number.grid(row=1, column=1)

label_km = Label(text="km")
label_km.grid(row=1, column=2)

button = Button(text="Convert", command=convert)
button.grid(row=2, column=1)





window.mainloop()