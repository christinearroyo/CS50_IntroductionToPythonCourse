text = input("Input: ")

result = ""

vowels = "AEIOUaeiou"

for char in text:
    if char not in vowels:
        result += char

print("Output:", result)