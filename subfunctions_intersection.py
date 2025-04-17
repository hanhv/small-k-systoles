# CHECK PRIMITIVE
#  output: (primitive, power):
#  primitive is the primitive word or sub-word
#  power is 1 if it is primitive, = k if it goes around the sub-word k times
def is_primitive(word):
    power = 1  # primitive
    primitive = word
    rotate = word
    i = 1
    while i < len(word):
        rotate = rotate_once(rotate)
        if rotate == word:
            primitive = word[:i]
            power = len(word) // i
            break
        i += 1
    return primitive, power


def rotate_once(word):
    return word[1:] + word[0]


# This is to compute the seam.
# example: input 'abaBaaab', output is 'BABAbAAA'
def starting_seam(word):
    output = ''
    end_char = word[-1]

    # Invert the last character
    if end_char == 'a':
        output += 'A'
    elif end_char == 'A':
        output += 'a'
    elif end_char == 'b':
        output += 'B'
    elif end_char == 'B':
        output += 'b'

    # Invert the rest of the characters
    for current_char in word[:-1]:  # Exclude the last character
        if current_char == 'a':
            output += 'A'
        elif current_char == 'A':
            output += 'a'
        elif current_char == 'b':
            output += 'B'
        elif current_char == 'B':
            output += 'b'

    return output

# # # test
# my_word = 'abaBaaab'
# my_starting_seam = starting_seam(my_word)
# print("my word ", my_word, "my my_starting_seam word ", my_starting_seam)
# is_my_word_primitive = is_primitive(my_word)
# print("my word ", my_word, "is_my_word_primitive ", is_my_word_primitive)