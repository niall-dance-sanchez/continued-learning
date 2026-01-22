"""Unreasonable checksum"""

# Write a program to validate strings against a check value.
# The check value is a decimal number representing
# The length of the longest consonant cluster in the string
# The number of vowels in the string

# Examples:
# tooth, 2.2 -> True  (th is the longest consonant cluster, o is the only vowel and appears twice)
# strength, 4.1 -> True
# absolution, 2.5 -> True
# merciful, 1.1 -> False

VOWELS = ["a", "e", "i", "o", "u"]


def get_consonant_cluster_length(word: str) -> int:
    """Finds the length of the longest consonant cluster in a word."""

    length = 0
    lengths = []

    for i in range(len(word)):
        if word[i] not in VOWELS:
            length += 1

            # account for consonant clusters at the end of a word
            if i == len(word)-1:
                lengths.append(length)
        else:
            lengths.append(length)
            length = 0

    return max(lengths)


def get_vowel_count(word: str) -> int:
    """Finds the number of vowels in a word."""

    word_vowels = [i for i in range(len(word)) if word[i] in VOWELS]

    return len(word_vowels)


def validate_string(word: str, check_value: float) -> bool:
    """
    Validates strings against a check value. 
    The check value is a decimal number representing:
        - The length of the longest consonant cluster in the string
        - The number of vowels in the string
    Returns True if both of these are satisfied, False otherwise.     
    """

    consonant_length, vowel_count = str(check_value).split(".")

    if (int(consonant_length) == get_consonant_cluster_length(word) and
            int(vowel_count) == get_vowel_count(word)):
        return True

    return False
