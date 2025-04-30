import tkinter

window = tkinter.Tk()
window.title("My First Tkinter GUI program")
window.minsize(width=500, height=500)

my_label = tkinter.Label(text="I am a label", font=("Arial", 11, "bold"))
my_label.pack()

window.mainloop()