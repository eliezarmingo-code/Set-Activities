
# Activity 1: Remove Duplicates
print("Activity 1: Remove Duplicates")
numbers = [1, 2, 2, 3, 4, 4, 5]

# Convert to set and print unique values
numbers = set([1,2,2,3,4,4,5])
print(numbers)

# Activity 2: Add and Remove
print("\nActivity 2: Add and Remove")
fruits = {"apple", "banana"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)

# Activity 3: Set Operations
A = {1, 2, 3}
B = {3, 4, 5}

# Find:
# union
union_result = A | B
print("Union:", union_result)

# intersection
intersection_result = A & B
print("Intersection:", intersection_result)







# Activity 4 (Challenge): Common Students

classA = {"John", "Ana", "Mark"}
classB = {"Ana", "Mark", "Liza"}

#Find students in BOTH classes
common_students = classA & classB
print("Students in Both classes:", common_students)

#Find ALL students
all_students = classA | classB
print("All students:", all_students) 

