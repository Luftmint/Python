#Övning 4 Datum-koll (error om det är mellan 00-06),
from datetime import datetime 

date = datetime.now()

if 0<=date.hour < 6:
    print("Varning! Det är sent, gå och lägg dig.")
else:
    print("Godmorgon")
print(f"Tid: {date}") 
# Eller print(f"Aktuell tid: {now.strftime('%Y-%m-%d %H:%M:%S')}")  
# Skriv ut aktuell tid
