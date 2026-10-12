import random
import time
import csv
import matplotlib.pyplot as plt

temperatures = []

print("IoT Temperature Monitoring System")
print("---------------------------------")

with open("temperature_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Reading", "Temperature_C", "Status"])

    for i in range(10):
        temperature = round(random.uniform(20, 45), 2)
        temperatures.append(temperature)

        if temperature > 35:
            status = "High Temperature"
        else:
            status = "Normal"

        print("Reading:", i + 1)
        print("Temperature:", temperature, "°C")
        print("Status:", status)
        print()

        writer.writerow([i + 1, temperature, status])
        time.sleep(1)

print("Temperature data saved to CSV file.")

plt.plot(range(1, 11), temperatures, marker="o")
plt.axhline(y=35, linestyle="--", label="Alert Threshold")
plt.xlabel("Reading Number")
plt.ylabel("Temperature (°C)")
plt.title("IoT Temperature Monitoring")
plt.legend()
plt.grid(True)
plt.savefig("temperature_graph.png")
plt.show()

print("Temperature graph saved successfully.")
