from lxml import html
from FileHandler import handle
import requests

programRunning = True

#gather the amount of people that have currently purchased minecraft
def peoplePurchased():
	#grabs the webpage and turns it into a string that contains the contents of the webpage and then parses the page
	tree = html.fromstring(requests.get('https://minecraft.net/').text)
	#puts the value within the specific span element into a list
	people = tree.xpath('//span[@class="paid_users"]/text()') 
	return str(people[0])

while(programRunning):
	handler = handle()
	handler.writeFile(peoplePurchased())
	print "Program ran Successfully!"
	programRunning = False



