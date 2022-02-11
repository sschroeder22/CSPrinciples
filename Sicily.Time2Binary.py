#sets hour and minute values from user input
hour, minutes = input('Time? (hh:mm)'). split(':')

#float to make input value usable in math
hour = float(hour)
minutes = float(minutes)

#number of reps of calculate(). used to add details specific to a certain rep
t = 0

#num will be input variable in calculate(), starting with hours
num = hour
#binary is where pieces of the binary will be added
binary = 0
#6 bit binary so 6 bit digits, first calculated is the left most bit
DecimalSpot = 100000
#changes exponent value
n = 0

def calculate():
    #variables in function are no longer local to it
    global t, num, hour, minutes, binary, DecimalSpot, n
    #tempA finds the decimal representation of the binary digit. n is change in exponent, starting at 0
    tempA = 2 ** (5 - n)
    #tempB subtracts temp A from the value being converted
    tempB = num - tempA
    #if tempB is positive, then there is a 1 at that digit
    if tempB >= 0:
        #updates the answer
        binary += DecimalSpot
        #finds remainder to put back through
        num -= tempA
    #makes it so now deciding the next value to the right
    DecimalSpot /= 10
    #decreases the exponent by one to solve for value to the right
    n += 1
    #if n is 6, all binary digits have been checked and solution AKA "binary" is found. t == 0 means it is for hours
    if n == 6 and t == 0:
        #sets the hour value to binary solution
        hour = binary
        #sets the number being converted to minutes, so it will repeat the process with minutes
        num = minutes
        #resets
        DecimalSpot = 100000
        #resets
        binary = 0
        #resets
        n = 0
        #increases t by one, so that the second time around the solution will be recognized as the minute solution
        t += 1
        #runs it again to solve for minutes
        calculate()
    #if n is 6, solution is found. If t == 1, that means it was the minute solution and the full time is converted
    elif n == 6 and t == 1:
        #sets minutes to binary version
        minutes = binary
        #removes the .0 at the end of floats
        minutes = int(minutes)
        hour = int(hour)
        #prints answer onto display
        print (str(hour) + ":" + str(minutes))
    else:
        #repeats the process if not all binary digits have been found
        calculate()

#checks it is a number that makes sense
if minutes <= 60 and hour <= 24:
    #runs script
    calculate()
else:
    print("input doesn't make sense")
