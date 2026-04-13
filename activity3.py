for X in range(50):
    if X % 20 == 0:
        print("twist")

    elif X % 15 == 0:
        pass 

    elif X % 5 == 0:
        print("fizz")

    elif X % 3 == 0:
        print("buzz")

    else:
        print(X)            