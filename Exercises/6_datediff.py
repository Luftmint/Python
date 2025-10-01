# Övning 6, date difference 
# Count days between 2025/01/01 and the date of which this code is ran
import datetime

d = datetime.datetime(2025, 1, 1, 00) # Sets the set date
now = datetime.datetime.now() # Sets the current time
diff = now - d # Subtracts the set date from current to get the value of time between

print(diff) # Print out the difference