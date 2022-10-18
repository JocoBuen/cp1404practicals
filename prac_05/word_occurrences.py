"""
Word Occurrences
Estimate: 40 minutes
Actual:   61 minutes
"""


def main():
    text_to_number = {}
    text = input("Text: ")
    texts = text.split(" ")
    texts.sort()
    count_the_occurrences_of_words(text_to_number, texts)
    display_the_word_occurrences(text_to_number)


def display_the_word_occurrences(text_to_number):
    max_length = max(len(text) for text in text_to_number.keys())
    for text, number in text_to_number.items():
        print(f"{text:{max_length}} : {number}")


def count_the_occurrences_of_words(text_to_number, texts):
    for text in texts:
        if text in text_to_number:
            text_to_number[text] += 1
        else:
            text_to_number[text] = 1


main()

