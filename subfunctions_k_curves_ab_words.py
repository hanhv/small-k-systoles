# add letter at the end of a word
def add_letters(word):
    output = []
    last_char = word[-1]

    if last_char == 'a':
        output.append(word + 'a')
        output.append(word + 'b')
        output.append(word + 'B')
    elif last_char == 'A':
        output.append(word + 'A')
        output.append(word + 'b')
        output.append(word + 'B')
    elif last_char == 'b':
        output.append(word + 'b')
        output.append(word + 'a')
        output.append(word + 'A')
    elif last_char == 'B':
        output.append(word + 'B')
        output.append(word + 'a')
        output.append(word + 'A')
    return output

######################################################################
# check if an ab-word is reduced
def is_reduce_ab(word):
    # Check the pair (initial, end) first
    initial_char = word[0]
    end_char = word[-1]
    if ((initial_char == 'a' and end_char == 'A') or
            (initial_char == 'A' and end_char == 'a') or
            (initial_char == 'b' and end_char == 'B') or
            (initial_char == 'B' and end_char == 'b')):
        return False  # not reduced

    # If (initial, end) reduced, check consecutive chars
    for i in range(len(word) - 1):
        current_char = word[i]
        next_char = word[i + 1]
        if ((current_char == 'a' and next_char == 'A') or
                (current_char == 'A' and next_char == 'a') or
                (current_char == 'b' and next_char == 'B') or
                (current_char == 'B' and next_char == 'b')):
            return False  # not reduced

    return True


######################################################################
# our words start from a
def count_transitions(word):
    transitions = 0
    # Loop through the word and check adjacent characters
    for i in range(len(word) - 1):
        current_char = word[i]
        next_char = word[i + 1]
        # Check if transition from a/A to b/B occurs
        if (current_char in ['a', 'A']) and (next_char in ['b', 'B']):
            transitions += 1
    return transitions

# get my back word a^kB
def construct_word(intersection_k):
    # Create a word with 'intersection_k' number of small 'a's followed by a single 'B'
    my_back = 'a' * intersection_k + 'B'
    return my_back

# test
# print(construct_word(1))


#################################################################################
#################################################################################

