from typing import ClassVar
import requests
from mlist import Mlist
from lxml import html
import csv
url = "https://www.cars24.com/buy-used-cars-ludhiana/"
print("Started\n")
data = requests.get(url).text

# print(data)

tree = html.fromstring(data)
name = tree.xpath('//h2[@itemprop="name"]/text()')
# print(name,type(name[0]))

price = tree.xpath('//h3[@class="_6KkG6"]/text()')
# print("price",price,len(price))

km =tree.xpath('//p[1]/span[1]/text()')
# print("km",km,len(km))

petrol = tree.xpath('//span[@itemprop="name"]/text()')
# petrol = tree.xpath('//p[1]/span[2]/text()')
# print("petrol",petrol,len(petrol)) 

owner = tree.xpath('//p[1]/span[3]/text()')
# print("owner",owner, len(owner))

url =tree.xpath('//a[@title]/@href')

# print(".................................")
# owner = Mlist(owner)
# owner.removeall('Owner')
# print(owner)

# ...........
def removeall(list1,r):
    m = list1.count(r)
    for i in range(m):
        list1.remove(r)
    return list1

owner1 = removeall(owner,' Owner')
price1 = removeall(price,'₹ ')
dist=removeall(km,"km")
# print(owner1)
# print(price1)
# print(dist)
# print(url)
all_data = list(zip(name, price1, owner1, petrol , dist))
# for i in all_data:
# #     print(i)
new_file ="car.csv"
with open(new_file, 'w',newline='') as file:
	writer = csv.writer(file)
	writer.writerows(all_data)