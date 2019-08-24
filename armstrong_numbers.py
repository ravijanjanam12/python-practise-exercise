def is_armstrong_number(number):
    n=len(str(number))
    rlist=[]
    for num in str(number):
        rlist.append(int(num)**n)
    if sum(rlist)==number:
        return True
    else: 
        return False

