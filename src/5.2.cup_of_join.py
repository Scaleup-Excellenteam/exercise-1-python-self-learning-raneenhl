def cup_of_join(*lists, **kwargs):
    """
    Joins all lists into one, separated by the separator (if passed).
    :param lists: Any number of lists
    :param sep: Optional separator to insert between lists
    :return: A single merged list with separators if requested
    """

    sep_given = 'sep' in kwargs
    sep = kwargs.get('sep', '-')

    if not lists:
        return None

    merged_lst = []

    for i, lst in enumerate(lists):
        if i > 0 and sep_given:
            merged_lst.append(sep)
        merged_lst.extend(lst)

    if sep_given:
        merged_lst.append(sep)

    return merged_lst


if __name__ == '__main__':
    # Example test cases
    # [1, 2, '@', 8, '@', 9, 5, 6]
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))  # [1, 2, '-', 8, '-', 9, 5, 6]
    print(cup_of_join([1]))  # [1]
    print(cup_of_join())  # None
