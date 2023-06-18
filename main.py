import tkinter as tk
from tkinter import messagebox
import joblib

# Load the trained model
model = joblib.load('diabetes_model.joblib')

# Create the main application window
window = tk.Tk()
window.title("Diabetes Prediction App")
window.minsize(300, 400)

# Function to handle the prediction, sends data to prewiously trained model
def predict_diabetes():
    pregnancies = float(pregnancies_entry.get() or 0)
    glucose = float(glucose_entry.get() or 0)
    blood_pressure = float(blood_pressure_entry.get() or 0)
    skin_thickness = float(skin_thickness_entry.get() or 0)
    insulin = float(insulin_entry.get() or 0)
    diabetes_pedigree = float(diabetes_pedigree_entry.get() or 0)
    Bmi = float(BMI_entry.get() or 0)
    age = float(age_entry.get() or 0)

    input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, diabetes_pedigree, Bmi, age]]
    
    predictions = model.predict(input_data)
    if predictions[0] == 0:
        result = "Not Diabetic"
    else:
        result = "Diabetic"

    messagebox.showinfo("Prediction Result", f"The person is {result}")

# Create the input fields and labels
pregnancies_label = tk.Label(window, text="Pregnancies:")
pregnancies_label.pack()
pregnancies_entry = tk.Entry(window)
pregnancies_entry.pack()

glucose_label = tk.Label(window, text="Glucose:")
glucose_label.pack()
glucose_entry = tk.Entry(window)
glucose_entry.pack()

blood_pressure_label = tk.Label(window, text="Blood Pressure:")
blood_pressure_label.pack()
blood_pressure_entry = tk.Entry(window)
blood_pressure_entry.pack()

skin_thickness_label = tk.Label(window, text="Skin Thickness:")
skin_thickness_label.pack()
skin_thickness_entry = tk.Entry(window)
skin_thickness_entry.pack()

insulin_label = tk.Label(window, text="Insulin:")
insulin_label.pack()
insulin_entry = tk.Entry(window)
insulin_entry.pack()

BMI_label = tk.Label(window, text="BMI:")
BMI_label.pack()
BMI_entry = tk.Entry(window)
BMI_entry.pack()

diabetes_pedigree_label = tk.Label(window, text="Diabetes Pedigree:")
diabetes_pedigree_label.pack()
diabetes_pedigree_entry = tk.Entry(window)
diabetes_pedigree_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

# Create the predict button
predict_button = tk.Button(window, text="Predict", command=predict_diabetes)
predict_button.pack()

# Run the application
window.mainloop()