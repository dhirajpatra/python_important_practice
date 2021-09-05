
import time

l1 = []
l2 = []
l3 = []
s1 = []
s2 = []


def get_missing_number(lst):
    return set(range(lst[-1])[1:]) - set(lst)


l = list(range(1, 100))
l.remove(50)

print(set(range(l[-1])[1:]))
print('=' * 100)
print(set(l))
print(get_missing_number(l))


def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
#         print('seen: {}'.format(seen))
#         print('duplicates: {}'.format(duplicates))
#         print('-' * 50)
    return list(duplicates)


l = [20, 30, 40, 20, 50, 30]
print(find_duplicates(l))


def intersect(lst1, lst2):
    res, lst2_copy = [], lst2[:]
    for el in lst1:
        if el in lst2_copy:
            res.append(el)
            lst2_copy.remove(el)
    return res


l1 = [20, 30, 40, 20, 50, 30]
l2 = [70, 80, 40, 90, 50, 100]
print(intersect(l1, l2))


def is_anagram(s1, s2):
    return set(s1) == set(s2)


print(is_anagram("elvies", "lives"))


print(max(l1))
print(min(l1))


# remove all duplicates
lst = list(range(10)) + list(range(10))
print(lst)
lst = list(set(lst))
print(lst)


def reverse(str):
    if len(str) <= 1:
        return str
    return reverse(str[1:]) + str[0]


print(reverse("hello"))


houses = ["Eric's house", "Kenny's house",
          "Kyle's house", "Stan's house", "Dhiraj's house"]

# Each function call represents an elf doing his work


def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)


print(deliver_presents_recursively(houses))


# Find pairs of integers in list so that their sum is equal to integer x
def find_pairs(l, x):
    pairs = []
    for (i, el1) in enumerate(l):
        for (j, el2) in enumerate(l[(i+1):]):
            if el1 + el2 == x:
                pairs.append((el1, el2))
    return pairs


print(l1)
tic = time.perf_counter()
print(find_pairs(l1, 50))
toc = time.perf_counter()
print(toc - tic)


# Find pairs of integers in list so that their sum is equal to integer x
def find_pairs(l, x):
    pairs = []
    len_l = len(l)
    for i in range(0, len_l):
        for j in range((i+1), len_l):
            if l[i] + l[j] == x:
                pairs.append((l[i], l[j]))
    return pairs


print(l1)
tic = time.perf_counter()
print(find_pairs(l1, 50))
toc = time.perf_counter()
print(toc - tic)


# Compute the first n Fibonacci numbers
def cal_fibinacci(n):
    a, b = 0, 1
    fib = []
    for i in range(n):
        fib.append(b)
        a, b = b, (a + b)
    return fib


print(cal_fibinacci(10))

# one line fibonacci
lambda x:x if x <= 1 else fib(x-1) + fib(x+1)


def is_palindrome(phrase):
    return phrase == phrase[::-1]


print(is_palindrome("madam"))


def qsort(l):
    if l == []:
        return []
    return qsort([x for x in l[1:] if x < l[0]]) + l[0:1] + qsort([x for x in l[1:] if x >= l[0]])


print(l1)
print(qsort(l1))


# as a list ...
l = [3, 4]
l += [5, 6]
print(l)

# ... as a stack ...
l.append(10)
l.extend([9, 7])
l.pop()
print(l)

# ... and as a queue
l.insert(0, 5)
l.pop()
print(l)


def get_permutations(w):
    if len(w) <= 1:
        return set(w)
    smaller = get_permutations(w[1:])
    perms = set()
    for x in smaller:
        for pos in range(0, len(x) + 1):
            perm = x[:pos] + w[0] + x[pos:]
            perms.add(perm)
    return perms


print(get_permutations("nan"))


s1 = ['red', 'green', 'blue']
list(map(lambda x: x[0], s1))


list(map(lambda x, y: str(x) + y, [4, 1, 3], s1))


' is '.join(['this', 'good'])


list(filter(lambda x: True if x > 10 else False, [1, 15, 9, 20]))


print('   good '.strip())


sorted(l1)


sorted(l1, key=lambda x: 0 if x == 50 else x)


# zip or groups by one of each list
print(l1)
print(l2)
l3 = list(zip(l1, l2))
print(l3)


# ungrouping
list(zip(*l3))


list(enumerate(s1))


a, b = 'jane', 'alice'
print(a)
print(b)
a, b = b, a
print(a)
print(b)


def f(x, y, z):
    return x + y * z


print(f(*[1, 3, 4]))
f(**{'z': 4, 'x': 1, 'y': 3})


a, *b = l1
print(a)
print(b)


