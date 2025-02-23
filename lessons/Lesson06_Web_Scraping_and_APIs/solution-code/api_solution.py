'''
CLASS: Getting Data from APIs

What is an API?
- Application Programming Interface
- Structured way to expose specific functionality and data access to users
- Web APIs usually follow the "REST" standard

How to interact with a REST API:
- Make a "request" to a specific URL (an "endpoint"), and get the data back in a "response"
- Most relevant request method for us is GET (other methods: POST, PUT, DELETE)
- Response is often JSON format
- Web console is sometimes available (allows you to explore an API)
'''

# read IMDb data into a DataFrame: we want a year column!
from bs4 import BeautifulSoup
import pandas as pd
url = r'https://raw.githubusercontent.com/justmarkham/DAT5/master/data/imdb_movie_ratings_top_1000.csv'
movies = pd.read_csv(url)
movies.head()

# use requests library to interact with a URL
import requests
r = requests.get('http://www.omdbapi.com/?t=the shawshank redemption&r=json&type=movie')

# check the status: 2xx Success, 3xx Redirection, 4xx Client Error, 5xx Server Error
r.status_code

# view the raw response text
type(r.text)

# decode the JSON response body into a dictionary
r.json()

# extracting the year from the dictionary
r.json()['Year']

# what happens if the movie name is not recognized?
r = requests.get('http://www.omdbapi.com/?t=blahblahblah&r=json&type=movie')
r.status_code
r.json()

# define a function to return the year
def get_movie_year(title):
    r = requests.get('http://www.omdbapi.com/?t={}&r=json&type=movie'.format(title))
    
    if r.json()['Response'] == 'False':
        return None

    return r.json()['Year']
    

# test the function
get_movie_year('The Shawshank Redemption')
get_movie_year('blahblahblah')

# create a smaller DataFrame for testing
top_movies = movies.head().copy()

# write a for loop to build a list of years
from time import sleep

years = []
for title in top_movies.title:
    years.append(get_movie_year(title))
    sleep(1)

# check that the DataFrame and the list of years are the same length
assert(len(top_movies) == len(years))

# save that list as a new column
top_movies['year'] = years

# collect data from google maps api
# documentation: https://developers.google.com/maps/documentation/geocoding/start
address = 'General Assembly DC'
api_url = r'https://maps.googleapis.com/maps/api/geocode/xml?address={}'.format(address)
r = requests.get(api_url)
b = BeautifulSoup(r.text, 'xml')


'''
Bonus content: Updating the DataFrame as part of a loop
'''

# enumerate allows you to access the item location while iterating
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print index, letter

# iterrows method for DataFrames is similar
for index, row in top_movies.iterrows():
    print index, row.title

# create a new column and set a default value
movies['year'] = -1

# loc method allows you to access a DataFrame element by 'label'
movies.loc[0, 'year'] = 1994

# write a for loop to update the year for the first three movies
for index, row in movies.iterrows():
    if index < 3:
        movies.loc[index, 'year'] = get_movie_year(row.title)
        sleep(1)
    else:
        break

'''
Other considerations when accessing APIs:
- Most APIs require you to have an access key (which you should store outside your code)
- Most APIs limit the number of API calls you can make (per day, hour, minute, etc.)
- Not all APIs are free
- Not all APIs are well-documented
- Pay attention to the API version

Python wrapper is another option for accessing an API:
- Set of functions that "wrap" the API code for ease of use
- Potentially simplifies your code
- But, wrapper could have bugs or be out-of-date or poorly documented
'''
