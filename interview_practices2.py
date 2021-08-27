
import re 

movies = ["The Godfather, 1972, Francis Ford Coppola", "Pather Panchali, 1975, Satyajit Ray"]
# Compile a regular expression to print only movie name and director name
pattern = re.compile(r', \d+, ')

movies_without_year = []
for movie in movies:
    # Retrieve a movie name and its director
    split_result = re.split(pattern, movie)
    # Create a new string with a movie name and its director
    movie_and_director = ', '.join(split_result)
    # Append the resulting string to movies_without_year
    movies_without_year.append(movie_and_director)
    
for movie in movies_without_year:
    print(movie)


college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
print(list(enumerate(college_years, 2019)))
# [(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]

fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]
#Desired output
# [('Apples', 5, 1.50), ('Oranges', 3, 2.25), ('Bananas', 4, 0.89)]
list(zip(fruits, quantities, prices))

# how to write the doc test
def sum(a, b):
    """
    >>> sum(4, 3)
    7

    >>> sum(-4, 5)
    1
    """
    return a + b
