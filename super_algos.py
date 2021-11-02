def find_min(element):
    """
    find_min(element) function takes element as a parameter, which is a list
    of integers. Function uses recursion and will return the minimum element
    from the list, or -1 if any element is not an integer.
    """

    if len(element) == 0:
        return -1
    elif len(element) == 1:
        return element[0]
    elif type(element[0]) != int or type(element[1]) != int:
        return -1
    elif element[0] < element[1]:
        element.pop(1)
        return find_min(element)
    else:
        element.pop(0)
        return find_min(element)


def sum_all(element):
    """
    sum_all(element) function takes element as a parameter, which is a list
    of integers. Function uses recursion and will return the sum of the elements
    from the list, or -1 if any element is not an integer.
    """

    if len(element) == 0:
        return -1
    elif len(element) == 1:
        return element[0]
    elif type(element[0]) != int or type(element[1]) != int:
        return -1
    else:
        element[0] += element[1]
        element.pop(1)
        return sum_all(element)


def find_possible_strings(character_set, n):
    """
    find_possible_strings(character_set, n) function takes character_set and
    n as parameters. character_set is a list of characters, and n is an
    integer. Function returns another function that uses recursion to return
    a list of all possible strings of length n using the characters from
    character_set. If character_set contains invalid characters then an empty
    list is returned.
    """

    k = len(character_set)
    return possible_strings_rec(character_set, "", k, n, [])


def possible_strings_rec(character_set, prefix, k, n, prefix_list):
    """
    possible_strings_rec(character_set, prefix, k, n, prefix_list) takes
    character_set, prefix, k, n, prefix_list as parameters. character_set is
    a list of characters, prefix is a string, k and n are integers,
    prefix_list is a list of strings. Function uses recursion to return
    a list of all possible strings of length n using the characters from
    character_set. If character_set contains invalid characters then an empty
    list is returned.
    """
    if n == 0:
        prefix_list.append(prefix)
        return

    for i in range(k):
        if type(character_set[i]) == str and character_set[i].rstrip() != "":
            newPrefix = prefix + character_set[i]
            possible_strings_rec(character_set, newPrefix, k, n - 1, prefix_list)
        else:
            return []

    if len(prefix_list) == pow(k, n):
        return prefix_list
