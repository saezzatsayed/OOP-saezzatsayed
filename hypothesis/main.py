import classes


def main():
    # "x" string value to store name value in.
    # "y" float value to store cap value from input.
    x: str = "name"
    y: str = "0.0"

    # "myMovie_name" is a new object from class movie_name.
    # "myMovie_cap" is a new object from class movie_cap.
    myMovie_name =  classes.movie_name()
    myMovie_cap =  classes.movie_cap()

    # take input split values and assign them to "x" and "y" in order.
    x, y = input().split()

    # use the setter function to set the value of the name.
    # use the setter function to set the value of the cap.
    myMovie_name.set_name(x)
    myMovie_cap.set_value(y)

    # "result" stores the min of the two numbers. 
    result = min(len(myMovie_name.get_name()), float(myMovie_cap.get_value()))

    # prints out the result
    print(result)
    print("This file is being run directly")


if __name__ == '__main__':
    main()
else:
    print("This is an imported file")
