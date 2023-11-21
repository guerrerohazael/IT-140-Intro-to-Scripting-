//Simple Python code to output "Hello, (your name)! You were born in, (birth year)"


# Prompt the user for their name
name = input("What is your name? ")

# Prompt the user for their age
age = int(input("How old are you? "))

# Calculate the birth year
current_year = 2023
birth_year = current_year - age


# Display the result
print("Hello", name + "! You were born in", birth_year,)
