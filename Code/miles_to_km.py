import tkinter

window = tkinter.Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=500)

miles_entry = tkinter.Entry()
miles_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Arial", 11, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 11, "bold"))
is_equal_label.grid(column=0, row=1)

converted_km_label = tkinter.Label(text="0", font=("Arial", 11, "bold"))
converted_km_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 11, "bold"))
km_label.grid(column=2, row=1)

def calculate():
    miles_value = int(miles_entry.get())
    converted_km_label.config(text=miles_value * 1.60934) 

calculate_btn = tkinter.Button(text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=2)

window.mainloop()