from urllib.request import FancyURLopener
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import csv

class myOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)Gecko/20071127 Firefox/2.0.0.11'


opener = myOpener()

itemName = input("Enter the name of the item you would like to search for the amazon store: ")
itemName = itemName.replace(" ", "+")

url = "https://www.amazon.com/s?k="+itemName+"&ref=nb_sb_noss_1"
print(url)

client = opener.open(url)
htmlCont = client.read()
client.close()

pageSoup = soup(htmlCont, features="html.parser")
localSoup = open('html_download.html', 'w', encoding='UTF-8')
for line in pageSoup.prettify(formatter = 'minimal'):
    localSoup.write(str(line))
localSoup.close()

containers = pageSoup.findAll('div',{'class':'sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32'})


with open('output-data.csv', 'w', newline="", encoding='UTF-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'rating', 'price'])
    for container in containers:
        if container != None:
            container_name = None
            container_rating = None
            container_price = None
            price = None
            if container.find('h2') != None:
                container_name = container.find('span', {'class':'a-size-base-plus a-color-base a-text-normal'})
                name = container_name.text
                print(name)
            if container.i != None:
                container_rating = container.i
                rating = container_rating.text
                print(rating)
            if container.find('span',{'class':'a-offscreen'}) != None:
                container_price = container.find('span',{'class':'a-offscreen'})
                price = container_price.text
                print(price+'\n')
            writer.writerow([str(name), str(rating), str(price)])


# print(len(containers))

# print(containers[0].find('span',{'class':'a-offscreen'}))

