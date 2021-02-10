#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

repeat = "y"


try:
    while repeat == "y" or repeat == "yes":
        userSel = input("What machine would you like to connect to: ")
        userUser = input("Please enter the username of the machine you would like to connect to: ")
        userPass = input("Please enter the password of the machine you would like to connect to: ")
        userLoc = input("Where would you like to save the files: ")

        ## where to connect to
        t = paramiko.Transport(userSel, 22) ## IP and port

        ## how to connect (see other labs on using id_rsa private/public keypairs)
        t.connect(username=userUser, password=userPass)
    
        ## Make an sftp connection object
        sftp = paramiko.SFTPClient.from_transport(t)
    
        #movethemfiles(sftp, userLoc)
        ## iterate across the files within directory
        if os.path.isdir(userLoc):
            for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
                if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
                    sftp.put("/home/student/filestocopy/"+x, userLoc+x) # move file to target location
            print("Files copied successfully")
    
        else:
            print("That directory does not exist.")

        ## close the connection
        sftp.close() # close the connection
    
        repeat = input("Would you like to connect to another machine? (y/n): ").lower()
    
except:
    sftp.close()
    print("A connection error has occured. Please try again.")

def movethemfiles(sftp, userLoc):
    ## iterate across the files within directory
    if os.path.isdir(userLoc):
        for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
            if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
                sftp.put("/home/student/filestocopy/"+x, userLoc+x) # move file to target location
        print("Files copied successfully")

    else:
        print("That directory does not exist.")
