### This program operates under the assumption that someone born in, for example 1903, wiil register as alive in 1903. If they died in 1980, they will register as dead in 1980.

import random

class person():
	def __init__(self, birthYear, deathYear):
		self.birthYear = birthYear
		self.deathYear = deathYear
	def getBirthYear(self):
		return self.birthYear
	def getDeathYear(self):
		return self.deathYear		

class Year():
	def __init__(self, intYear): 
		self.stillAlive = 0 #PortalThings
		self.intYear = intYear
	def getYear(self):
		return self.intYear
	def getStillAlive(self):
		return self.stillAlive
	def checkPerson(self, human):
		if self.intYear >= human.getBirthYear() and self.intYear < human.getDeathYear():
			self.stillAlive += 1
		return

def main():
	yearList = []
	for yearCount in range (1900,2001):
		yearList.append(Year(yearCount))
	#generate a random list of people for testing purposes
	people = []
	for count in range (0, 500):
		birth = random.randint(1900,2001)
		death = random.randint(birth,2001) #possibility for people to have the same birth and death year, they won't count as alive in any year
		people.append(person(birth,death))
		
	greatestAlive = [Year(0)] #list of years with the greatest amount of living people, in case of ties
	for item in yearList:
		for human in people:
			item.checkPerson(human) #see if this human was alive that year
		if item.getStillAlive() == greatestAlive[0].getStillAlive(): #if this year is tied for the most alive people, add it to the list
			greatestAlive.append(item)
		if item.getStillAlive() > greatestAlive[0].getStillAlive():
			greatestAlive = [item] #if this year has the most alive people so far, create a new list consisting of just this year
	if len(greatestAlive) == 1: 			#Only one winning year
		print "The year with the most living number of people was "+str(greatestAlive[0].getYear())+"."
	else: 									#if more than one year, make a string out of all the years to display
		YearString = ""
		for count in range(0, len(greatestAlive)):
			YearString+=(str(greatestAlive[count].getYear()))
			if count < (len(greatestAlive)-1): # only add commas if we're not done yet
				YearString+=(", ")
		YearString += "."
		print "The years with the most living number of people were " + YearString

		
	
if __name__ == "__main__":
	main()