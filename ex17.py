import sys
import random
import timeit
import requests
from bs4 import BeautifulSoup
##################################################
"""
http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
Exercise 17 (and Solution)
Use the BeautifulSoup and requests Python packages to print out a list 
of all the article titles on the New York Times homepage.
"""
##################################################
def getfiles():
    #set url to search
    url = 'https://github.com/demianvle/PythonExercises'
    r = requests.get(url)
    r_html = r.text
    #parse html and get only the links within the files table
    soup = BeautifulSoup(r_html, "html.parser")
    table= soup.find_all('table', 'files')
    links=soup.table.find_all('a')
    for link in links:
        print(link.get('href'))
#getfiles()

def web2text(url):
    r= requests.get(url)
    r_html=r.text
    soup= BeautifulSoup(r_html,'html.parser')
    print(soup.get_text())


def web2textcaller():
    url = '{}'.format(input("Enter a website:\n>>>"))

    web2text(url)

web2textcaller()

#############################################
print("\n The execution time was: {}".format(timeit.timeit(number = 10000)))
#############################################
sys.exit()

