import numpy as np
from subfunctions_intersection import *
from subfunctions_intersection_check_j_right_i import *


def intersection(word):
    primitive, power = is_primitive(word)
    if power == 1:  # primitive
        return intersection_primitive(word)
    elif power >= 1:  # non-primitive
        return power * power * intersection_primitive(primitive) + power - 1


def intersection_primitive(word):
    number_of_intersection = -1
    my_starting_seam = starting_seam(word)
    _, power = is_primitive(word)

    if power == 1:  # primitive
        number_of_intersection = 0
        word_length = len(word)
        matrix = np.zeros((word_length, word_length))  # Use a numpy matrix for tracking

        for i in range(word_length - 1):
            wi = my_starting_seam[i] + word[i]  # concatenate inverseWord(i) and word(i)

            for j in range(i + 1, word_length):
                wj = my_starting_seam[j] + word[j]  # concatenate inverseWord(j) and word(j)

                # check if wi intersects wj
                if matrix[i, j] == 0:  # if not checked yet
                    if matrix[j, i] != 0:
                        matrix[i, j] = matrix[j, i]
                    else:
                        matrix[i, j] = 1  # mark as checked

                        # Case 1: Intersect immediately
                        if (
                                (wi in ['ab', 'ba'] and wj in ['AB', 'BA']) or
                                (wi in ['AB', 'BA'] and wj in ['ab', 'ba'])
                        ):
                            number_of_intersection += 1

                        # Case 2: never intersect
                        ###################################################################################
                        ###################################################################################
                        # Case 3: start and end at the same letters
                        if wi[0] == wj[0] and wi[1] == wj[1]:
                            # Start Forward
                            forward = 0  # Forward until they end at different letters

                            index_i_forward = i
                            index_j_forward = j

                            while word[index_i_forward] == word[index_j_forward]:
                                matrix[index_i_forward, index_j_forward] = 1  # mark as checked
                                forward += 1
                                index_i_forward = (i + forward) % word_length
                                index_j_forward = (j + forward) % word_length

                                if forward > word_length:
                                    break

                            start_ij_forward = my_starting_seam[index_i_forward]
                            end_i_forward = word[index_i_forward]
                            end_j_forward = word[index_j_forward]
                            matrix[index_i_forward, index_j_forward] = 1  # mark as checked

                            w_i_done_forward = start_ij_forward + end_i_forward
                            w_j_done_forward = start_ij_forward + end_j_forward

                            forward_j_right_of_i = check_j_right_i(w_i_done_forward, w_j_done_forward)

                            # Start Backward
                            backward = 0  # Backward until they end at different letters

                            index_i_backward = i
                            index_j_backward = j

                            while my_starting_seam[index_i_backward] == my_starting_seam[index_j_backward]:
                                matrix[index_i_backward, index_j_backward] = 1  # mark as checked
                                backward += 1
                                index_i_backward = (i - backward) % word_length
                                index_j_backward = (j - backward) % word_length

                                if backward > word_length:
                                    break

                            end_i_backward = word[index_i_backward]
                            start_i_backward = my_starting_seam[index_i_backward]
                            start_j_backward = my_starting_seam[index_j_backward]
                            matrix[index_i_backward, index_j_backward] = 1  # mark as checked

                            w_i_done_backward = start_i_backward + end_i_backward
                            w_j_done_backward = start_j_backward + end_i_backward

                            backward_j_right_of_i = check_j_right_i(w_i_done_backward, w_j_done_backward)

                            if forward_j_right_of_i != backward_j_right_of_i:
                                number_of_intersection += 1
                        # DONE CASE 3
                        ###################################################################################
                        ###################################################################################
                        # Case 4: start from different letters, end at the same, same direction.
                        if wi[0] != wj[0] and wi[1] == wj[1]:
                            # 1 immediately know from the picture: j is left or right of i.
                            # current picture: know immediately. THE SAME AS BACKWARD IN CASE 3.
                            current_j_right_i = check_j_right_i(wi, wj)

                            # FORWARD wi, wj: THE SAME AS CASE 3 FORWARD PART.
                            # /////////////////////////////////////////////////////

                            # START FORWARD
                            kforward = 0

                            indexiforward = i
                            indexjforward = j

                            # forward until wi end wj end at different letters.
                            while word[indexiforward] == word[indexjforward]:
                                matrix[indexiforward, indexjforward] = 1
                                # mark cell(i+k mod l, j+k mod l) as checked.
                                kforward += 1
                                indexiforward = (i + kforward) % word_length
                                indexjforward = (j + kforward) % word_length

                                if kforward > word_length:
                                    break

                            # after forwarding k times:
                            matrix[indexiforward, indexjforward] = 1
                            # mark cell(i+k mod l, j+k mod l) as checked.

                            # starting letter of wi and wj
                            startijforward = my_starting_seam[indexiforward]
                            # ending letter of wi
                            endiforward = word[indexiforward]
                            # ending letter of wj
                            endjforward = word[indexjforward]

                            wi_done_forward = startijforward + endiforward
                            wj_done_forward = startijforward + endjforward

                            # from (charStartij, charEndi, charEndj), decide j left or right of i.
                            forward_j_right_of_i = check_j_right_i(wi_done_forward, wj_done_forward)
                            # if not considering, j is on the left of i automatically.
                            # FINISH FORWARD.

                            if current_j_right_i != forward_j_right_of_i:
                                number_of_intersection += 1
                        # DONE CASE 4
                        ###################################################################################
                        ###################################################################################
                        # CASE 5
                        # case 5: start from the same letter, end at different.
                        if wi[0] == wj[0] and wi[1] != wj[1]:
                            # 1 : immediately know from the picture
                            # and 1 : backward wi and wj
                            # CURRENT PICTURE THE SAME AS FORWARD CASE 3, CASE 4.
                            # from the picture: know immediately.
                            currentJRightOfI = check_j_right_i(wi, wj)
                            # ///////////////////////////////////////////////////

                            # START BACKWARD.
                            # the same as case 3: backward part.
                            # backward wi, backward wj.
                            kbackward = 0
                            indexibackward = i
                            indexjbackward = j

                            # backward until wi end wj start from different letters.
                            while my_starting_seam[indexibackward] == my_starting_seam[indexjbackward]:
                                matrix[indexibackward][indexjbackward] = 1
                                # mark cell(i-k mod l, j-k mod l) as checked.
                                kbackward += 1

                                indexibackward = (i - kbackward) % word_length
                                indexjbackward = (j - kbackward) % word_length

                                if kbackward > word_length:
                                    break
                            # now wi and wj start from different letters, and end at the same letter.

                            # after backwarding k times:
                            # ending letter of wi and wj the same
                            endijbackward = word[indexibackward]
                            # starting letter of wi
                            startibackward = my_starting_seam[indexibackward]
                            # starting letter of wj
                            startjbackward = my_starting_seam[indexjbackward]

                            w_i_done_backward = startibackward + endijbackward
                            w_j_done_backward = startjbackward + endijbackward

                            # from (charStarti, charStartj, charEndij), decide j left or right of i.
                            backwardJRightOfI = check_j_right_i(w_i_done_backward, w_j_done_backward)
                            # if not considering, j is on the left of i automatically.
                            # RETURN False if j is on the left of i
                            # RETURN True if j is on the right of i

                            matrix[indexibackward][indexjbackward] = 1
                            # mark cell(i-k mod l, j-k mod l) as checked.

                            # FINISH BACKWARD

                            if currentJRightOfI != backwardJRightOfI:
                                number_of_intersection += 1

                        # end case 5.
                        # DONE CASE 5
                        ###################################################################################
                        ###################################################################################

                        ###################################################################################
                        ###################################################################################
                        # CASE 6
                        # Case 6: Same 2 letters, different direction.
                        # Start i = end j
                        # End i = start j
                        if wi[0] == wj[1] and wi[1] == wj[0]:
                            # (forward i, backward j)
                            # (backward i, forward j)

                            # START FORWARD i, BACKWARD j:
                            kforwardibackwardj = 0
                            indexiforward = i
                            indexjbackward = j

                            while word[indexiforward] == my_starting_seam[indexjbackward]:
                                matrix[indexiforward, indexjbackward] = 1

                                kforwardibackwardj += 1
                                indexiforward = (i + kforwardibackwardj) % word_length
                                indexjbackward = (j - kforwardibackwardj) % word_length

                                if kforwardibackwardj > word_length:
                                    break

                            # Now after k times forward i and backward j,
                            # start(wi) = end(wj) and end(wi) different start(wj):
                            startiendj = my_starting_seam[indexiforward]
                            endiforward = word[indexiforward]
                            startjbackward = my_starting_seam[indexjbackward]

                            wi_done1 = startiendj + endiforward
                            wj_done1 = startjbackward + startiendj
                            iforwardjbackwardJRightOfI = check_j_right_i(wi_done1, wj_done1)

                            matrix[indexiforward, indexjbackward] = 1
                            # mark the cell (i+k mod l, j-k mod l) as checked.

                            # FINISH FORWARD i BACKWARD j.
                            # ///////////////////////////////

                            # START BACKWARD i, FORWARD j:
                            # Backward i forward j
                            ibackwardjforwardJRightOfI = 0  # if not considered, wj is on the left of wi.

                            kbackwardiforwardj = 0

                            indexibackward = i
                            indexjforward = j

                            while my_starting_seam[indexibackward] == word[indexjforward]:
                                matrix[indexibackward, indexjforward] = 1
                                # mark cell (i-k mod l, j+k mod l) as checked
                                kbackwardiforwardj += 1

                                indexibackward = (i - kbackwardiforwardj) % word_length
                                indexjforward = (j + kbackwardiforwardj) % word_length

                                if kbackwardiforwardj > word_length:
                                    break

                            # After k times backward i, forward j:
                            # start wi different end wj
                            # end wi = start wj
                            endistartj = word[indexibackward]
                            startibackward = my_starting_seam[indexibackward]
                            endjforward = word[indexjforward]

                            # (endistartj, startibackward, endjforward) to function left or right
                            wi_done2 = startibackward + endistartj
                            wj_done2 = endistartj + endjforward
                            ibackwardjforwardJRightOfI = check_j_right_i(wi_done2, wj_done2)

                            matrix[indexibackward, indexjforward] = 1
                            # mark cell (i-k mod l, j+k mod l) as checked

                            # END BACKWARD i, FORWARD j.

                            if iforwardjbackwardJRightOfI != ibackwardjforwardJRightOfI:
                                number_of_intersection += 1

                        # DONE CASE 6
                        ###################################################################################
                        ###################################################################################
                        # CASE 7
                        # Case 7: the end of wi = the start of wj, start i different end j.
                        if wi[1] == wj[0] and wi[0] != wj[1]:
                            # From current picture, know immediately 1 thing.
                            # CURRENT PICTURE THE SAME AS CASE 6 BACKWARD I FORWARD J
                            currentJRightOfI = check_j_right_i(wi, wj)
                            # Finish current picture.
                            # /////////////////////////////

                            # Now forward i, backward j
                            # THE SAME AS CASE 6 FORWARD I BACKWARD J
                            iforwardjbackwardJRightOfI = 0  # if not considered, wj is on the left of wi.

                            # START FORWARD i, BACKWARD j:
                            kforwardibackwardj = 0

                            indexiforward = i
                            indexjbackward = j

                            while word[indexiforward] == my_starting_seam[indexjbackward]:
                                matrix[indexiforward, indexjbackward] = 1
                                # Mark the cell (i+k mod l, j-k mod l) as checked.
                                kforwardibackwardj += 1
                                indexiforward = (i + kforwardibackwardj) % word_length
                                indexjbackward = (j - kforwardibackwardj) % word_length

                                if kforwardibackwardj > word_length:
                                    break

                            # After k times forward i and backward j,
                            # start(wi) = end(wj) and end(wi) different start(wj):

                            startiendj = my_starting_seam[indexiforward]
                            endiforward = word[indexiforward]
                            startjbackward = my_starting_seam[indexjbackward]
                            case7_done_wi = startiendj + endiforward
                            case7_done_wj = startjbackward + startiendj

                            # (startiendj, endiforward, startjbackward) to function left or right
                            # wj is on the right of wi
                            iforwardjbackwardJRightOfI = check_j_right_i(case7_done_wi, case7_done_wj)

                            matrix[indexiforward, indexjbackward] = 1
                            # Mark the cell (i+k mod l, j-k mod l) as checked. % here java file + wordLength

                            # FINISH FORWARD i BACKWARD j.
                            # ///////////////////////////////

                            if currentJRightOfI != iforwardjbackwardJRightOfI:
                                number_of_intersection += 1

                        # DONE CASE 7
                        ###################################################################################
                        ###################################################################################

                        # CASE 8
                        # Case 8: start i = end j, end i different start j
                        if (wi[0] == wj[1] and wi[1] != wj[0]):
                            # Current picture, know immediately 1 thing
                            # Current picture the same as case 6 and case 7: forward i, backward j
                            currentJRightOfI = check_j_right_i(wi, wj)

                            # Now backward i, forward j
                            kbackwardiforwardj = 0

                            indexibackward = i
                            indexjforward = j

                            while my_starting_seam[indexibackward] == word[indexjforward]:
                                matrix[indexibackward][indexjforward] = 1
                                # Mark cell (i-k mod l, j+k mod l) as checked
                                kbackwardiforwardj += 1

                                indexibackward = (i - kbackwardiforwardj) % word_length
                                indexjforward = (j + kbackwardiforwardj) % word_length

                                if kbackwardiforwardj > word_length:
                                    break

                            # After k times backward i, forward j:
                            endistartj = word[indexibackward]
                            startibackward = my_starting_seam[indexibackward]
                            endjforward = word[indexjforward]

                            case8_done_wi = startibackward + endistartj
                            case8_done_wj = endistartj + endjforward

                            ibackwardjforwardJRightOfI = check_j_right_i(case8_done_wi, case8_done_wj)

                            matrix[indexibackward][indexjforward] = 1
                            # Mark cell (i-k mod l, j+k mod l) as checked

                            # If the right-or-left status differs, increase the number of intersections
                            if currentJRightOfI != ibackwardjforwardJRightOfI:
                                number_of_intersection += 1
                        # DONE CASE 8
                        ###################################################################################
                        ###################################################################################
    return number_of_intersection


# # TEST
# my_word = 'aabab'
# my_intersection = intersection_primitive(my_word)
# print("my_word ", my_word, "my_intersection ", my_intersection)

# # # TEST
# my_word = 'abbab'
# my_intersection = intersection(my_word)
# print("my_word ", my_word, "my_intersection ", my_intersection)



