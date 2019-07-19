import csv

file = open("Print Reports.txt", "r")

extractThisText = ["Total Pages printed in the last 24 hours: ","Total Pages printed since ","Total Users: ","Average pages printed per user: ","Total Pages Printed to Date: ","Daily Report For Collaborate PrintSpot for "]

class printLabStats:
	def __init__(self, requestDate, sinceDate, pagesIn24Hrs, totalPagesSinceDate, totalUsers, averagePagesPerUser, totalPagesPrintedToDate):
		self.requestDate = requestDate
		self.sinceDate = sinceDate
		self.requestDate = requestDate
		self.pagesIn24Hrs = pagesIn24Hrs
		self.totalPagesSinceDate = totalPagesSinceDate
		self.totalUsers = totalUsers
		self.averagePagesPerUser = averagePagesPerUser
		self.totalPagesPrintedToDate = totalPagesPrintedToDate
	def getData(self):
		return(self.requestDate + '!' + self.sinceDate + '!' + self.pagesIn24Hrs + '!' + self.totalPagesSinceDate + '!' + self.totalUsers + '!' + self.averagePagesPerUser + '!' + self.totalPagesPrintedToDate).split('!')

#Store all data grabbed into list
extractedData = []
for x in file:
	for y in extractThisText:
		if x.startswith(y):
			x = x.replace(y,'')
			x = x.replace('\n','')
			if(x.find('/') != -1):
				date = x[:10]
				x = x.strip(x[:12])
				extractedData.append(date)
				extractedData.append(x)
			else:
				extractedData.append(x)

#extractedData = [Request Date, Pages in last 24 hours, Date, Total pages printed since xx/xx/xxxx, Total users, Average pages printed per user, Total printed printed to date]
statObjects = []
for i in xrange(0,len(extractedData)-1,7):
	statObjects.append(printLabStats(extractedData[i],extractedData[i+2],extractedData[i+1],extractedData[i+3],extractedData[i+4],extractedData[i+5],extractedData[i+6]))

# Write list of printLabStats objects into a CSV file
with open('printLabData.csv','wb') as csv_file:
	writer = csv.writer(csv_file)
	delimiter = '!'
	writer.writerow(['Request Date','Cumulative Date Start','Pages Printed in Last 24 Hours','Total Pages Printed Since Cumulative Date','Total Users','Average Pages Printed Per User','Total Pages to Date'])
	for obj in range(len(statObjects)):
		stringList = (statObjects[obj].getData())
		writer.writerow(stringList)
