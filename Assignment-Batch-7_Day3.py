1)List and its default functions.

i)
append(x)

Adds an item (x) to the end of the list. This is equivalent to a[len(a):] = [x].


a = ["bee", "moth"]

print(a)

a.append("ant")

print(a)

Result

['bee', 'moth']
['bee', 'moth', 'ant']

ii)

insert(i, x)

Inserts an item at a given position. The first argument is the index of the element before which to insert. For example, a.insert(0, x) inserts at the front of the list.


a = ["bee", "moth"]

print(a)

a.insert(0, "ant")

print(a)

a.insert(2, "fly")

print(a)

Result

['bee', 'moth']
['ant', 'bee', 'moth']
['ant', 'bee', 'fly', 'moth']


iii)

remove(x)

Removes the first item from the list that has a value of x. Returns an error if there is no such item.


a = ["bee", "moth", "ant"]

print(a)

a.remove("moth")

print(a)

Result

['bee', 'moth', 'ant']
['bee', 'ant']

iv)

pop([i])

Removes the item at the given position in the list, and returns it. If no index is specified, pop() removes and returns the last item in the list.


# Example 1: No index specified

a = ["bee", "moth", "ant"]

print(a)

a.pop()

print(a)

​

# Example 2: Index specified

a = ["bee", "moth", "ant"]

print(a)

a.pop(1)

print(a)

Result

['bee', 'moth', 'ant']
['bee', 'moth']
['bee', 'moth', 'ant']
['bee', 'ant']

v)

clear()

Removes all items from the list. Equivalent to del a[:].


a = ["bee", "moth", "ant"]

print(a)

a.clear()

print(a)

Result

['bee', 'moth', 'ant']
[]



=============================================================================================================================================

2)Dictionary and its default functions.

i)The syntax of clear() is:

dict.clear()


clear() method doesn't take any parameters.

clear() method doesn't return any value (returns None).

Example 1: How clear() method works for dictionaries?

d = {1: "one", 2: "two"}

d.clear()
print('d =', d)

Output

d = {}


ii)

The syntax of copy() is:

dict.copy()

copy() method doesn't take any parameters

This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.

original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)

Output

Orignal:  {1: 'one', 2: 'two'}
New:  {1: 'one', 2: 'two'}


iii)

The syntax of fromkeys() method is:

dictionary.fromkeys(sequence[, value])

fromkeys() method takes two parameters:

    sequence - sequence of elements which is to be used as keys for the new dictionary
    value (Optional) - value which is set to each each element of the dictionary


fromkeys() method returns a new dictionary with the given sequence of elements as the keys of the dictionary.

If the value argument is set, each element of the newly created dictionary is set to the provided value.


# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)

Output

{'a': None, 'u': None, 'o': None, 'e': None, 'i': None}




iv)

Python Dictionary get()

The get() method returns the value for the specified key if key is in dictionary.

he syntax of get() is:

dict.get(key[, value]) 

get() Parameters

get() method takes maximum of two parameters:

    key - key to be searched in the dictionary
    value (optional) - Value to be returned if the key is not found. The default value is None.

Return Value from get()

get() method returns:

    the value for the specified key if key is in dictionary.
    None if the key is not found and value is not specified.
    value if the key is not found and value is specified.

Example 1: How get() works for dictionaries?

person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))

Output

Name:  Phill
Age:  22
Salary:  None
Salary:  0.0


iv)

Python Dictionary pop()
The pop() method removes and returns an element from a dictionary having the given key.

The syntax of pop() method is

dictionary.pop(key[, default])

pop() Parameters

pop() method takes two parameters:

    key - key which is to be searched for removal
    default - value which is to be returned when the key is not in the dictionary

Return value from pop()

The pop() method returns:

    If key is found - removed/popped element from the dictionary
    If key is not found - value specified as the second argument (default)
    If key is not found and default argument is not specified - KeyError exception is raised

Example 1: Pop an element from the dictionary

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)

Output

The popped element is: 2
The dictionary is: {'orange': 3, 'grapes': 4}



v)

Python Dictionary update()
The update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.

update() method adds element(s) to the dictionary if the key is not in the dictionary. If the key is in the dictionary, it updates the key with the new value.

The syntax of update() is:

dict.update([other])

update() Parameters

The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).

If update() is called without passing parameters, the dictionary remains unchanged.
Return Value from update()

update() method updates the dictionary with elements from a dictionary object or an iterable object of key/value pairs.

It doesn't return any value (returns None).
Example 1: Working of update()

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)

Output

{1: 'one', 2: 'two'}
{1: 'one', 2: 'two', 3: 'three'}


========================================================================================================================================

3)Sets and its default functions.

i)

Python Set add()
The set add() method adds a given element to a set. If the element is already present, it doesn't add any element.

The syntax of set add() method is:

set.add(elem)

add() method doesn't add an element to the set if it's already present in it.

Also, you don't get back a set if you use add() method when creating a set object.

noneValue = set().add(elem)

The above statement doesn't return a reference to the set but 'None', because the statement returns the return type of add which is None.
Set add() Parameters

add() method takes a single parameter:

    elem - the element that is added to the set

