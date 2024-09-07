try:
    age = int(input("How old are you?"))
except ValueError:
    print("you have typed in letters try in numbers")
    age= int(input("how old are you"))
if age > 18:
    print(f"You can drive at age {age}.")
