#Task1

try:
    while True:
        user_input = int(input("Enter temperature in Farenheit: "))
        print(user_input)
except ValueError:
    print("Ooops! That's not a valid number")

#Task2

def temperature(farenheit):
    celsius = (farenheit - 32) * 5 / 9
    return celsius

try:
    while True:
        farenheit = int(input("Enter temperature in Farenheit: "))
        print(f"{farenheit}°F is {celsius}°C")

except ValueError:
    print("Ooops! That's not a valid number.")

#Task3