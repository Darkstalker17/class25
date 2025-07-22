'''Hands-on Map
Outline:
Write a program to return the addition of numbers of two different lists.
Then, display a list that is square of numbers of another list. Use the map()
function here to get the desired result.'''
'''nums = [1, 2, 3, 4, 5]
def square(n):
    return n**2
mySquare = list(map(square, nums))
print(mySquare)
list1 = [3, 5, 7, 9]
list2 = [2, 4, 6, 8]
myadd = list(map(lambda x, y : x+y, list1, list2))
print(myadd)

sq = [1, 2, 3, 4, 5]
mysq = list(map(lambda x : x**2, sq))
print(mysq)'''
'''Zip It!
Outline:
Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together,
but 2nd list in reverse order 3. elements of two lists zipped into a dictionary'''
l1 = [1, 3, 5, 7, 9]
l2 = ["a", "c", "e", "g", "h"]
#l3 = list(zip(l1, l2))
#print(l3)
#reverse = l2[::-1]
#l3 = list(zip(l1, reverse))
#print(l3)
l3 = dict(zip(l1, l2))
print(l3)
'''Thats the exit
Outline:
Write a program where the value of i begins from 1 and goes to 10.
When the value of i becomes 5, force the interpreter to exit the program.'''
for i in range(1, 11):
    print(i)
    if i == 5:
        exit()