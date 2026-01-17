def first_non_repeating_character(s):
    """
    Function to find the first non-repeating character in a string.

    Parameters:
    s (str): Input string

    Returns:
    str or None: First non-repeating character or None if not found
    """

    # Dictionary to store character frequencies
    freq = {}

    # Count frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Find the first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char

    return None


# Example usage
if __name__ == "__main__":
    s = "analytics"
    result = first_non_repeating_character(s)

    if result:
        print("First non-repeating character:", result)
    else:
        print("No non-repeating character found")