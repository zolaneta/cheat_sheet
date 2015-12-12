
#Escape with /
sentence = " You \n are \n the best\n in the world" # start from new line
sentence = " You \t are \t the best\t in the world\n" # add space
sentence = " \"quote\" \\"  # \\ to print \ # keep the "" in the string

# Split()  Join()
string = " I love the kind of life that I have "
string = string.split()
string = ' '.join(string)

string = "i am . so cool."  
string = string.strip('.') # removes ... from the END
string = string.capitalize() # capitalize the first word
string = string.title()   # capitalize all words
string = string.upper()   # all letters capital
string = string.lower()  # all letters lowercase
string = string.swapcase() # swap upper- and lowercase


#Lists
list1 = ["Aneta", "Ada", "Wanda"]
list2 = ["Tod"]
list3 = ["Anna"]

list1.append("Ana") # adds elements 
list1.extend(list2)  #adds 2 to 1
list1 += list2  # also adds 2 to 1
list1.append(list2)   # list1 = ["Aneta", "Ada", "Wanda", ["Tod"]]
list1.insert(1, "Aga")  # adds to index position 1

del list1[2]
list1.remove("Aneta")
list1.pop(1)
list3.index("Anna") # 1

#Test for a value with in
"Anna" in list3 #True3

list3.count("Anna") # how many times it appears in a list
 
friends = ["Harry", "Ana", "Todd"]
separator = '*'
joined_friends = separator.join(friends) # 'Harry*Ana*Todd'
separated_friends = joined_friends.split(separator)  # ["Harry", "Ana", "Todd"]

sorted_list1 = sorted(list1) #sorts alfabetically creates a copy
list1.sort() # sorts and changes the list
len(list1)  #get length

#coping a whole list
a = [1, 2, 3]
import copy
b = copy.copy(a)    # b c d are new objects that don't refer to a
c = list(a)     
d = a[:]    # changing a doesn't not affect b c d
e = a    # e refers to the same object as a, changing a changes e

#Tuples
empty_tuple = ()   
one_element = "Aneta",   #comma at the end    #() are optional
many_elements = "Ata", "Anetka", "Ada"   # no comma at the end #Python adds ()
#convert list to tuple
list_a = [1, 2, 3]
tuple(list_a)   # (1, 2, 3)

#Dictionaries (maps, arrays, hashes)
empty_dic = {}
dict([(1,2), (4,2), (3,2)]) #{1: 2, 3: 2, 4: 2}  #11.7%
first_dic = {1: 2, 3: 2, 4: 2}
second_dic = {1: 3, 3: 3, 5: 2}
first_dic.update(second_dic) # updates first_dic and overrides keys that are the same
del first_dic [1] # delete Item by key
first_dic.clear()  # delete all items
1 in second_dic  # test for key
second_dic[1] # 3  # get item by key
second_dic.get(1) # 3  # get item using get() function
second_dic.keys()  # get all keys using keys() function
second_dic.values() # get all values 
list(second_dic.items()) # get all key-value pairs

#Sets
empty_set = set()
set1 = {6, 2, 4, 6, 8}
list1= [9, 2, 3]
set2 = set(list1) # convert list to set

# \ backslash
print "I want to stay on the same line", "but I need to go to\
the next liene so I am using \ backslash"

#LOOP
rabbits = ['Flops', 'Colps', 'Tid']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current +=1
# a better way!!
for rabbit in rabbits:
    print(rabbit)

#zip()
for l1, l2, l3 in zip(list1, list2, list3):
    print (l1, "l1 content", l2, "l2 content........")
#zip() to pair tuples
eng = "Mon" , "Tue"
fr = "Lundi", "Mardi"
list(zip(eng, fr))  #[('Mon', 'Lundi'), ('Tue', 'Mardi')]

# range()
# range(start, stop, step) omit start and it begins at 0, the only required is stop
# default value of step is 1, go backward with -1.
list(range(0, -11, -2)) # [0, -2, -4, -6, -8, -10]

# List Comprehension
number_list = [number-1 for number in range(1,6) if number % 2 == 1]# automatically appends number-1
#example 
even = [x for x in range(0,10,2)]
b = [x for x in range(10) if x%2 == 0]
print even, b
# Dictionary Comprehension
word = 'letters'
letter_count = {letter: word.count(letter) for letter in word}# {'s': 1, 'r': 1, 'e': 2, 'l': 1, 't': 2}

# Tuples do not have comprehension  ?? generator comprehension??

# Gather Positional Arguments with *
# groups into a tuple 
def print_all(item1, item2, *rest):
    print "1", item1
    print "2", item2
    print "all the rest", rest    # all the rest ('5', '6', '7')
print_all( "one", "two", "5", "6", "7")

# Keyword Arguments **
# groups into a dictionary
def print_manue(**kwargs):
    print 'Todays manue:', kwargs
print_manue(wine='merlot', entree='steak', dessert='flan')#Todays manue: {'dessert': 'flan', 'entree': 'steak', 'wine': 'merlot'}

# Docstrings

def docstrings():
    'these are docstrings, readability counts'
    

    '''
    You can also use three quotes for lond docstings
    like the one here
    '''
# to print docstrings
def function_name():
    print "how to print docstrings?"
help(function_name)
# or
print(function_name.__doc__)

### Functions are First-Calss Citizens
### you can assign them as variables, use them as arguments to other functions, and return then from functions!!!!!!

# Lambda    # when you need many small, quick functions that you are not going to reuse
word_list = ['hello', 'haha', 'me']
def edit_story(words, func):
    for word in words:
        print (func(word))
edit_story(word_list, lambda word: word.capitalize() + '!')

# Module Path Search

import sys
for place in sys.path:
    print(place)



class Person():
    def __init__(self, name):
        self.name = name

# creating an object from the Perso class

aneta = Person('Aneta Zolkiewicz')
print aneta.name

# subclass
class EmailPerson(Person):
    def __init__(self, name, email):
      #  super().__init__()  #super gets the definition of the parent class
        self.name = name
        self.email = email
        
aneta = EmailPerson('Aneta', 'zolaneta@yahoo.com')
print aneta.name
print aneta.email


# FORMATING with %

# %s  sring             "cheese"
# %d  decimal integer    42
# %f  decimal float      7.03
# %%  a literal %
print '%d%%' %100  # 100%

# FORMATING with {}
print "I want to have %d dollars in my account" %1000
print "I want to have {} or {} dollars in my account".format(1000,2000)

#CSV
import csv
dic = [
    ['hello', 'czesc'],
    ['love', 'kocham'],
    ['bear', 'mis']   
    ]
with open('dic', 'wt')as polish:
    #a context manager
    csvout = csv.writer(polish)
    csvout.writerows(dic)

import os
name = 'B.py'
print os.path.exists(name)
print os.path.isfile(name)
print os.path.isdir(name)
print os.path.abspath(name) #prints the path
print os.path.realpath(name)
#os.remove(name)


#Interesting links for finance
# https://www.quantopian.com/algorithms/5667163bc244ce1b94000012
# http://gbeced.github.io/pyalgotrade/
# https://www.quandl.com/


# isinstance() #checking if it is a list
name = ["Ana", "Ela"]
isinstance(name, list)
#True
num = 5
isinstance(num, list)
#False




































