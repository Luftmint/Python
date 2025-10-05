# Övning 12, list with failed logins

login_log = {
    1: 'failed login',
    2: 'failed login',
    3: 'successful login',
    4: 'successful login',
    5: 'failed login',
    6: 'successful login'
}

dict_list = list(login_log.items())
count = " "

for dict_list in range(0-5):
    for i in dict_list:
        if i == 'failed login':
            count + 1
        elif count == 3:
            print("Brute force attack.")
    
     