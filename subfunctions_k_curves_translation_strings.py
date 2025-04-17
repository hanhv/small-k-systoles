## This is to translate ab-words to efg-words and compute the number of strings.

def translate_to_efg(word):
    word_efg = ''
    for char in word:
        if char == 'a':
            word_efg += 'Ef'
        elif char == 'b':
            word_efg += 'Fg'
        elif char == 'A':
            word_efg += 'Fe'
        elif char == 'B':
            word_efg += 'Gf'
    return word_efg


def reducing_efg(word):
    word, output = is_reduce_efg(word)
    while output == 0:
        word, output = is_reduce_efg(word)
    return word


def is_reduce_efg(word):
    new_word = word
    output = 1  # yes reduced
    # Check the pair (initial, end) first
    initial_char = word[0]
    end_char = word[-1]

    if (initial_char == 'e' and end_char == 'E') or \
            (initial_char == 'E' and end_char == 'e') or \
            (initial_char == 'f' and end_char == 'F') or \
            (initial_char == 'F' and end_char == 'f') or \
            (initial_char == 'g' and end_char == 'G') or \
            (initial_char == 'G' and end_char == 'g'):
        output = 0  # not reduced
        new_word = word[1:-1]  # Remove first and last characters
        return new_word, output
    else:
        # If (initial, end) reduced, check consecutive chars
        i = 0
        while i < len(word) - 1:
            current_char = word[i]
            next_char = word[i + 1]

            if (current_char == 'e' and next_char == 'E') or \
                    (current_char == 'E' and next_char == 'e') or \
                    (current_char == 'f' and next_char == 'F') or \
                    (current_char == 'F' and next_char == 'f') or \
                    (current_char == 'g' and next_char == 'G') or \
                    (current_char == 'G' and next_char == 'g'):
                output = 0  # not reduced
                new_word = word[:i] + word[i + 2:]  # Remove the pair
                return new_word, output
            i += 1
    return new_word, output


def num_strings(word):
    return len(reducing_efg(translate_to_efg(word)))