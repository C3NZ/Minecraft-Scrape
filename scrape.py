from lxml import html
from FileHandler import handle
import requests
import gc

programRunning = True

#gather the amount of people that have currently purchased minecraft
def peoplePurchased():
	
	page = requests.get('https://minecraft.net/')#grabs webpage
	tree = html.fromstring(page.text)#page.text contains the contents of the webpage as a string and then parses the page

	people = tree.xpath('//span[@class="paid_users"]/text()') #puts the value within the specific span element into a list
	return str(people[0])

while(programRunning is True):
	test = handle()
	test.writeFile(peoplePurchased())
	gc.collect()	
	print "Program ran Successfully!"
	programRunning = False



