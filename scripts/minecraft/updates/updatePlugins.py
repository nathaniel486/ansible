#Author Nathaniel Larrimore
#version 3.5.6


import urllib.request
import time
import os

urlsToDownload = []#list of URLs to the files you want to download
fileNamesToDownload = []#List of file names you want to download
directory = ""#the directory you want to download your files to
numToUpdate = 0#the number of files you are going to download
numUpdated = 0 #incrimented number used for when you're specifying the files to download
numDownloaded = 0#incrimented number for the number of files successfully downloaded

#Used to download the file
def DownloadFile(Url ,fileName):
        print ("Downloading " + fileName)
        urllib.request.urlretrieve(Url,fileName)
        print (fileName + " has been downloaded.")


#Create a backup of all the files you're downloading that already exist in a folder with today's date
def Backup(filename):
	print ('Backing up current plugins')
	today = time.strftime('%m-%d-%Y')
	if not os.path.exists(directory + '/' + today):
    		os.makedirs(directory + '/' + today)
	os.system('cp ' + filename + ' ' + directory + '/' + today)



def askForDirectory():
	while(True):
		decision = ''

		directory = input('Please enter the full path of the '\
		'directory you wish to update:\t')

		if not directory:
			print ('You can\'t leave this empty.')
			continue

		while(True):
			decision = input('You are using ' + directory + ' as your '\
			'directory.  Is this correct? (y/n)').lower()


			if  decision == 'y' or decision == 'n':
				break
			else:
				print ('Please enter y or n.')
		
		if decision == 'y':
			break


def askForNumber():
        while(True):

                numToUpdate = input('How many plugins do you wish to update?\t')

  #              if not directory:
 #                       print ('You can\'t leave this empty.')
#                        continue


                try:
                        val = int(numToUpdate)
                        numToUpdate = val
                except ValueError:
                        print('This is not an int!')
                        continue

                if type(val) == int:
                        if val > 0 and val < 25:
                                
                                break
                        else:
                                print('Please enter a valid number')

                else:
                	print('Please enter a valid number')


def askForNames():
        numUpdated = 0
        print ('asking for names')
        while(numUpdated < numToUpdate):
                
                
                tempStr = input('Please enter the name of the plugin to update '\
'(include .zip)\t')
                
                fileNamesToDownload.append(tempStr)
                
                tempStr = input('Please enter the URL of the plugin you wish ' \
'to update:\t')

                urlsToDownload.append(tempStr)

                numUpdated = numUpdated + 1

#Start the prompt asking you to specify desired file names and where to download them

askForDirectory()

askForNumber()

askForNames()

#Actually backup and download the files.
while(numDownloaded < numToUpdate):
	
	filename = (directory + '/' + fileNamesToDownload[numDownloaded])
	Backup(filename)
	DownloadFile(urlsToDownload[numDownloaded],filename)
	numDownloaded = numDownloaded + 1


