#First, type 'pip install xmltodict' in the command prompt to install the 
#required module
import xmltodict, csv

#Initial Lists:
doc_authors = []
doc_title = []
doc_periodical = []
doc_year = []

#Append author names, replace file location as necessary
with open("C:\Users\Ayanle\Desktop\Python Programs\Pubs_basedon_TCIA.xml") as fd:
    doc= xmltodict.parse(fd.read())
    
for i in range(0,8):
    doc_authors.append(doc["xml"]["records"]["record"][0]["contributors"]["authors"]["author"][i][u'style']["#text"])

#Append titles, periodicals and years
doc_title.append(doc["xml"]["records"]["record"][0]["titles"]["title"][u'style']["#text"])

#Append periodical name
doc_periodical.append(doc["xml"]["records"]["record"][0]["periodical"]["full-title"][u'style']["#text"])

#Append year number
doc_year.append(doc["xml"]["records"]["record"][0]["dates"]["year"][u'style']["#text"])

#Print out everything
def printText():
    print "Authors:\n--------"
    for i in doc_authors:
        print i
    print "\nTitle:\n------\n" + doc_title[0].strip("u")
    print "\nPeriodical:\n-----------\n" + doc_periodical[0].strip("u")
    print "\nYear:\n-----\n" + doc_year[0].strip("u")
printText()

#Write information to CSV file. If "output.csv" doesn't exist, it will be
#created in the same directory as this script
def writeCSV():
    outputFile = open('output.csv', 'w')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(['Authors:'])
    outputWriter.writerow(doc_authors)
    outputWriter.writerow(['Title:'])
    outputWriter.writerow(doc_title)
    outputWriter.writerow(['Periodical:'])
    outputWriter.writerow(doc_periodical)
    outputWriter.writerow(['Year:'])
    outputWriter.writerow(doc_year)
writeCSV()