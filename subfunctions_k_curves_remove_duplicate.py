# This is to remove duplicated words in the set of plausible k-systoles

def is_duplicate(word, word_set):
    is_this_duplicate = False  # not duplicate
    word_rotation_set = rotation_set(word)

    inverse_word = find_inverse(word)
    inverse_rotation_set = rotation_set(inverse_word)

    # Add the inverse rotations to word_rotation_set
    word_rotation_set.extend(inverse_rotation_set)

    flag = False
    for current_in_set in word_set:
        for current_rotate in word_rotation_set:
            if current_rotate == current_in_set:
                is_this_duplicate = True  # duplicate
                flag = True
                break
        if flag:
            break

    return is_this_duplicate


def rotation_set(word):
    output_rotation_set = [word]  # Initialize the set with the original word
    for i in range(1, len(word)):
        word = rotate_once(word)
        output_rotation_set.append(word)

    return output_rotation_set


def rotate_once(word):
    # Rotate the word by moving the first character to the end
    output = word[1:] + word[0]
    return output


def find_inverse(word):
    inverse_word = ''
    for char in reversed(word):  # Iterates over the word in reverse
        if char == 'a':
            inverse_word += 'A'
        elif char == 'b':
            inverse_word += 'B'
        elif char == 'A':
            inverse_word += 'a'
        elif char == 'B':
            inverse_word += 'b'

    return inverse_word


