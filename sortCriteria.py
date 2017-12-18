def sort_criteria(header_row):
    '''
    tuple --> tuple

    takes in a tuple (in THIS case, in the form of the header row of an OpenPyXL worksheet object)
    returns a tuple of indexes to be used as keys by itemgetter for sorting criteria.
    '''

    sort_list = []
    criteria = ('CC', 'Company', 'Employee Name') #the terms we're looking for to find our sorting indexes

    for c in criteria:
        for i in header_row:
            if i.value == c:
                sort_list.append(header_row.index(i))
    sort_tuple = tuple(sort_list)
    return sort_tuple