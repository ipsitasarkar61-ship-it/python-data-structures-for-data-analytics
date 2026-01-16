def longest_word(sentence):
    """
    Function to find the longest word in a sentence.
    If multiple words have the same length,
    the first occurring word is returned.
    """

    # Remove leading/trailing spaces and split sentence into words
    words = sentence.strip().split()

    longest = ""

    # Traverse each word
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


# Driver code
if __name__ == "__main__":
    sentence = "Data analytics builds strong problem solving skills"
    result = longest_word(sentence)
    print("Longest word:", result)

Output:-
Longest word: analytics