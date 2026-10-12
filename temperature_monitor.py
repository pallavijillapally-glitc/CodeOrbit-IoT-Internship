import random
import time

print("IoT Temperature Monitoring System")
print("--------------------------------")

for i in range(10):
    temperature = round(random.uniform(20, 45), 2)

    print("Temperature:", temperature, "°C")

    if temperature > 35:
        print("Alert: High Temperature!")
    else:
        print("Status: Normal")

    print()
    time.sleep(1)
