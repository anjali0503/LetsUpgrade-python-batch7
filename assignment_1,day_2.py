# -*- coding: utf-8 -*-
"""assignment:1,Day:2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FN_oNimxUY-fHgc0XJ3lII1A_zZf-m7p

# 1.LIST AND IT'S DEFAULT FUNCTIONS
 1. List is an ordered collection of elemnts. 
 2.It is indicated by"[]".
 3.Its most commonly used data type in python and its very flexiable, all elements in list need not to be off same data type .
 4.Lists are mutable means values of list can be altered.
"""

#list of few elements.
lst=[5,15,22.44,"anjali",[2,1,3,4],"love python"]
lst

#default function APPEND
lst.append("pandey")

lst

#default function INDEX
lst.index(22.44)

# default function COUNT
lst.count("anjali")

#default function REVERSE
lst.reverse()
lst

#default function 
lst.remove(15)
lst

"""#2. DICTIONARY and its defaults functions

 #1.It is unorder collection key-value pairs.
 #2.Its denoted by {}
 #3.We must use keys to retrive the values
 #4.keys and values can of any type
 #5. syntax ={keys:values}
"""

#eg of dictionary with new elements
dit={"name":"anjali","age":20,"std":"TY","number":12345678}
dit

# default function : Keys
dit.keys()

#default fuction :VALUES
dit.values()

dit.pop("std")

dit

"""#3. SET and its default functions

 #1.Set is an  unordered collection of unique elements.
 #2.using set we can perform set operations like : UNION, CONJUSTION, INTERSECTION, etc .
 #3.since set have uniqe  values therefore they will eliminate duplicates
"""

set={23,34,555.54,23,6,7,6,6,}
set

#default function add
set.add(655)
set

"""#4. TUPLE and its default function

 #1.Tuple is an ordered sequence of item same as list the only difference is that  TUPLES ARE IMMUTABLE ,which means a tuple elements once created can't be modify.
 #2.It is indicated by "()".
"""

#elements in tuple
tpl=(5,15,22.44,"anjali",[2,1,3,4],"love python")
tpl

#default function count
tpl.count(15)

# default function index
tpl.index("love python")

"""#5. STRINGS and its default fuction

 #1.Strings are sequences of characters.
 #2.we can use single "'" or double '"' to reperesent strings.
 #3.strings are immutable
"""

str="anjali","love's python","anjali"
str

str.count("anjali")

str.index("love's python")