from datetime import datetime, date, timedelta
import os.path

class handle:

	#init important variables when class is called
	def __init__(self):
		save_directory = 'logs/'
		self.today = os.path.join(save_directory, (date.today().strftime("%m-%d-%y") + ".txt")) 
		self.yesterday = os.path.join(save_directory, ((date.today() - timedelta(1)).strftime("%m-%d-%y") + ".txt"))

	#read the previous days file and store each line into a list	
	def readPreviousFile(self):
		if self.checkExistance(self.yesterday):
			f = open(self.yesterday, 'r')
			self.data = f.readlines()

	#if the file isnt already in existance for that day then create the file		
	def writeFile(self, totalPeoplePurchased):	
		
		if self.checkExistance(self.today) is False:
			
			self.readPreviousFile()
			
			peoplePurchasedYesterday_int = int(self.data[1].translate(None, ",Total Purchases:  \n"))	
			totalPeoplePurchased_int = int(totalPeoplePurchased.translate(None, ","))
			peoplePurchasedinDay = totalPeoplePurchased_int - peoplePurchasedYesterday_int
			peoplePurchasedinDay_yes = float(self.data[3].translate(None, ",People purchased today: \n"))
			Growth_rate = abs(float(((peoplePurchasedinDay - peoplePurchasedinDay_yes) / peoplePurchasedinDay_yes) * 100.0))

			f = open(self.today, 'w+')
			f.write("Stats as of " + datetime.now().strftime("%m-%d-%y %H:%M") + "\n" )
			f.write("Total Purchases: " + totalPeoplePurchased + "\n")
			f.write("Purchased Yesterday: " + str(peoplePurchasedYesterday_int) + "\n")
			f.write("People purchased today: " + str(peoplePurchasedinDay) +"\n")
			f.write("Profit made: " + "$"+ str(peoplePurchasedinDay * 26.950) + "\n")
			
			if(peoplePurchasedinDay > peoplePurchasedinDay_yes):
				f.write("Change in growth Since Yesterday: " + ("{0:.2f}".format(Growth_rate)) + "% increase")
			else:
				f.write("Change in growth Since Yesterday: " + ("{0:.2f}".format(Growth_rate)) + "% decrease")	
		else:
			print "Statistics for the day already exist"

	#check to see if a file exists		
	def checkExistance(self, date):
		if(os.path.isfile(date)):
			return True
		else:
			return False 		