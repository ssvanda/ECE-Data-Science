import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    r1 = re.findall("\+1\s\(\d{3}\)\s\d{3}-\d{4}",searchstring)
    r2 = re.findall("\+1\s\d{3}-\d{3}-\d{4}",searchstring)
    r3 = re.findall("\+52\s\(\d{3}\)\s\d{3}-\d{4}",searchstring)
    r4 = re.findall("\+52\s\d{3}-\d{3}-\d{4}",searchstring)
    r5 = re.findall("\d{3}[-]\d{4}",searchstring)


    if len(searchstring) == 17:
        if len(r1) > 0:
            return True
        else:
            return False
    elif len(searchstring) == 15:
        if len(r2) > 0:
            return True
        else:
            return False
    elif len(searchstring) == 18:
        if len(r3) > 0:
            return True
        else:
            return False
    elif len(searchstring) == 16:
        if len(r4) > 0:
            return True
        else:
            return False
    elif len(searchstring) == 8:
        if len(r5) > 0:
            return True
        else:
            return False
    else:
        return False
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    p = re.compile(r'\d+\s(([A-Z][a-z]*\s)+)(Rd.|Dr.|Ave.|St.)')
    #r1 = p.search(searchstring)
    return p.search(searchstring).group(1).rstrip()
    #return r1.group(0)
    
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    p = re.compile(r'(\d+)\s(([A-Z][a-z]*\s)+)(Rd.|Dr.|Ave.|St.)')
    r0 = p.search(searchstring).group(2).rstrip()
    street = p.search(searchstring).group(4)
    number = p.search(searchstring).group(1)
    r1 = r0[::-1]
    s1 = p.sub(number + ' ' + r1 + ' ' + street, searchstring)
    
    return s1


if __name__ == '__main__' :
    
    print(problem1('+1 765-494-4600')) #True
    print(problem1('+52 765-494-4600 ')) #False
    print(problem1('+1 (765) 494 4600')) #False
    print(problem1('+52 (765) 494-4600')) #True    
    print(problem1('494-4600')) #True
    
    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First
    
    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))
    