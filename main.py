from subfunctions_k_curves_ab_words import *
from subfunctions_k_curves_remove_duplicate import *
from intersection import *
from subfunctions_k_curves_translation_strings import *
import pandas as pd
import os


def find_plausible_short(intersection_k):
    output_list = []
    my_back = 'a' * intersection_k + 'B'  # Multiply 'a' k times and concatenate 'B'
    num_strings_my_back = num_strings(my_back)


    list_current_short = []
    list_plausible_shortest = []
    WLBound = 2*intersection_k
    list_current_short.append(my_back)
    list_plausible_shortest.append(my_back)

    current_set = ['a']

    while True:
        new_set = []
        for current_word in current_set:
            actives = add_letters(current_word)
            for current_active in actives:
                if len(current_active) <= WLBound:
                    # if length is <= 2k then continue
                    if current_active[-1] in ['b', 'B'] and num_strings(current_active) < num_strings_my_back:
                        # if current_active is cyclically reduced and with < num strings of back geodesic
                        current_intersection = intersection(current_active)
                        if current_intersection >= intersection_k:
                            is_current_primitive = is_primitive(current_active)
                            if is_current_primitive[1] == 1:
                                list_current_short.append(current_active)
                        else:
                            # if intersection is still < k then continue generating new words
                            new_set.append(current_active)
                    else:
                        # if current_active is not cyclically reduced
                        new_set.append(current_active)
        current_set = new_set
        if not current_set:
            # if the current_set is empty
            break

    for current_short in list_current_short:
        is_this_duplicate = is_duplicate(current_short, list_plausible_shortest)
        if not is_this_duplicate:
            # if item_short not in list_plausible_shortest yet:
            list_plausible_shortest.append(current_short)

    print("\nshortest list ")
    for shortest in list_plausible_shortest:
        output_list.append([shortest, intersection(shortest)])
        print(shortest, intersection(shortest))
    return output_list


# TEST
my_intersection_k = 7
print("checking for my_intersection_k = ", my_intersection_k)
output_list = find_plausible_short(my_intersection_k)
# print("num curves ", len(output_list))

# Create output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Create DataFrame from list of [curve, self_intersection] pairs
df = pd.DataFrame(output_list, columns=["Curve", "Self-intersection"])

# Generate dynamic filename and full path
filename = f"curves_k_{my_intersection_k}.xlsx"
filepath = os.path.join(output_dir, filename)

# Save to Excel
df.to_excel(filepath, index=False)
print(f"Saved to {filepath}")

# Total words
print("Total words ", len(output_list))