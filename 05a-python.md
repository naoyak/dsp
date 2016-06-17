# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples and lists are both ordered sequences of values, with the important difference that tuples are immutable - you can't modify individual elements. Only tuples will work as dictionary keys, since the lookup function would break if a mutable key's value was modified.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both collections of elements which can be of mixed type, but lists are ordered while sets are unordered and consist of unique elements.

```python
member_list = ['Amy', 'John', 'Ben', John']
>>> member_list
['Amy', 'John', 'Ben', 'John']
member_set = {'Amy', 'John', 'Ben', 'John'}
>>> member_set
{'Amy', 'John', 'Ben'} # duplicates removed
```

Finding an element is much faster in sets, since membership is checked with a hashtable.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are anonymous functions that can be created without a full named function declaration. This is often useful for passing to functions which expect a function object as an argument.

```python
In [1]: nums = [12, -33, 35, -2, 0]
In [2]: sorted(nums, key=lambda x: x^2-1)
Out[2]: [-33, -2, 0, 12, 35]
```


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is a syntactical construct in Python which creates a list where each element is a function of the individual elements returned by traversing an iterable. Map/filter is sometimes more concise if you already have an existing function to apply, but comprehensions are considered more readable and Pythonic.

```python
# Example 1
# Using map()
def add_one(x):
	return x+1

>> map(add_one, [0, 2, 5, 6, 7])
[1, 3, 6, 7, 8]

# Using a comprehension
>> lst = [0, 2, 5, 6, 7]
>> [x+1 for x in lst]
[1, 3, 6, 7, 8]

# Example 2
# Using filter()
def less_than_four(x):
	return x < 4

>> filter(less_than_five, [0, 1, 2, 3, 4, 5])
[0, 1, 2, 3]

# Using a comprehension
>> lst = [0, 1, 2, 3, 4, 5]
>> [x for x in lst if x < 4]
[0, 1, 2, 3]

# Example 3: set comprehension
>> {x for x in [0, 1, 1, 2, 2, 3, 4, 5, 5, 6] if x < 4}
{0, 1, 2, 3}

# Example 4: dictionary comprehension
>> fruit_counts =  {'apples': 4, 'bananas': 3, 'mangoes': 6, 'guavas': 8}
>> {k:v for k, v in fruit_counts if v > 5}
{'mangoes': 6, 'guavas': 8}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'

In [17]:  datetime.strptime(date_stop, '%m-%d-%Y') - datetime.strptime(date_sta
rt, '%m-%d-%Y')
Out[17]: datetime.timedelta(937)
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  

In [20]:  datetime.strptime(date_stop, '%m%d%Y') - datetime.strptime(date_start
, '%m%d%Y')
Out[20]: datetime.timedelta(513)
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015' 

In [24]:  datetime.strptime(date_stop, '%d-%b-%Y') - datetime.strptime(date_sta
rt, '%d-%b-%Y')
Out[24]: datetime.timedelta(7850) 
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





