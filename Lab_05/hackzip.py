#!/usr/bin/env python3

import zipfile

print("Hack a ZIP file")

zipfilename = "protected.zip"

zf = zipfile.ZipFile(zipfilename, 'r')
target = zf.namelist()[0]
print("Target filename: " + target)

done = False

### STUDENTS SHALL MAKE SOME CHANGE ON NEXT LINE TO COMPLETE THE HACK!
for PIN in range(1000, 9999):
    try:
        password = str(PIN).zfill(4)
        zf.extract(target, "./temp/", bytes(password, "utf-8"))
    except:
        print("Failed password: " + password)
    else:
        print("Gotcha! Correct password found: " + password)
        print("Extracted file " + target + " to folder temp")
        done = True
        break;

if not done:
    print("Failed to hack the ZIP!")

input("Press Enter to dismiss...")
