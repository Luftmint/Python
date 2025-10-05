# Övning 11, nattinloggning
# If login between 22-06, write 'nightly login suspected'

from datetime import datetime

now = datetime.now()

if now.hour > 22-6:
    print("Nightly login suspected.")
else:
    print("Welcome.")