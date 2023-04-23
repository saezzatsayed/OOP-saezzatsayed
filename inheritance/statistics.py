# importing classes.py
import classes

# initializing "case" to be equal to 1.(Start point)
case = 1
#While loop as long as there is an accepted input.
while True:
    try:
        # taking input and storing it in "inp"
        inp = input()
        # creating a new object of type sample
        mySample = classes.Sample()
        # mapping out the input and storing it in data variable using set_data
        mySample.set_data(list(map(int, inp.split())))
        # separating the n values from the sample values
        mySample.set_sample(mySample.get_data()[0],mySample.get_data()[1:])

        # applying min method
        sample_min = mySample.get_min()
        # applying max method
        sample_max = mySample.get_max()
        # applying range method
        sample_range = mySample.get_range()

        # printing out the results in the asked form.
        print(f"Case {case}: {sample_min} {sample_max} {sample_range}")
        # incrementing case by 1 each line.
        case += 1
    except EOFError:
        break
