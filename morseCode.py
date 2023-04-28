# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def translate_to_morse_code(text):
    """
    Translates text to Morse code using the Morse code dictionary.

    Args:
        text (str): The input text to be translated to Morse code.

    Returns:
        str: The input text translated to Morse code.
    """
    morse_code_text = ""
    for char in text:
        if char.upper() in morse_code:
            # Add Morse code representation for the character
            morse_code_text += morse_code[char.upper()] + " "
        elif char == " ":
            # Add forward slash to represent a space
            morse_code_text += "/"
        else:
            # Add the character as-is (e.g. punctuation or special character)
            morse_code_text += char
    # Remove trailing space character
    morse_code_text = morse_code_text.rstrip()
    return morse_code_text

# Main program loop
while True:
    # Prompt user for input text
    user_input = input("Enter text to translate to Morse code (press q to quit): ")
    if user_input.lower() == "q":
        # Exit the program loop if user enters "q"
        break
    # Translate the user's input text to Morse code
    morse_code_output = translate_to_morse_code(user_input)
    # Print the Morse code output
    print(morse_code_output)
