def remove_special_characters(text):
    """
    Remove special characters from the input string.
    Keeps only alphabets and numbers.
    """

    result = ""

    for char in text:
        if char.isalnum() or char == " ":
            result += char

    return result


# Driver code
if __name__ == "__main__":
    input_string = "Data@Analytics#2025!"
    cleaned_string = remove_special_characters(input_string)
    print("Original String:", input_string)
    print("Cleaned String:", cleaned_string)