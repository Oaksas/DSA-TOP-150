
def commonString(strs):
    strs.sort()

    first_string = strs[0]
    last_string = strs[-1]

    common = []

    for i in range(len(first_string)):
        if i < len(last_string) and first_string[i] == last_string[i]:
            common.append(first_string[i])
        else:
            break
    common_prefix = ''.join(common)
    return common_prefix


print(commonString(["fd", "fdf", "fdsaf", "fdsd"]))
