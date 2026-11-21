def add_two_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b


def area_of_circle(radius):
    """
    This function calculates the area of a circle given its radius.
    
    Parameters:
    radius (int or float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2

def add_all_numbers(*args):
    """
    This function takes any number of arguments and returns their sum.
    
    Parameters:
    *args (int or float): A variable number of numbers to be summed.
    
    Returns:
    int or float: The sum of all the input numbers.
    """
    return sum(args)

def convert_celsius_to_fahrenheit(celsius):
    """
    This function converts a temperature from Celsius to Fahrenheit.
    
    Parameters:
    celsius (int or float): The temperature in Celsius.
    
    Returns:
    float: The temperature converted to Fahrenheit.
    """
    return (celsius * 9/5) + 32

def check_season(month):
    """
    This function checks the season based on the given month.
    
    Parameters:
    month (str): The name of the month.
    
    Returns:
    str: The season corresponding to the month.
    """
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'

def calculate_slope(x1, y1, x2, y2):
    """
    This function calculates the slope of a line given two points (x1, y1) and (x2, y2).
    
    Parameters:
    x1 (int or float): The x-coordinate of the first point.
    y1 (int or float): The y-coordinate of the first point.
    x2 (int or float): The x-coordinate of the second point.
    y2 (int or float): The y-coordinate of the second point.
    
    Returns:
    float: The slope of the line connecting the two points.
    """
    if x2 - x1 == 0:
        raise ValueError("The x-coordinates cannot be the same; slope is undefined.")
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    """
    This function solves a quadratic equation of the form ax^2 + bx + c = 0.
    
    Parameters:
    a (int or float): The coefficient of x^2.
    b (int or float): The coefficient of x.
    c (int or float): The constant term.
    
    Returns:
    tuple: A tuple containing the two solutions of the quadratic equation.
    """
    import cmath
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return (root1, root2)

def print_list(lst):
    """
    This function prints each element of a list on a new line.
    
    Parameters:
    lst (list): The list to be printed.
    
    Returns:
    None
    """
    for item in lst:
        print(item)


def reverse_list(lst):
    """
    This function reverses a list.
    
    Parameters:
    lst (list): The list to be reversed.
    
    Returns:
    list: The reversed list.
    """
    return lst[::-1]
    

# calling the functions

print(add_two_numbers(5, 3))
print(area_of_circle(5))    
print(add_all_numbers(1, 2, 3, 4, 5))
print(convert_celsius_to_fahrenheit(21))
print(check_season('February'))
print(calculate_slope(15, 2, 23, 9))
print(solve_quadratic_eqn(1, -5, 6))
print(print_list(['HTML', 'CSS', 'JS', 'React', 'Python']))
print(reverse_list(['HTML', 'CSS', 'JS', 'React', 'Python']))
