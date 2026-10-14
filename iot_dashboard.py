import tkinter as tk
import csv
import os

root = tk.Tk()
root.title("IoT Sensor Dashboard")
root.geometry("600x450")
root.configure(bg="#eaf2f8")

title = tk.Label(
    root, text="IoT Temperature Dashboard",
    font=("Arial", 20, "bold"),
    bg="#154360", fg="white", pady=15
)
title.pack(fill="x")

temp_label = tk.Label(
    root, text="Current Temperature: Loading...",
    font=("Arial", 16), bg="#eaf2f8"
)
temp_label.pack(pady=20)

status_label = tk.Label(
    root, text="Status: Waiting",
    font=("Arial", 15, "bold"), bg="#eaf2f8"
)
status_label.pack(pady=10)

history_label = tk.Label(
    root, text="Temperature Readings",
    font=("Arial", 14, "bold"), bg="#eaf2f8"
)
history_label.pack(pady=10)

readings_box = tk.Listbox(root, width=45, height=8)
readings_box.pack(pady=5)

def load_data():
    readings_box.delete(0, tk.END)
    temperatures = []

    try:
        with open("temperature_data.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                temp = float(row["Temperature_C"])
                temperatures.append(temp)
                readings_box.insert(
                    tk.END,
                    f"Reading {row['Reading']}: {temp:.2f} °C"
                )

        if temperatures:
            current = temperatures[-1]
            temp_label.config(
                text=f"Current Temperature: {current:.2f} °C"
            )

            if current > 35:
                status_label.config(
                    text="ALERT: High Temperature!",
                    fg="red"
                )
            else:
                status_label.config(
                    text="Status: Normal",
                    fg="green"
                )
        else:
            temp_label.config(text="No readings available")

    except (FileNotFoundError, KeyError, ValueError):
        temp_label.config(
            text="CSV file missing or format incorrect"
        )
        status_label.config(text="Check Task 2 CSV file", fg="red")

refresh_button = tk.Button(
    root, text="Refresh Dashboard",
    command=load_data, font=("Arial", 12)
)
refresh_button.pack(pady=10)

load_data()
root.mainloop()
