def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats

    # Write your code here
    # 2. Change `h` to absolute value of `b` 
    #    if the absolute value of `b` is greater than `h`
    if (abs(b) > abs(h)):                                              
        h = abs(b)
    # 3. **if `b < 0` any values in `data` that are negative should
    #    be changed to its absolute value.**
    
    if b < 0:
        for index in range(len(data)):                                                  
                data[index] = abs(data[index])

    # 4. Change `b` to `0` if `b` is negative.
        b = 0  
    # 5. Initialize the histogram `hist` as a list of `n` zeros.                                                 
    hist = [0] * n                                                      
    # 6. Calculate the bin width as `w = (h-b)/n`, so that `hist[0]`
    #    will represent values in the range `(b, b + w)`, `hist[1]` 
    #    in the range `[b + w, b + 2w)`, and so on through `hist[n-1]`.
    #    (Remember that `[` is inclusive while `)` is not!).
    #           which bin does the data bit belong to, then add 1 to that element 
    w = (h-b)/n

    # 7. Ignore any values in `data` that are less than or equal to `b`
    #    and greater than or equal to `h`. *Remember if you have change `h` 
    #    in step 2, you would need to work with the new value of `h`. The same
    #    goes for `b`, if modified in step 4*.
    
    for d in data:
        if ((d <= b) or (d >= h)):
            pass
    # 8. Increment `hist[i]` by 1 for each value in `data` that belongs to 
    #    bin `i`, i.e., in the range `[b + i*w, b + (i+1)*w)`.
        else:
            for i in range(n):
                if (((b + i*w) <= d) and (d < (b + (i+1)*w))):
                    hist[i] = hist[i] + 1
    # return the variable storing the histogram
    # Output should be a list
#            i = 0
#            while i < n:
#                #if (((b + i*w) < d) and (d < (b + (i+1)*w))):
#                if (b + i*w) < d < b + (i+1)*w:
#                    hist[i] = hist[i] + 1
#                i = i + 1
                    
    return hist
    pass


def birthdaycake(name_to_day, name_to_month, name_to_year):
    #name_to_day, name_to_month and name_to_year are dictionaries
    #Write your code here
    import datetime
    import random
    import calendar
    import math
    name_to_date = {}
    zellerdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for name in name_to_day.keys():
        day = name_to_day[name]
        month = name_to_month[name]
        year = name_to_year[name]
        if month <= 2:
            month+= 12
    # and also adjust year if January or February
        
        if ((name_to_month[name] == 10) or (name_to_month[name] == 11) or (name_to_month[name] == 12)):
            year += 5
        name_to_year[name] = year
        if name_to_month[name] <= 2:
            year -= 1
        day_return = (day + math.floor((13 * (month + 1)) / 5) + year + math.floor(year / 4) - math.floor(year / 100) + math.floor(year / 400)) % 7
        
        name_to_date[name] = ((name_to_month[name], name_to_day[name], name_to_year[name]), zellerdays[day_return])

    return name_to_date


    # return the variable storing name_to_all
    # Output should be a dictionary
    
    pass