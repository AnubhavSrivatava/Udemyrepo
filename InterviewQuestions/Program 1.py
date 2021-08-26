# Write a program for the below mentioned question:
# Create a string variable, str1 and assign it some value, say “abcd”
# Find the number of times the letter ‘a’ occurs in str1 and print the count to console.
# For example, if str1 = aba, the output should be 2

c = 0
str1 = input("Enter any string \n").lower()
length_str1 = len(str1)
for char in str1:
    if char == "a":
        c += 1
print(f" Occurrence of 'a' in {str1} is  {c}")
