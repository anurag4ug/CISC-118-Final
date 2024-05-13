for row in range(11):
    for column in range(10):
        if (row + column) % 2 == 0:
            print("*", end=" ")
        else:
            print("+", end=" ")
    print()
    