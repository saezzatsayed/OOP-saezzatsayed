#imports classes.py
import classes

#while loop takes all test cases, stops when input = 0 0.
while True:
    # "inp" var to store the input.
    inp = input()
    # if loop to stop the while loop when input = 0 0.
    if inp == "0 0":
        break
    # 'k', 'm' are two variables to save the split of the input.    
    k, m = inp.split()

    # creating new objects of type fraction and reminder.
    myfraction = classes.fraction() 
    myreminder = classes.reminder()

    # setting the numerator and denominator of the fraction.
    myfraction.set_x(int(k))
    myfraction.set_y(int(m))

    # calculating the division of the fraction then assiging it to the whole number of the mixed fraction
    myreminder.set_whole(int(myfraction.get_x()/myfraction.get_y()))
    # calculating the remainder of the fraction then assiging it to the remainder number of the mixed fraction
    myreminder.set_rem(myfraction.get_x() % myfraction.get_y())

    #prints out the mixed fraction
    print(myreminder.get_whole(), myreminder.get_rem(),"/",myfraction.get_y())