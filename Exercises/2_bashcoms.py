# Övning 2, lista med bash kommandon,
# 5 bash kommandon,

# Importing sleep module from time so I can delay the output,
from time import sleep

com_list = ['whoami', 'date', 'pwd', 'cd', 'cat']

# For-loop to print each item in the list one by one,
for i in range(0,4):
    print(com_list[i]);
    sleep(0.5); # Delay of 0.5sec between the printing of each line
