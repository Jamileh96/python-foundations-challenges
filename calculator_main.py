
def calculator():
    from art import logo
    print(logo)

    n1 = float(input("What's the first number: "))
    continue_calculation = True
    answer = 0 #this is added cuz what if the user inout was wrong, the system would still have an answer = 0
    print("+ \n" "- \n" "* \n" "/ \n")
    user_operation = input("Pick an operation  ")
    n2 = float(input("What's the second number: "))
    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    def multiply(n1, n2):
        return n1 * n2
    def divide(n1, n2):
        return n1 / n2

    #PAUSE 2
    operations = { #look at the solution she used for loop for this
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide}
    #print(operations["+"](3, 2)) this is pause 3
    if user_operation == "+":
        answer = operations["+"](n1, n2)
        print(f"{n1} + {n2} = {answer}")
    elif user_operation == "-":
        answer = operations["-"](n1, n2)
        print(f"{n1} - {n2} = {answer}")

    elif user_operation == "*":
        answer = operations["*"](n1, n2)
        print(f"{n1} * {n2} = {answer}")

    elif user_operation == "/":
        answer = operations["/"](n1, n2)
        print(f"{n1} / {n2} = {answer}")
    else:
        print("Invalid operation")

    while continue_calculation:
        calculation_2 = input(f"Type 'y' to continue with {answer} or type 'n' to start a new operation")

        if calculation_2 == "y":
            n1 = answer
            print("+ \n" "- \n" "* \n" "/ \n")
            user_operation = input("Pick an operation  ")
            n2 = float(input("What's the second number: "))
            answer = operations[user_operation](n1, n2)
            print(f"{n1} {user_operation} {n2} = {answer}")
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()

calculator()

#okay i need to focus and make things simpler lol