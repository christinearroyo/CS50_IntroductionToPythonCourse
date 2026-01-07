import emoji

def main():
    # Prompt user for input
    text = input("Input: ")
    
    # Convert emoji codes to emojis
    emojized_text = emoji.emojize(text, language='alias')
    
    # Output the result
    print(f"Output: {emojized_text}")

if __name__ == "__main__":
    main()