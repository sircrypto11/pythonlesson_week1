name=input("enter name:")
age=int(input("Enter your age"))
DoB= age
print(f"hello {name},you were born in {2026-age} years old. You are {2026-age}")

age=2
if age<0 or age>200:
   print("Invalid age")
elif age >=18:
   print("You can vote")
else:
   print("Go home kid")