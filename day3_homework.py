# Exercise #1
# Filter out all of the empty strings from the list below

places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']

def words(l):
    just_places = list(filter(None, [i.strip() for i in l]))    
    return just_places
print (words(places))

#############################################################################
# Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

authors.sort(key = lambda x: x.split(" ")[-1].lower())
print(authors)

##############################################################################

# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

convert = lambda n: (n[0], n[1] * (9/5) + 32)
print (list(map(convert, places)))


##############################################################################


# Exercise #4
# Write a recursive function to perform the fibonacci sequence up to the number passed in.

dict = {}
def fib_seq(n):
    if n in dict:
        return dict[n]
    
    if n == 1:
        res = 1
    elif n ==2:
        res = 1
    elif n > 2:
        res = fib_seq(n-1) + fib_seq(n-2)
    dict[n] = res
    return res

for n in range(1, 11):
    print (n, ":", fib_seq(n))

