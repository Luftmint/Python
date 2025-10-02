# Övning 7, file size check

size = float(input("Size of your file in mb: "))

if size < 100:
    print("Filesize good!")
else:
    print("Not good, get rid of the bloat.")