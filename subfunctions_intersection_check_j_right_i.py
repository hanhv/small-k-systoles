# input: a pair wi, wj
# output: check if wj is on the right of wi or not
# check cross pair final: after forward/ backward
# return True if j is on the right of i.
def check_j_right_i(wi, wj):
    # only check position if they have 1 common node
    # SAME START
    # wi start a
    if wi[0] == 'a':
        if (
            (wi[1] == 'A' and wj in {'ab', 'aB', 'ba', 'Ba'}) or
            (wi[1] == 'b' and wj in {'aB', 'Ba'})
        ):
            return True
    # wi start A
    elif wi[0] == 'A':
        if (
            (wi[1] == 'b' and wj in {'AB', 'Aa', 'BA', 'aA'}) or
            (wi[1] == 'B' and wj in {'Aa', 'aA'})
        ):
            return True
    # wi start b
    elif wi[0] == 'b':
        if(
            (wi[1] == 'B' and wj in {'ba', 'bA', 'ab', 'Ab'}) or
            (wi[1] == 'a' and wj in {'bA', 'Ab'})
        ):
            return True
    # wi start B
    elif wi[0] == 'B':
        if(
            (wi[1] == 'a' and wj in {'BA', 'Bb', 'AB', 'bB'}) or
            (wi[1] == 'A' and wj in {'Bb', 'bB'})
        ):
            return True

    # SAME END
    # wi end a
    if wi[1] == 'a':
        if(
            (wi[0] == 'B' and wj in {'ba', 'Aa', 'ab', 'aA'}) or
            (wi[0] == 'b' and wj in {'Aa', 'aA'})
        ):
            return True
    # wi end A
    elif wi[1] == 'A':
        if(
            (wi[0] == 'a' and wj in {'BA', 'bA', 'AB', 'Ab'}) or
            (wi[0] == 'B' and wj in {'bA', 'Ab'})
        ):
            return True
    # wi end b
    elif wi[1] == 'b':
        if(
            (wi[0] == 'A' and wj in {'ab', 'Bb', 'ba', 'bB'}) or
            (wi[0] == 'a' and wj in {'Bb', 'bB'})
        ):
            return True
    # wi end B
    elif wi[1] == 'B':
        if (
                (wi[0] == 'b' and wj in {'AB', 'aB', 'BA', 'Ba'}) or
                (wi[0] == 'A' and wj in {'aB', 'Ba'})
        ):
            return True

    return False


# wi = 'ab'
# wj = 'aB'
# print(check_j_right_i(wi, wj))

# wi = 'ab'
# wj = 'aA'
# print(check_j_right_i(wi, wj))