x = {'alice': 18}
y = {'bob': 27, 'ann': 22}
z = {**x, **y}
print(z)


l1 = [20, 40, 30]
l1.append(30)
print(l1)
l1.insert(2, 60)
print(l1)
l1 + [30]
print(l1)
l1.remove(60)
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1.index(30)
l1.index(30, 1)


stack = [3]
stack.append(5)
print(stack)
stack.pop()


basket = {'apple', 'banana', 'mango'}
print(basket)
same = set(['apple', 'banana', 'mango'])
print(same)
print('mashroom' in basket)
print('apple' in basket)


calories = {'apple': 50, 'banana': 80, 'chocolate': 540}
print(calories)
print(calories['apple'] < calories['banana'])
print('apple' in calories.keys())
print(50 in calories.values())
for k, v in calories.items():
    print(k) if v > 500 else None


# list comprehention
l = [('hi ' + x) for x in ['alice', 'bob', 'zen']]
print(l)
l = [x * y for x in range(3) for y in range(3) if x > y]
print(l)
squares = {x**2 for x in [0, 2, 4] if x < 4}
print(squares)


if None or 0 or 0.0 or '' or [] or {} or set():
    print('dead')
else:
    print('good')


s = "the quick brown fox jumps over the lazy dog"
print(s[1:])
print(s[:-1])
print(s[::-1])
print(s[-3:])
print(s.startswith('the'))
print(s.find('dog'))
print(s.replace('dog', 'wolf'))
print(len(s))
print('fox' in s)


[(lambda x: x * 2)(x) for x in l1]

[markdown]
# ## Iterators, Generators and Decorators


class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # return itself as as iterator object
    def __iter__(self):
        return self

    # return the next value still the value is less than high
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
        return self.current - 1

    # generator
    def generator(self):
        print("inside my generator")
        yield 'a'
        yield 'b'
        yield 'c'

    # yield
    def counter_generator(self):
        while self.current <= self.high:
            yield self.current
            self.current += 1


# calling
c = Counter(5, 10)
for i in c:
    print(i, end=' ')

c.generator()
for char in c.generator():
    print(char)

c = Counter(1, 5)
for i in c.counter_generator():
    print(i, end=' ')


# clouser adder is a clouser
def add_num(num):
    def adder(number):
        return num + number
    return adder


result = add_num(10)
result = result(20)
print(result)


# decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before call")
        print(args)
        print(kwargs)
        # changing args
        args = [5, 9]
        result = func(*args, **kwargs)
        print("after call")
        return result
    return wrapper


@my_decorator
def add(a, b):
    print("our add function")
    return a + b


add(1, 3)


# Find the first non-repeating integer in a list
def find_first_unique(lst):
    counts = {}  # Creating a dictionary
    # Initializing dictionary with pairs like (lst[i],(count,order))
    counts = counts.fromkeys(lst, (0, len(lst)))
    order = 0
    for ele in lst:
        # counts[ele][0] += 1  # Incrementing for every repitition
        # counts[ele][1] = order
        counts[ele] = (counts[ele][0]+1, order)
        # increment order
        order += 1
    answer = None
    answer_key = None
    # filter non-repeating with least order
    for ele in lst:
        if (counts[ele][0] is 1) and (answer is None):
            answer = counts[ele]
            answer_key = ele
        elif answer is None:
            continue
        elif (counts[ele][0] is 1) and (counts[ele][1] < answer[1]):
            answer = counts[ele]
            answer_key = ele
    return answer_key


print(find_first_unique([1, 1, 1, 2]))


def f(*args, **kwargs):
  print(args)
  print(kwargs)

f(1, 2, 3)
#(1, 2, 3)
#{}


# list 
doubles = [2 * n for n in range(50)]
# generator / iterator
doubles = (2 * n for n in range(50))


def print_name_with_prefix(prefix):
        print(f"Searching prefix:{prefix}")
        while True:
            name = (yield)
            if prefix in name:
                print(name)

# generator
x = print_name_with_prefix("hello")


# ciser encryption of a text and shift key
def encrypt(text, key):
  
    encrypted_text = ''

    # Fill in the blanks to create an encrypted text
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        encrypted_text = encrypted_text + alphabet[idx]

    return encrypted_text

# Check the encryption function with the shift equals to 10
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(encrypt("datacamp", 10))


# Create a word list from the string stored in text
text = 'StRing ObJeCts haVe mANy inTEResting pROPerTies'
text_split = text.split()
word_list = list()
for word in text_split:
    if text_split.index(word) % 2 != 0:
        word = word.upper()
    else:
        word = word.lower()
    word_list.append(word)

word_list = ' '.join(word_list)
