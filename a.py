
# LIST
list1 = [10,20,30,40,20]
print("This is list :", list1)

print("Access first element :", list1[0])

list1.append(50)
print("Append the list :", list1)

list1.remove(20)
print("Remove 20 from list :", list1)

sum1 = 0
for i in list1:
    sum1 = sum1 + i
print("Sum of list :", sum1)


# TUPLE
tuple1 = (1,2,3,4,2)
print("\nThis is tuple :", tuple1)

print("Access second element :", tuple1[1])

sum2 = 0
for i in tuple1:
    sum2 = sum2 + i
print("Sum of tuple :", sum2)


# DICTIONARY
dict1 = {"name":"Harshit","age":22,"marks":80}
print("\nThis is dictionary :", dict1)

print("Print name from dictionary :", dict1["name"])

dict1["age"] = 23
print("Update age :", dict1)

dict1["city"] = "Modinagar"
print("Add city :", dict1)

total = dict1["age"] + dict1["marks"]
print("Sum of age and marks :", total)


# SET
set1 = {10,20,30,40,20}
print("\nThis is set :", set1)

set1.add(50)
print("Add 50 in set :", set1)

set1.remove(30)
print("Remove 30 from set :", set1)

sum3 = 0
for i in set1:
    sum3 = sum3 + i
print("Sum of set :", sum3)