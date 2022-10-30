#Basic Calculator with Python 
def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " =" + str(answer))

def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

print("A. Addition (Toplama)")
print("B. Subtraction (Çıkarma)")
print("C. Multiplication (Çarpma)")
print("D. Division (Bölme)")
print("E. Exit (Çıkış)")

choice = input("Input your choice: ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Input first number (Birinci sayıyı giriniz): "))
    b = int(input("Input second number (İkinci sayıyı giriniz): "))
    add(a,b)

elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("Input first number (Birinci sayıyı giriniz): "))
    b = int(input("Input second number (İkinci sayıyı giriniz): "))
    sub(a,b)
elif choice == "C" or choice == "c":
    print("Multiplication")
    a = int(input("Input first number (Birinci sayıyı giriniz): "))
    b = int(input("Input second number (İkinci sayıyı giriniz): "))
    mul(a,b)
elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("Input first number (Birinci sayıyı giriniz): "))
    b = int(input("Input second number (İkinci sayıyı giriniz): "))
    div(a,b)
elif choice == "e" or choice == "E":
    print("Program Ended (Bitiş")
    quit()

#Open source code, edited by Yağız Köylü with additions.
    