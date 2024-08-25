def is_leap(year):
    """
    Returns True if the year is a leap year, False otherwise.
    """
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))