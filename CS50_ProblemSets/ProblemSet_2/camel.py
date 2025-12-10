camel_case = input("Enter a variable name in camel case: ").strip()

snake_case = ""

for i, char in enumerate(camel_case):
    if char.isupper() and i > 0:
        snake_case += "_" + char.lower()
    else:
        snake_case += char.lower()

print(f"Snake case: {snake_case}")