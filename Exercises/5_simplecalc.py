# Övning 5, en enkel kalkylator 
# + - / eller * två tal, skriv ut produkt samt differens(?)

# Funktion för addition
def add(n1,n2):
    answer = n1 + n2
    return answer

# Funktion för subtraktion
def sub (n1,n2):
    answer = n1 - n2
    return answer

# Funktion för division
def div(n1,n2):
    answer = n1 / n2
    return answer

# Funktion för multiplikation
def mult(n1,n2):
    answer = n1 * n2
    return answer


print("Select operation -\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Divide\n"
        "4. Multiply\n")

user = int(input("Select operation[1-4]: "))
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
answer = ""

if user == 1:
    print(n1, "+", n2, "=", add(n1,n2))
elif user == 2:
    print(n1, "-", n2, "=", sub(n1,n2))
elif user == 3:
    print(n1, "/", n2, "=", div(n1,n2))
elif user == 4:
    print(n1, "*", n2, "=", mult(n1,n2))
else:
    print("Invalid input.")





