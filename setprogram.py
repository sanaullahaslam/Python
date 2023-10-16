from builtins import print

set={"sanaullah","Sanaullah","aslam","babar",1,"true"}  # in set duplicate value will be ignored
#print(set)
#print(type(set))
#set.add("hello")   #we can't chnage value but add and delete in set
#print(set)
#A set is a collection which is unordered, unchangeable*, and unindexed.
set.remove("sanaullah")
print(set)
set.remove(1)
print(set)
set.remove("true")
helo={"hello","world"}
set.update(helo)   #add another set to current set
print(set)
list=["python","data","science"]    # we can also add list in set by update keyword
set.update(list)
print(set)

set.discard("sanaull")   #remove or discord used to remove value from set but if we use reomveand element does not exists it will cause an error so we use discord
print(set)
print(type(set))

#print("aslam" in set) # to check value is present in set or not
"""for a in set:
    print(a)"""
