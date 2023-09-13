# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:09:02 2023

@author: Dou
"""

def is_valid_date(year: int, month: int, day: int) -> bool:
    """
    Check if a given date is valid.

    Args:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # Initialize the number of days in each month
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if it's a leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day_count_for_month[2] = 29

    # Check if the month and day are within the valid range
    return 1 <= month <= 12 and 1 <= day <= day_count_for_month[month]

date = [[2021,2,29],[2020,2,29],[2020,13,29],[2020,1,32]]
for d in date:
    if is_valid_date(*d):
        print(f"La date {d[2]}/{d[1]}/{d[0]} est valide")
    else:
        print(f"La date {d[2]}/{d[1]}/{d[0]} n'est pas valide")

