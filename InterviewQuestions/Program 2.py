# Create three variables: a, b & c
# Print the three numbers in ascending order, separated by commas.For example: Let a = 1, b = 5, c = 2.
# Output = 1, 2, 5


a = int(input("Enter 1st number \n"))
b = int(input("Enter 2nd number \n"))
c = int(input("Enter 3nd number \n"))

smallest = min(a, b, c)
largest = max(a, b, c)
mid = (a + b + c) - largest - smallest
print(f"Output = {smallest},{mid},{largest}")
