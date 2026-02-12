# # functions
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b


# # loop calculator
# while True:

#     print("\n--- CALCULATOR ---")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     choice = input("Choose operation: ")

#     if choice == "5":
#         print("Calculator closed.")
#         break

#     x = float(input("Enter first number: "))
#     y = float(input("Enter second number: "))

#     if choice == "1":
#         print("Answer:", add(x, y))

#     elif choice == "2":
#         print("Answer:", subtract(x, y))

#     elif choice == "3":
#         print("Answer:", multiply(x, y))

#     elif choice == "4":
#         print("Answer:", divide(x, y))

#     else:
#         print("Invalid choice")


def analyze_sentence(sentence, shout=False, reverse=False):
    """
    Analyze a sentence:
    - Count characters, words, vowels, consonants
    - Optionally uppercase or reverse the sentence
    Returns a dictionary with results
    """
    sentence = sentence.strip()  # remove extra spaces
    
    if shout:
        sentence = sentence.upper()
    if reverse:
        sentence = sentence[::-1]
    
    # Counts
    char_count = len(sentence)
    words = sentence.split()
    word_count = len(words)
    vowels = sum(1 for c in sentence.lower() if c in "aeiou")
    consonants = sum(1 for c in sentence.lower() if c.isalpha() and c not in "aeiou")
    
    # Return results as dictionary
    return {
        "processed_sentence": sentence,
        "characters": char_count,
        "words": word_count,
        "vowels": vowels,
        "consonants": consonants
    }
text = "Hello Python World!"
result = analyze_sentence(text, shout=True, reverse=False)

print("Processed Sentence:", result["processed_sentence"])
print("Character Count:", result["characters"])
print("Word Count:", result["words"])
print("Vowel Count:", result["vowels"])
print("Consonant Count:", result["consonants"])
