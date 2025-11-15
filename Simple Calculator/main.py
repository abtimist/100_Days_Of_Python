from art import logo
print(logo+"\n\n\n")
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2
is_continue=True
result=float()
status="n"
operation={"+":add,"-":subtract,"*":multiply,"/":divide}
while is_continue:
    if status=="y":
        n1=result
    elif status=="n":
        n1 = float(input("Enter the first number: "))
    else:
        is_continue=False
        continue
    print("Choose the operation: ")
    for i in operation:
        print(i)
    operator=input()
    n2=float(input("Enter the second number: "))
    result=operation[operator](n1,n2)
    print(result)
    status=input(f"Do you want to continue your calculation on {result} or start a new calculation?Y/N").lower()
