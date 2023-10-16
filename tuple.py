tple =("Sanaullah" , "Aslam" , "Babar" , 9)   # tuple are unchangable

#print(tple)
#print(tple[-1])    # -1 indicate access value from last
#print(type(tple))
#size=len(tple)
#print(tple[2:4])   # 2:4 indicate starting and ending value simply it define range
#print(size)
i=0

#while i<size:
   # print(tple[i])
   # i+=1;

#for i in tple:
 #   print(i)


tp=("Hello","World")  # we can't change tuple but we can convert into list then update then convert back to tuple
lt=list(tp)
lt[1]="sanaullah"
tp=tuple(lt)
print(tp)