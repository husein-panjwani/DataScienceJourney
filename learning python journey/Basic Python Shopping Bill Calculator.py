num1 = 0
for i in range(100):

    print("enter price of item no ", i+1, ":")
    user_input = (input())
    if user_input != "q":
        num2 = user_input
        add = num1 + int(num2)
        num1 = add
        print("your bill total is ", add)
    else:
        print("your bill total is :", add)
        print("thanks for shopping")
        given = int(input("enter the money coustmer gave you "))
        while given < add:
            print("ask for more money")
            given=int(input("enter correct value"))

        change = given - add
        print("return",change)
        break
