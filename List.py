list= ["sanaullah",1,"ali","sanaullah",1]

for i in list:
    print(i)
print(list[::3])   # :: 3 means print first then leave 3 then print
print(list.append("sami"))  # append add value to the list in the last

print(list.insert(0,"first"))  #insert function add value to list but you have to give index also

#list.pop()  remove the valuesfrom list in the last
print(list)

print(list[1:3])   # specifying range for list from 1 to 3 element shown