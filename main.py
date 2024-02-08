import tkinter as tk
from Predictor import Predictor

# Colors #
gray = "#363636"
lightBlue = "#0080FE"
white = "#FBFCF8"
darkBlue = "#0F52BA"

predictor = Predictor()

window = tk.Tk()

window.attributes("-fullscreen", True)

window.title("Glucose Predictor")

window.config(background="BLACK")

window.geometry("360x360")


def toggle_Screen(event):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))


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

gender_select.place(x=50, y=0)

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

hypertension_select.place(x=50, y=100)

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

disease_selection.place(x=50, y=200)

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

married_selection.place(x=50, y=300)

# Age Entry #
ageEntry = tk.Entry(window,
    width=25,
    background=darkBlue,
    foreground=white,
    highlightthickness=2,
    highlightcolor='WHITE',
    font=("Arial", 25))

ageEntry.insert(0, "Enter Age Here:")
ageEntry.place(x=50, y=450)

# Work Type Selector #
workVar = tk.StringVar()
workVar.set("Choose Work Status Option")
work_options = ["Children", "Government", "Private", "Self Employed"]

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

work_selection.place(x=50, y=500)

# BMI Entry #
bmiEntry = tk.Entry(window,
    width=25,
    background=darkBlue,
    foreground=white,
    highlightthickness=2,
    highlightcolor='WHITE',
    font=("Arial", 25))

bmiEntry.insert(0, "Enter BMI Here:")
bmiEntry.place(x=50, y=600)

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

residence_selections.place(x=50, y=700)

window.bind('<Escape>', toggle_Screen)

window.mainloop()
