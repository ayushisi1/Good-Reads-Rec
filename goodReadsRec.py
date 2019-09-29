import requests
import urllib
import sys
from bs4 import BeautifulSoup

list_genres = ["art", "biography","business","classics",
"comics","ebooks","fantasy","fiction","graphic-novels","historical-fiction",
"horror","mystery","nonfiction","poetry","psychology",
"romance","science","science-fiction"]
string_menu = "Pick Genre: "
print(string_menu)
int_count = 1;
for i in list_genres:
    print(str(int_count) + ". " + i)
    int_count += 1
string_numInput = input("Enter a Number ")
if float(string_numInput) > 18 or float(string_numInput) < 1:
    print("Number is out of range")
else:
    string_Genre = list_genres[int(string_numInput)-1]
    mainUrl = "https://www.goodreads.com"
    basicUrl = "https://www.goodreads.com/genres/most_read/"
    url = basicUrl + string_Genre
    response = requests.get(url)
    soupMostRead = BeautifulSoup(response.text, 'html.parser')
    list_links = []
    for tags in soupMostRead.find_all('a'):
        string_link = tags.get('href')
        if string_link != None:
            if(string_link.find('/book/show') != -1):
                list_links.append(tags.get('href'))
    list_book = []
    for books in range(10):
        string_book = mainUrl + list_links[books]
        response1 = requests.get(string_book)
        soupBook = BeautifulSoup(response1.text, 'html.parser')
        ratingVal = soupBook.find('span', itemprop = "ratingValue")
        int_rating = float(ratingVal.text)
        if int_rating > 4.0:
            ratingCount = soupBook.find('meta', itemprop = 'ratingCount')
            string_text = ratingCount.text
            string_text = string_text.replace('ratings', '')
            string_text = string_text.replace(',', '')
            string_text = string_text[3:-4]
            int_count = float(string_text)
            if int_count < 25000:
                title = Book.find('h1', itemprop = "name")
                list_book.append(title.text)
    if len(list_book) == 0:
        print("There are no underrated books")
    else:
        for i in list_book:
        print(i)