Return Value from Set add()

add() method doesn't return any value and returns None.
Example 1: Add an element to a set

# set of vowels
vowels = {'a', 'e', 'i', 'u'}

# adding 'o'
vowels.add('o')
print('Vowels are:', vowels)

# adding 'a' again
vowels.add('a')
print('Vowels are:', vowels)

Output

Vowels are: {'a', 'i', 'o', 'u', 'e'}
Vowels are: {'a', 'i', 'o', 'u', 'e'}

ii)


Python Set copy()
The copy() method returns a shallow copy of the set.

A set can be copied using = operator in Python. For example:

numbers = {1, 2, 3, 4}
new_numbers = numbers

The problem with copying the set in this way is that if you modify the numbers set, the new_numbers set is also modified.

numbers = {1, 2, 3, 4}
new_numbers = numbers

new_numbers.add(5)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)

Output

numbers:  {1, 2, 3, 4, 5}
new_numbers:  {1, 2, 3, 4, 5}

However, if you need the original set to be unchanged when the new set is modified, you can use the copy() method.

The syntax of copy() is:

set.copy()

copy() Parameters

It doesn't take any parameters.
Return Value from copy()

The copy() method returns a shallow copy of the set.
Example 1: How the copy() method works for sets?

numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()

new_numbers.add(5)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)

Output

numbers:  {1, 2, 3, 4}
new_numbers:  {1, 2, 3, 4, 5}

iii)

Python Set union()
The Python set union() method returns a new set with distinct elements from all the sets.

The union of two or more sets is the set of all distinct elements present in all the sets. For example:

A = {1, 2}
B = {2, 3, 4}
C = {5}

Then,
A∪B = B∪A = {1, 2, 3, 4}
A∪C = C∪A = {1, 2, 5}
B∪C = C∪B = {2, 3, 4, 5}

A∪B∪C = {1, 2, 3, 4, 5}

Union of Sets
Union of three set shown in green color

The syntax of union() is:

A.union(*other_sets)

Note: * is not part of the syntax. It is used to indicate that the method can take 0 or more arguments.
Return Value from union()

    The union() method returns a new set with elements from the set and all other sets (passed as an argument).
    If the argument is not passed to union(), it returns a shallow copy of the set.

Example 1: Working of union()

A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))
print('A.union() =', A.union())

Output

A U B = {2, 'a', 'd', 'c'}
B U C = {1, 2, 3, 'd', 'c'}
A U B U C = {1, 2, 3, 'a', 'd', 'c'}
A.union() = {'a', 'd', 'c'}

iv)

Python Set update()
The Python set update() method updates the set, adding items from other iterables.

The syntax of update() is:

A.update(iterable)

Here, A is a set, and iterable can be any iterable such as list, set, dictionary, string, etc. The elements of the iterable are added to the set A.

Let's take another example:

A.update(iter1, iter2, iter3)

Here, the elements of iterables iter1, iter2, and iter3 are added to set A.
Return Value from update()

This set update() method returns None (returns nothing).
Example 1: Python set update()

A = {'a', 'b'}
B = {1, 2, 3}

result = A.update(B)

print('A =', A)
print('result =', result)

Output

A = {'a', 1, 2, 3, 'b'}
result = None

v)

Python Set remove()
The remove() method removes the specified element from the set.

The syntax of the remove() method is:

set.remove(element)

remove() Parameters

The remove() method takes a single element as an argument and removes it from the set.
Return Value from remove()

The remove() removes the specified element from the set and updates the set. It doesn't return any value.

If the element passed to remove() doesn't exist, KeyError exception is thrown.
Example 1: Remove an Element From The Set

# language set
language = {'English', 'French', 'German'}

# removing 'German' from language
language.remove('German')

# Updated language set
print('Updated language set:', language)

Output

Updated language set: {'English', 'French'}


============================================================================================================================================

4)Tuple and explore default methods.


Python Tuples are like a list. It can hold a sequence of items. The difference is that it is immutable. Let’s learn the syntax to create a tuple in Python.

Examples :-

a. len()

Like a list, a Python tuple is of a certain length. The len() function returns its length.

    >>> my_tuple

(1, 2, 3, [6, 5])

    >>> len(my_tuple)

4

It returned 4, not 5, because the list counts as 1.
b. max()

It returns the item from the tuple with the highest value.

We can’t apply this function on the tuple my_tuple, because ints cannot be compared to a list. So let’s take yet another tuple in Python.

    >>> a=(3,1,2,5,4,6)
    >>> max(a)

6

Let’s try that on strings.

    >>> max(('Hi','hi','Hello'))

‘hi’

‘hi’ is the greatest out of these, because h has the highest ASCII value among h and H.

But you can’t compare an int and a string.

    >>> max(('Hi',9))

Traceback (most recent call last):

File “<pyshell#59>”, line 1, in <module>

max((‘Hi’,9))

TypeError: ‘>’ not supported between instances of ‘int’ and ‘str’
c. min()

Like the max() function, the min() returns the item with the lowest values.

    >>> min(a)

1

As you can see, 1 is the smallest item in this Python tuple.
d. sum()

