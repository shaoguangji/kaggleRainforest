'''
CLASS: Web Scraping with Beautiful Soup

What is web scraping?
- Extracting information from websites (simulates a human copying and pasting)
- Based on finding patterns in website code (usually HTML)

What are best practices for web scraping?
- Scraping too many pages too fast can get your IP address blocked
- Pay attention to the robots exclusion standard (robots.txt)
- Let's look at http://www.imdb.com/robots.txt

What is HTML?
- Code interpreted by a web browser to produce ("render") a web page
- Let's look at example.html
- Tags are opened and closed
- Tags have optional attributes

How to view HTML code:
- To view the entire page: "View Source" or "View Page Source" or "Show Page Source"
- To view a specific part: "Inspect Element"
- Safari users: Safari menu, Preferences, Advanced, Show Develop menu in menu bar
- Let's inspect example.html
'''

# read the HTML code for a web page and save as a string
import requests
url = r'https://raw.githubusercontent.com/justmarkham/DAT7/master/data/example.html'
r = requests.get(url)
r.text

# convert HTML into a structured Soup object
from bs4 import BeautifulSoup
b = BeautifulSoup(r.text, "html")

# print out the object
print b

# 'find' method returns the first matching Tag (and everything inside of it)
b.find('title')
b.find('li')

# Tags allow you to access the 'inside text'
b.find('title').text

# Tags also allow you to access their attributes
b.find('h1')['id']

# 'find_all' method is useful for finding all matching Tags
b.find_all('p')[:3]

# ResultSets can be sliced like lists
b.find_all('p')[:3]
b.find_all('p')[2]

# iterate over a ResultSet
for element in b.find_all('p'):
    print element.text

# limit search by Tag attribute
b.find_all('p', attrs={'class':'topic'})    

# limit search to specific sections
b.find('body').find_all('p')

'''
EXERCISE ONE
'''

# find the 'h2' tag and then print its text
b.find('h2').text

# find the 'p' tag with an 'id' value of 'reproducibility' and then print its text
b.find('p',attrs={'id':'reproducibility'}).text

# find the first 'p' tag and then print the value of the 'id' attribute
print b.find('p')['id']

# print the text of all four li tags
for elem in b.find_all('li'):
    print elem.text

# print the text of only the API resources
for elem in b.find('ul', attrs={'id':'api'}).find_all('li'):
    print elem.text

'''
Scraping the IMDb website
'''

# get the HTML from the Shawshank Redemption page
r = requests.get('http://www.imdb.com/title/tt0111161/')

# convert HTML into Soup
b = BeautifulSoup(r.text)
print b

# run this code if you have encoding errors
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# get the title
b.find('h1', attrs={'itemprop':'name'}).text[:-8]

# get the star rating (as a float)
b.find('span',attrs={'itemprop':'ratingValue'}).text

'''
EXERCISE TWO
'''

# get the description
b.find('div',attrs={'itemprop':'description'}).text[21:-13]

# get the content rating
b.find('meta', attrs={'itemprop':'contentRating'})['content']

# get the duration in minutes (as an integer)
duration = b.find_all('time', attrs={'itemprop':'duration', 'datetime':'PT142M'})[1].text[:3]
runtime = int(duration)
runtime
'''
OPTIONAL WEB SCRAPING HOMEWORK

First, define a function that accepts an IMDb ID and returns a dictionary of
movie information: title, star_rating, description, content_rating, duration.
The function should gather this information by scraping the IMDb website, not
by calling the OMDb API. (This is really just a wrapper of the web scraping
code we wrote above.)

For example, get_movie_info('tt0111161') should return:

{'content_rating': 'R',
 'description': u'Two imprisoned men bond over a number of years...',
 'duration': 142,
 'star_rating': 9.3,
 'title': u'The Shawshank Redemption'}

Then, open the file imdb_ids.txt using Python, and write a for loop that builds
a list in which each element is a dictionary of movie information.

Finally, convert that list into a DataFrame.
'''

# define a function that accepts an IMDb ID and returns a dictionary of movie information
def get_movie_info(IMDBId):
    return

# test the function


# open the file of IDs (one ID per row), and store the IDs in a list


# get the information for each movie, and store the results in a list


# check that the list of IDs and list of movies are the same length


# convert the list of movies into a DataFrame


'''
Another IMDb example: Getting the genres
'''

# read the Shawshank Redemption page again

# only gets the first genre

# gets all of the genres

# stores the genres in a list

'''
Another IMDb example: Getting the writers
'''

# attempt to get the list of writers (too many results)

# limit search to a smaller section to only get the writers

'''
Another IMDb example: Getting the URLs of cast images
'''

# find the images by size

# check that the number of results matches the number of cast images on the page

# iterate over the results to get all URLs

'''
Useful to know: Alternative Beautiful Soup syntax
'''

# read the example web page again
url = r'https://raw.githubusercontent.com/ga-students/DAT-DC-9/master/data/example.html?token=AG8aPhA-GT-gTGX3iXysiHnk2BLKJmttks5WLS2rwA%3D%3D'
r = requests.get(url)

# convert to Soup
b = BeautifulSoup(r.text)

# these are equivalent
b.find(name='p')    # normal way
b.find('p')         # 'name' is the first argument
b.p                 # can also be accessed as an attribute of the object

# these are equivalent
b.find(name='p', attrs={'id':'scraping'})   # normal way
b.find('p', {'id':'scraping'})              # 'name' and 'attrs' are the first two arguments
b.find('p', id='scraping')                  # can write the attributes as arguments

# these are equivalent
b.find(name='p', attrs={'class':'topic'})   # normal way
b.find('p', class_='topic')                 # 'class' is special, so it needs a trailing underscore
b.find('p', 'topic')                        # if you don't name it, it's assumed to be the class

# these are equivalent
b.find_all(name='p')    # normal way
b.findAll(name='p')     # old function name from Beautiful Soup 3
b('p')                  # if you don't name the method, it's assumed to be find_all