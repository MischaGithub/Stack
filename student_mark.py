#Creating an array of student mark
#creating an array with integer type

my_marks = [3, 5, 6, 2, 7, 10, 45, 8, 14, 10]
def mark_array(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8, mk9,mk10):
    """

    >>> mark_array(total = [2, 5, 6, 7, 8, 10, 1, 4, 3, 11])
    57
    """
    total = (mk1+mk2+mk3+mk4+mk5+mk6+mk7+mk8+mk9+mk10) // 100

    return total


#Creating a function to determie average of the mark arrays
def average_mark(average):

    if average >= 50:
        mark = "Passed"

        return mark

    else:
        mark = "Failed"

        return mark
