# QUESTION 1
def CALCULATEGRADE(Score):
    if Score > 100 or Score < 0:
        return 'Invalid score'
    elif Score >= 90:
        return 'A+'
    elif Score >= 80:
        return 'A'
    elif Score >= 70:
        return 'B'
    elif Score >= 60:
        return 'C'
    elif Score >= 50:
        return 'D'
    elif Score >= 40:
        return 'E'
    else:
        return 'F'

def print_MarkSheet(Name, Score, Grade):
    print("Marksheet")
    print(f"Student Name: {Name}")
    print(f"Score: {Score}")
    print(f"Grade: {Grade}")

Name = input("Enter the student's name: ")
try:
    Score = float(input("Enter the student's score: "))
    if Score > 100:
        raise ValueError("Score cannot be greater than 100.")
except ValueError as e:
    print(e)
    exit()

Grade = CALCULATEGRADE(Score)
print_MarkSheet(Name, Score, Grade)


# QUESTION:2
Year = int(input("Enter a year: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(f"{Year} is a leap year.")
else:
    print(f"{Year} is not a leap year.")

# Question 3
def Celsius_to_Fahrenheit(Celsius):
    return (9/5) * Celsius + 32

def Fahrenheit_to_Celsius(Fahrenheit):
    return (5/9) * (Fahrenheit - 32)

def Celsius_to_Kelvin(Celsius):
    return Celsius + 273.15

print("Choose a NUMBER:") 
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
print("3: Celsius to Kelvin")

choice = int(input("Enter Choice (1/2/3): "))

if choice == 1:
    Celsius = float(input("Enter temperature in Celsius: "))
    Fahrenheit = Celsius_to_Fahrenheit(Celsius)
    print("Temperature in Fahrenheit:", Fahrenheit)
elif choice == 2:
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celsius = Fahrenheit_to_Celsius(Fahrenheit)
    print("Temperature in Celsius:", Celsius)
elif choice == 3:
    Celsius = float(input("Enter temperature in Celsius: "))
    Kelvin = Celsius_to_Kelvin(Celsius)
    print("Temperature in Kelvin:", Kelvin)
else:
    print("Invalid Choice")

# QUESTION 4
def determine_triangle_type(Side1, Side2, Side3):
    if Side1 <= 0 or Side2 <= 0 or Side3 <= 0:
        return "Invalid Triangle: All side lengths must be positive."
    elif Side1 + Side2 <= Side3 or Side2 + Side3 <= Side1 or Side1 + Side3 <= Side2:
        return "Invalid Triangle: The given sides do not form a triangle."
    if Side1 == Side2 == Side3:
        return "Equilateral Triangle"
    elif Side1 == Side2 or Side2 == Side3 or Side1 == Side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

try:
    Side1 = float(input("Enter the length of the first side: "))
    Side2 = float(input("Enter the length of the second side: "))
    Side3 = float(input("Enter the length of the third side: "))
except ValueError:
    print("Invalid input.")
    exit()

triangle_type = determine_triangle_type(Side1, Side2, Side3)
print("The triangle is a:", triangle_type)
