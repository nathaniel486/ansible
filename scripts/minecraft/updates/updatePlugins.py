#Author Nathaniel Larrimore
#version 3.5.6


import urllib.request
import time
import os

global urlsToDownload #list of URLs to the files you want to download
global fileNamesToDownload#List of file names you want to download
global directory#the directory you want to download your files to
global numToUpdate#the number of files you are going to download
global numUpdated
global numDownloaded#incrimented number for the number of files successfully downloaded

urlsToDownload  = []
fileNamesToDownload = []
directory = ''
numToUpdate = 0
numUpdated = 0
numDownloaded = 0




#Create a backup of all the files you're downloading that already exist in a folder with today's date
def Backup(filename):
        try:
                
                today = time.strftime('%m-%d-%Y')
                if not os.path.exists(directory + '/' + today):
                        os.makedirs(directory + '/' + today)
                os.system('cp ' + filename + ' ' + directory + '/' + today)
        except Exception:
                print ('Count not backup ' + filename)




#Used to download the file
def downloadFiles():
        global numDownloaded
        global numToUpdate

        while(numDownloaded < numToUpdate):
                fileName = (directory + '/' + fileNamesToDownload[numDownloaded])

                print ('Backing up current plugins')
                Backup(fileName)

                try:
                        print ("Downloading " + fileName)
                        urllib.request.urlretrieve(urlsToDownload[numDownloaded],fileName)
                        print (fileName + " has been downloaded.")
                except Exception:
                        print ('Count not download ' + fileName + ' at ' + urlsToDownload[numDownloaded])

                numDownloaded = numDownloaded + 1



def askForDirectory():
	while(True):
		decision = ''

		global directory
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
                global numToUpdate
                numToUpdate = input('How many plugins do you wish to update?\t')

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

        global numUpdated
        global numToUpdate
        global fileNamesToDownload
        global urlsToDownload
        while(numUpdated < numToUpdate):
                while(True):

                        tempStr = input('Please enter the name of the plugin to update '\
                        '(include .zip)\t')
                        
                        if not tempStr:
                                print ('You can\'t leave this empty.')
                        else:
                                fileNamesToDownload.append(tempStr)
                                break

                while(True):

                        tempStr = input('Please enter the URL of the plugin you wish ' \
                        'to update:\t')
                        
                        if not tempStr:
                                print ('You can\'t leave this empty.')
                        else:
                                urlsToDownload.append(tempStr)
                                break


                numUpdated = numUpdated + 1
                        

#Start the prompt asking you to specify desired file names and where to download them

askForDirectory()

askForNumber()

askForNames()

downloadFiles()


print ('Finished.')
exit()
