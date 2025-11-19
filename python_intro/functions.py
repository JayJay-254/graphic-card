def my_function():
    #  lines of codes that perform a specific task
    print("Hello Jay")
my_function()

def salutation():
    hello = "Good Afternooon bestie"
    print(hello)
salutation()

def salute(name):
    print(f'Good afternoon {name}')
salute('Jay')

def student(name, age, gender):
    print(f'My name is {name}, I am a {gender} and am {age} years old')
student('Jay Jay', 21, 'Man')

def multi(a, b, c):
    result = a*b*c
    return result
print(multi(2,4,6))

def age_calc(current_age):
    new_age = current_age + 9
    return new_age
print(age_calc(21))

# write a function that calculates a persons BMI and response to the person whether they are obese or an underweight

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f'Your BMI is {bmi:.2f}. You are underweight.'
    elif 18.5 <= bmi < 24.9:
        return f'Your BMI is {bmi:.2f}. You have a normal weight.'
    elif 25 <= bmi < 29.9:
        return f'Your BMI is {bmi:.2f}. You are overweight.'
    else:
        return f'Your BMI is {bmi:.2f}. You are obese.'
print(bmi_calculator(70, 1.75))