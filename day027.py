import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometers")

def click():
    mylabel3.config(text = int(myinput.get()) * 1.609)


myinput = tkinter.Entry(width=5)
myinput.grid(column=1,row=0)

mylabel1 = tkinter.Label(text="Miles")
mylabel1.grid(column=2,row=0)

mylabel2 = tkinter.Label(text="is equal to")
mylabel2.grid(column=0,row=1)

mylabel3 = tkinter.Label(text=0)
mylabel3.grid(column=1,row=1)

mylabel4 = tkinter.Label(text="km")
mylabel4.grid(column=2,row=1)

mybutton1 = tkinter.Button(text = "Calculate", command=click)
mybutton1.grid(column=1,row=2)






window.mainloop()


