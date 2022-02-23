while True:
    num = input("Please enter a number ")
    try:
        val = int(num)
        print("Input is an integer number.")
        print("Input number is: ", val)
        break
    except ValueError:
        print("Input is not integer.")
