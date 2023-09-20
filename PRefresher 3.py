#PRefresher Activity 3
def tupledict(tuple):
    return {key: value for key, value in tuple}

tuple = (('d', 1), ('o', 2) ,('g', 3))
dict_tuple = tupledict(tuple)
print('Tuple to dictionary:', dict_tuple)