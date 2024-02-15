import tkinter as tk
import numpy as np
import pandas as pd
from Predictor import Predictor

# Colors #
gray = "#363636"
lightBlue = "#0080FE"
white = "#FBFCF8"
darkBlue = "#0F52BA"

window = tk.Tk()

predictor = Predictor()

window.attributes("-fullscreen", True)

window.title("Glucose Predictor")

window.config(background="BLACK")

window.geometry("360x360")


def toggle_Screen(event):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))


def Reset():
    genderVar.set("Choose Gender Option")
    hyperVar.set("Choose Hypertension Option")
    diseaseVar.set("Choose Heart Disease Option")
    marriedVar.set("Choose Married Status Option")
    workVar.set("Choose Work Status Option")
    residenceVar.set("Choose Residence Status Option")
    strokeVar.set("Choose Stroke Status Option")

    ageLength = len(ageEntry.get())
    ageEntry.delete(0, ageLength)
    ageEntry.insert(0, "Enter Age Here:")

    bmiLength = len(bmiEntry.get())
    bmiEntry.delete(0, bmiLength)
    bmiEntry.insert(0, "Enter BMI Here:")

    status.config(text="Result: ")


def Submit():
    gender = genderVar.get()
    hyper = hyperVar.get()
    disease = diseaseVar.get()
    married = marriedVar.get()
    age = int(ageEntry.get())
    work = workVar.get()
    bmi = int(bmiEntry.get())
    residence = residenceVar.get()
    stroke = strokeVar.get()

    x_list = [gender, age, hyper, disease, married, work, residence, bmi, stroke]

    prediction = predictor.predict(x_list)[0][0]

    prediction = round(prediction, 2)

    if prediction < 0:
        prediction = "Try Again"

    string = "Result: " + str(prediction)

    status.config(text=string)


title = tk.Label(
    window,
    background=darkBlue,
    foreground=white,
    activebackground=lightBlue,
    activeforeground=white,
    highlightthickness=2,
    highlightcolor='WHITE',
    width=50,
    height=0,
    text="Glucose Predictor",
    font=("Arial", 35, "bold"))

title.grid(row=0, column=0)

# Gender Selector #
genderVar = tk.StringVar()
genderVar.set("Choose Gender Option")
gender_options = ["Male", "Female"]

gender_select = tk.OptionMenu(
    window,
    genderVar,
    *gender_options)

gender_select.config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 25),
    border=0,
    highlightthickness=1,
    highlightbackground=white,
    indicatoron=False
)

gender_select['menu'].config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 16),
    border=0,
    activeborder=2
)

gender_select.place(x=50, y=100)

# HyperTension Selector #
hyperVar = tk.StringVar()
hyperVar.set("Choose Hypertension Option")
hyper_options = ["Yes", "No"]

hypertension_select = tk.OptionMenu(
    window,
    hyperVar,
    *hyper_options)

hypertension_select.config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 25),
    border=0,
    highlightthickness=1,
    highlightbackground=white,
    indicatoron=False
)

hypertension_select['menu'].config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 16),
    border=0,
    activeborder=2
)

hypertension_select.place(x=50, y=190)

# Heart Disease Selector #
diseaseVar = tk.StringVar()
diseaseVar.set("Choose Heart Disease Option")
disease_options = ["Yes", "No"]

disease_selection = tk.OptionMenu(
    window,
    diseaseVar,
    *disease_options)

disease_selection.config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 25),
    border=0,
    highlightthickness=1,
    highlightbackground=white,
    indicatoron=False
)

disease_selection['menu'].config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 16),
    border=0,
    activeborder=2
)

disease_selection.place(x=50, y=340)

# Married Ever Selector #
marriedVar = tk.StringVar()
marriedVar.set("Choose Married Status Option")
married_options = ["Yes", "No"]

married_selection = tk.OptionMenu(
    window,
    marriedVar,
    *married_options)

married_selection.config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 25),
    border=0,
    highlightthickness=1,
    highlightbackground=white,
    indicatoron=False
)

married_selection['menu'].config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 16),
    border=0,
    activeborder=2
)

married_selection.place(x=50, y=490)

# Age Entry #
ageEntry = tk.Entry(window,
                    width=25,
                    background=darkBlue,
                    foreground=white,
                    highlightthickness=2,
                    highlightcolor='WHITE',
                    font=("Arial", 25))

ageEntry.insert(0, "Enter Age Here:")
ageEntry.place(x=50, y=590)

# Work Type Selector #
workVar = tk.StringVar()
workVar.set("Choose Work Status Option")
work_options = ["children", "Govt_jov", "Private", "Self-employed"]

work_selection = tk.OptionMenu(
    window,
    workVar,
    *work_options)

work_selection.config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 25),
    border=0,
    highlightthickness=1,
    highlightbackground=white,
    indicatoron=False
)

work_selection['menu'].config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 16),
    border=0,
    activeborder=2
)

work_selection.place(x=750, y=100)

# BMI Entry #
bmiEntry = tk.Entry(window,
                    width=25,
                    background=darkBlue,
                    foreground=white,
                    highlightthickness=2,
                    highlightcolor='WHITE',
                    font=("Arial", 25))

bmiEntry.insert(0, "Enter BMI Here:")
bmiEntry.place(x=750, y=190)

# Residence Type Selector #
residenceVar = tk.StringVar()
residenceVar.set("Choose Residence Status Option")
residence_options = ["Rural", "Urban"]

residence_selections = tk.OptionMenu(
    window,
    residenceVar,
    *residence_options)

residence_selections.config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 25),
    border=0,
    highlightthickness=1,
    highlightbackground=white,
    indicatoron=False
)

residence_selections['menu'].config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 16),
    border=0,
    activeborder=2
)

residence_selections.place(x=750, y=340)

# Residence Type Selector #
strokeVar = tk.StringVar()
strokeVar.set("Choose Stroke Status Option")
stroke_options = ["Had Stroke", "Never"]

stroke_selections = tk.OptionMenu(
    window,
    strokeVar,
    *stroke_options)

stroke_selections.config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 25),
    border=0,
    highlightthickness=1,
    highlightbackground=white,
    indicatoron=False
)

stroke_selections['menu'].config(
    bg=darkBlue,
    fg=white,
    activebackground=lightBlue,
    activeforeground=white,
    font=('Arial', 16),
    border=0,
    activeborder=2
)

stroke_selections.place(x=750, y=490)

buttonSubmit = tk.Button(window,
    background=darkBlue,
    foreground=white,
    activebackground=lightBlue,
    activeforeground=white,
    highlightthickness=2,
    highlightcolor='WHITE',
    command=Submit,
    width=12,
    height=4,
    text="Submit Options",
    font=("Arial", 16, "bold"))

buttonSubmit.place(x=600, y=600)

buttonReset = tk.Button(window,
    background=darkBlue,
    foreground=white,
    activebackground=lightBlue,
    activeforeground=white,
    highlightthickness=2,
    highlightcolor='WHITE',
    command=Reset,
    width=12,
    height=4,
    text="Reset Options",
    font=("Arial", 16, "bold"))

buttonReset.place(x=800, y=600)

status = tk.Label(window,
    background=darkBlue,
    foreground=white,
    activebackground=lightBlue,
    activeforeground=white,
    highlightthickness=2,
    highlightcolor='WHITE',
    width=12,
    height=5,
    text="Result: ",
    font=("Arial", 16, "bold"))

status.place(x=1000, y=600)

window.bind('<Escape>', toggle_Screen)

window.mainloop()
