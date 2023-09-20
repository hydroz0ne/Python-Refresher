#PRefresher Activity 5
def numlist(list):
    result = 1
    for item in list:
        result = result * item
    return result

list = [2, 4, 6, 8]
result = numlist(list)
print('The result is:', result)