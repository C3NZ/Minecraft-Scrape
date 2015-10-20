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
			f.close()

	#if the file isnt already in existance for that day then create the file		
	def writeFile(self, totalPeoplePurchased):	
		
		if self.checkExistance(self.today) is False:
			
			#load the previous days data into a list
			self.readPreviousFile()
			
			#set up all the appropriate variables that are going to be written to the file.
			#translate(arg1, arg2) arg1 is whats going to replace any char in arg2 of the string you give it
			peoplePurchasedYesterday_int = int(self.data[1].translate(None, ",Total Purchases:  \n"))	
			
			totalPeoplePurchased_int = int(totalPeoplePurchased.translate(None, ","))
			#total amount of people that have purchased minecraft today.
			peoplePurchasedinDay = totalPeoplePurchased_int - peoplePurchasedYesterday_int
			#total amount of people that have purchased minecraft yesterday.
			peoplePurchasedinDay_yes = float(self.data[3].translate(None, ",People purchased today: \n"))
			#take the absolute value because we define whether the growth rate is an increase or decrease later on.
			Growth_rate = abs(float(((peoplePurchasedinDay - peoplePurchasedinDay_yes) / peoplePurchasedinDay_yes) * 100.0))

			f = open(self.today, 'w+')#returns a file object with the privilege to write
			
			#write all the data gathered to the file and do any necessary foormatting to variables
			f.write("Stats as of " + datetime.now().strftime("%m-%d-%y %H:%M") + "\n" )
			f.write("Total Purchases: " + totalPeoplePurchased + "\n")
			f.write("Purchased Yesterday: " + str(peoplePurchasedYesterday_int) + "\n")
			f.write("People purchased today: " + str(peoplePurchasedinDay) +"\n")
			f.write("Profit made: " + "$"+ str(peoplePurchasedinDay * 26.950) + "\n")
			
			#determines whether the growth rate is decreasing or increasing
			#Formats the code to 2 decimal places
			if(peoplePurchasedinDay > peoplePurchasedinDay_yes):
				f.write("Change in growth Since Yesterday: " + ("{0:.2f}".format(Growth_rate)) + "% increase")
			else:
				f.write("Change in growth Since Yesterday: " + ("{0:.2f}".format(Growth_rate)) + "% decrease")	
			#close the file out of memory	
			f.close()	
		else:
			print "Statistics for the day already exist"

	#check to see if a file exists
	#The date is the filename for all cases		
	def checkExistance(self, date):
		if(os.path.isfile(date)):
			return True
		else:
			return False 		