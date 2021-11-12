def is_leap(year):
    
    if year==2100 or year==2200 or year==2300 or year==2500 :
        leap=False
    elif year%4==0 :
        leap=True
    else:
        leap = False
    
    return leap