This function returns the arithmetic sum of all the items in the tuple.

    >>> sum(a)

21

However, you can’t apply this function on a tuple with strings.

    >>> sum(('1','2','3'))

Traceback (most recent call last):

File “<pyshell#57>”, line 1, in <module>

sum((‘1′,’2′,’3’))

TypeError: unsupported operand type(s) for +: ‘int’ and ‘str’
e. any()

If even one item in the tuple has a Boolean value of True, then this function returns True. Otherwise, it returns False.

    >>> any(('','0',''))

True

The string ‘0’ does have a Boolean value of True. If it was rather the integer 0, it would’ve returned False.

    >>> any(('',0,''))

False


===========================================================================================================================================


5)Strings and explore default methods.

i)

Python String capitalize()
In Python, the capitalize() method converts first character of a string to uppercase letter and lowercases all other characters, if any.

The syntax of capitalize() is:

string.capitalize()

capitalize() Parameter

The capitalize() function doesn't take any parameter.
Return Value from capitalize()

The capitalize() function returns a string with the first letter capitalized and all other characters lowercased. It doesn't modify the original string.
Example 1: Capitalize a Sentence

string = "python is AWesome."

capitalized_string = string.capitalize()

print('Old String: ', string)
print('Capitalized String:', capitalized_string)

Output

Old String: python is AWesome
Capitalized String: Python is awesome

ii)

Python String center()
The center() method returns a string which is padded with the specified character.

The syntax of center() method is:

string.center(width[, fillchar])

center() Parameters

The center() method takes two arguments:

    width - length of the string with padded characters
    fillchar (optional) - padding character

The fillchar argument is optional. If it's not provided, space is taken as default argument.
Return Value from center()

The center() method returns a string padded with specified fillchar. It doesn't modify the original string.
Example 1: center() Method With Default fillchar

string = "Python is awesome"

new_string = string.center(24)

print("Centered String: ", new_string)

Output

Centered String:     Python is awesome


iii)

Python String encode()
The string encode() method returns encoded version of the given string.

Since Python 3.0, strings are stored as Unicode, i.e. each character in the string is represented by a code point. So, each string is just a sequence of Unicode code points.

For efficient storage of these strings, the sequence of code points is converted into a set of bytes. The process is known as encoding.

There are various encodings present which treats a string differently. The popular encodings being utf-8, ascii, etc.

Using string's encode() method, you can convert unicoded strings into any encodings supported by Python. By default, Python uses utf-8 encoding.

The syntax of encode() method is:

string.encode(encoding='UTF-8',errors='strict')

String encode() Parameters

By default, encode() method doesn't require any parameters.

It returns utf-8 encoded version of the string. In case of failure, it raises a UnicodeDecodeError exception.

However, it takes two parameters:

    encoding - the encoding type a string has to be encoded to
    errors - response when encoding fails. There are six types of error response
        strict - default response which raises a UnicodeDecodeError exception on failure
        ignore - ignores the unencodable unicode from the result
        replace - replaces the unencodable unicode to a question mark ?
        xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
        backslashreplace - inserts a \uNNNN escape sequence instead of unencodable unicode
        namereplace - inserts a \N{...} escape sequence instead of unencodable unicode

Example 1: Encode to Default Utf-8 Encoding

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)

Output

The string is: pythön!
The encoded version is: b'pyth\xc3\xb6n!'


iv)

Python String endswith()
The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.

The syntax of endswith() is:

str.endswith(suffix[, start[, end]])

endswith() Parameters

The endswith() takes three parameters:

    suffix - String or tuple of suffixes to be checked
    start (optional) - Beginning position where suffix is to be checked within the string.
    end (optional) - Ending position where suffix is to be checked within the string.

Return Value from endswith()

The endswith() method returns a boolean.

    It returns True if strings ends with the specified suffix.
    It returns False if string doesn't end with the specified suffix.

Example 1: endswith() Without start and end Parameters

text = "Python is easy to learn."

result = text.endswith('to learn')
# returns False
print(result)

result = text.endswith('to learn.')
# returns True
print(result)

result = text.endswith('Python is easy to learn.')
# returns True
print(result)

Output

False
True
True

v)

Python String index()
The index() method returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.

The syntax of the index() method for string is:

str.index(sub[, start[, end]] )

index() Parameters

The index() method takes three parameters:

    sub - substring to be searched in the string str.
    start and end(optional) - substring is searched within str[start:end]

Return Value from index()

    If substring exists inside the string, it returns the lowest index in the string where substring is found.
    If substring doesn't exist inside the string, it raises a ValueError exception.

The index() method is similar to find() method for strings.

The only difference is that find() method returns -1 if the substring is not found, whereas index() throws an exception.
Example 1: index() With Substring argument Only

sentence = 'Python programming is fun.'

result = sentence.index('is fun')
print("Substring 'is fun':", result)

result = sentence.index('Java')
print("Substring 'Java':", result)

Output

Substring 'is fun': 19

Traceback (most recent call last):
  File "<string>", line 6, in
    result = sentence.index('Java')
ValueError: substring not found

============================================================================================================================================


=======================================================END=================================================================================
