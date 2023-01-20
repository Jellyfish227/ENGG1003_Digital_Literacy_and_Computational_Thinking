universities = ["CUHK", "HKU", "UST"]
print( "First:", universities[0] )
universities.append("MU");  # append "MU" at the end
universities[1] = "MU";     # replace "HKU" with "MU"
# the list becomes [ "CUHK" , "MU" , "UST" , "MU" ]
for item in universities:
    print(item)             # print list items, one on a line
del universities[2]         # remove "UST"
print( universities )       # print the whole list

