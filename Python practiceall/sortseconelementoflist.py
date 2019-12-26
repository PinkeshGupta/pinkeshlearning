def sortel(items):
    return items[-1]
def sortelsec(tuples):

  return sorted(tuples, key=sortel)
print(sortelsec([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# def last(n): return n[-1]

# def sort_list_last(tuples):
#   return sorted(tuples, key=last)

# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
