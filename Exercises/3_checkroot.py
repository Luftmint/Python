# Övning 3, root checker,
# Import sys and subprocess,
import subprocess # This is so that the 'whoami' code gets captured and not printed


name = input("Input your username: ").strip()

whoami = subprocess.check_output(['whoami']).decode().strip() # Runs command and captures output and checks it

if name != whoami:
    print(f"{name} is approved");
    exit() 
else:
    print(f"The username {name} is not secure enough, why are you root??")