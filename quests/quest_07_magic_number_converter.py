# import datetime
import datetime

# 1.Get current year 
current_year = 2026 

# 2.Ask for birth year
birth_year_string = input("The Fortune Teller asks: In what year were you born? ")

# 3.Convert the string to an integer so we can do math
birth_year = int(birth_year_string)

# 4.Perform the calculation
age = current_year - birth_year

# 5.Output
print(f"By my calculations, you are roughly {age} years old!")
