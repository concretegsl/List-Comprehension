import random 

# Get lenght of lists from user
lenA = int(input("Give me the length of list A: "))
lenB = int(input("Give me the length of list B: "))

# Fill list A and B with random integers and lenght according to user input
a = [random.randint(1,10) for _ in range(lenA)]
b = [random.randint(1,10) for _ in range(lenB)]

# Declare set 'c'
c = set()

# Fill set with numbers from A and B, then print all 3 sorted
c = set(a + b)

# changed loop from a + b to c
cEven = {item for item in c if item % 2 == 0}

# Print everything
print("\n -- Lists --")
print(f"Sorted list A: {sorted(a)}")
print(f"Sorted list B: {sorted(b)}")

print("\n -- Sets --")
print(f"Sorted set C: {sorted(c)}")
print(f"Sorted set C (only even numbers): {sorted(cEven)}")

# Print the sum off the lists A, B and set C
# Made output clearer
sumA = sum(a)
sumB = sum(b)
sumC = sum(c)
sumCEven = sum(cEven)
print("\n -- Sums --")
print(f"The sum of list A is: {sumA}")
print(f"The sum of list B is: {sumB}")
print(f"The sum of set C is: {sumC}")
print(f"The sum of set C (even) is: {sumCEven}")


print("Prueba")





