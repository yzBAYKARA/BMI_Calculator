from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=225, height=225)

def calculator():
    kilo_input = entry.get()
    boy_input = entry2.get()

    if not kilo_input.strip() or not boy_input.strip():
        label3 = Label(text="Please enter both weight and height!")
        label3.grid(row=4, column=0, columnspan=2)
        return

    try:
        kilo = float(kilo_input)
        boy = float(boy_input)
    except ValueError:
        label3 = Label(text="Invalid input! Please enter numeric values.")
        label3.grid(row=4, column=0, columnspan=2)
        return

    if kilo <= 0 or boy <= 0:
        label3 = Label(text="Invalid input! Please enter positive values.")
        label3.grid(row=4, column=0, columnspan=2)
        return

    metreboy = boy / 100
    metrekare = metreboy * metreboy
    BMI = kilo / metrekare

    if BMI < 18.4:
        calculate = "Underweight"
    elif BMI < 24.9:
        calculate = "Normal"
    elif BMI < 39.9:
        calculate = "Overweight"
    else:
        calculate = "Obese"

    label3 = Label(text="Your BMI = {:.2f}. You are {}.".format(BMI, calculate))
    label3.grid(row=5, column=0, columnspan=2)

label = Label(text="Enter Your Weight (kg)")
label.grid(row=0, column=0, padx=10, pady=10)

entry = Entry(width=10)
entry.grid(row=0, column=1)

label2 = Label(text="Enter Your Height (cm)")
label2.grid(row=1, column=0)

entry2 = Entry(width=10)
entry2.grid(row=1, column=1)

button = Button(text="Calculate", command=calculator)
button.grid(row=2, column=0, columnspan=2, padx=4, pady=4)

window.mainloop()