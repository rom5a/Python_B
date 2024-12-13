# 1 Prover videnie simvoli cifra ili storka

integer = input("Enter a numer:")
if integer.isdigit():
    integer = int(integer)

print(type(integer))

# 2 Formatirovanie

name = "Roman"
age = 25
print(f"Hello, my name is {name} and my age is {age}")

# 3
x = 5
y = 10
print(f"x umonizit na y ravnog {x*y}, slozoit {x+y}" )
