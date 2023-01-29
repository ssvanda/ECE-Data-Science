#!/usr/bin/python3
day = 'sunday'
# Your code should be below this line
##Modify `problem1.py` by adding additional lines of code so that it solves the following problem: 

##Determine if the text entered at the top of the file in problem1.py is a `weekday`, `weekend`, or `neither`, and print the result accordingly.
#For example, if `day` = `tuesday`, it should print `weekday`, while if `day` = `saturday`, it should print `weekend`, and 
# finally if `day` = `noth1ng`, it should print `neither`.

##Your code should be correct for any string entered into the day variable. 
# You can assume the text will always be entered in all lowercase.
#  At the same time, please be careful to format your print outputs exactly as stated above, i.e., in all lowercase and without any additional whitespace.

##You can temporarily change the value of the year variable to test your code, but you **SHOULD** return it to its original value `day` = `sunday` before submission.
if day == ("sunday" or "saturday"):
    print ("weekend")
elif day == ("monday" or "tuesday" or "wednesday" or "thursday" or "friday"):
    print ("weekday")
else:
    print ("neither")
