# Practicing using Beautiful Soup!

import bs4 as bs
import urllib.request

specified_url = input("Enter a url to check for links: ")

sauce = urllib.request.urlopen(specified_url).read()
soup = bs.BeautifulSoup(sauce, "lxml")

count = 0
list_item = 1

for url in soup.find_all("a"):
    print(list_item, ": ", url.get("href"), sep="")
    count += 1
    list_item += 1


print("Total links: ", count, sep="")



