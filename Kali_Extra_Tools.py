#!/usr/bin/python
#-------------------------------#
import os, sys, subprocess
import argparse

#-------------------------------#
# Info
#-------------------------------#
__purpose__ = "Simple Script to install additional tools in Kali"
__author__ = "Eric Walker"
__license__ = "GPL"
__version__ = "0.1"
__date__ = "21 Nov 2014"
__credits__ " "
__maintainer__ = "Eric Walker"
__email__ = "eric@ericwalker.org"
__status__ = "Testing"

#-------------------------------#
# Updates:
#
#
#
#-------------------------------#
# Colors:
#-------------------------------#
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
#-------------------------------#

#-------------------------------#
# Main Menu section:
#-------------------------------#
def main_menu():
    """Display the main menu"""

    i = None
    valid_options = {1: google_chrome,
                     2: smbexec,
                     3: phantomjs,
                     4: responder ,
                     5: eyewitness,
                     99: quit
    }
    os.system('clear')
    banner()
    while i is None:
        print OKGREEN + " [1]" + ENDC + " Install Google Chrome"
        print OKGREEN + " [2]" + ENDC + " Install SMBEXEC 2 "
        print OKGREEN + " [3]" + ENDC + " Install PhantomJS "
        print OKGREEN + " [4]" + ENDC + " Install Responder"
        print OKGREEN + " [5]" + ENDC + " Install EyeWitness"
        #print OKGREEN + " [6]" + ENDC + " Install "
        #print OKGREEN + " [7]" + ENDC + " Install "
        print FAIL + "[99]" + ENDC + " Quit "
        ##Check for valid Inputs##
        try:
            i = raw_input("\nWhat would you like to do: ")
            i == int(i) in valid_options
        except ValueError:
            i = None 
            os.system('clear')
            banner()
            print FAIL + "[!] Not a valid option, please try again: " + ENDC
            i = None
        except KeyError:
            os.system('clear')
            banner()
            print FAIL + "[!] Not a valid option, please try again: " + ENDC
            i = None
        except TypeError:
            os.system('clear')
            banner()
            print FAIL + "[!] Not a valid option, please try again: " + ENDC
            i = None
        except KeyboardInterrupt:
            print FAIL + "\n[!] CTRL C entered - Quitting " + ENDC
            exit(1)
        else:
            if int(i) in valid_options:
                valid_options[int(i)]()
            else:
                os.system('clear')
                banner()
                print FAIL + "[!] Not a valid option, please try again: " + ENDC
                i = None

#-------------------------------#
#1 Google Chrome Install
#-------------------------------#
def google_chrome():
    """Install Google Chrome Repo Keys and Application """
    os.system('clear')
    print OKGREEN + "[*] Checking for Google Chrome"
    INSTALL1 =  subprocess.call(['dpkg-query', '-W', 'google-chrome-stable'])
    if INSTALL1 == 0:
         print WARNING + "[*] Google Chrome is already installed " + ENDC
         INPUT1 = raw_input("Press any key to continue")
         main_menu()
    else:    
        print OKGREEN + "[*] Installing Google APT Repo Keys"
        os.system('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -')
        os.system('echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list')
        print OKGREEN + "[*] Checking for system updates" + ENDC
        os.system('apt-get update')
        os.system('apt-get install google-chrome-stable')
        print OKBLUE + "[-] Run using gksu google-chrome" + ENDC
        print OKBLUE + "[-] Or modify /opt/google/chrome/google-chrome" + ENDC
        print OKBLUE + "[-] " + ENDC
        print OKBLUE + "[-] add: --user-data-dir to the end of the last line" + ENDC
        print OKBLUE + "[-] " + ENDC
        print OKBLUE + "[-] Just know this will get removed on updates" + ENDC
    main_menu()


#-------------------------------#
#2 SMBEXEC 2 Install
#-------------------------------#
def smbexec():
    """Install SMBEXEC 2"""
    os.system('clear')
    print OKGREEN + "[*] Installing SMBEXEC 2"
    RESP1 = os.path.isdir('/opt/smbexec/')
    if RESP1 == True:
        print WARNING + "[*] SMBEXEC is already installed " + ENDC
        INPUT1 = raw_input("Press any key to continue")
    else:
        print OKGREEN + "[*] Pulling SMBEXEC from Github" + ENDC
        os.system("cd /opt/; git clone https://github.com/pentestgeek/smbexec.git ")
        print OKGREEN + "[*] SMBEXEC has been downloaded " + ENDC
        INPUT1 = raw_input("Press any key to continue")
        print OKGREEN + "[*] Finishing the Installation: " + ENDC
        os.system("cd /opt/smbexec/; ./install.sh")
    main_menu()

#-------------------------------#
#3 PhantomJS Install
#-------------------------------#
def phantomjs():
    """"Install PhantomJS"""
    os.system('clear')
    print OKGREEN + "[*] Installing PhantomJS " + ENDC
    RESP1 = os.path.isdir('/opt/phantomjs/')
    if RESP1 == True:
        print WARNING + "[*] PhantomJS is already installed " + ENDC
        INPUT1 = raw_input("Press any key to continue")
    else:
        print OKGREEN + "[*] Pulling PhantomJS from Github" + ENDC
        os.system("cd /opt/; git clone git://github.com/ariya/phantomjs.git ")
        print OKGREEN + "[*] PhantomJS has been downloaded " + ENDC
        INPUT1 = raw_input("Press any key to continue")
        print OKGREEN + "[*] Finishing the Installation: " + ENDC
        print WARNING + "[*] This will take a long time so be patient " + ENDC
        INPUT2 = raw_input("Press any key to continue")
        os.system("cd /opt/phantomjs/; git checkout 1.9")
        os.system("cd /opt/phantomjs/; ./build.sh")
    main_menu()

#-------------------------------#
#4 Responder Install
#-------------------------------#
def responder():
    os.system('clear')
    print OKGREEN + "[*] Installing Responder; Please Wait:" + ENDC
    RESP1 = os.path.isdir('/opt/Responder/')
    if RESP1 == True:
        print WARNING + "[*] Responder is already installed " + ENDC
        INPUT1 = raw_input("Press any key to continue")
    else:
        print OKGREEN + "[*] Pulling Responder from Github" + ENDC
        os.system('cd /opt; git clone https://github.com/SpiderLabs/Responder.git ')
        print OKGREEN + "[*] Responder has been downloaded " + ENDC
        INPUT1 = raw_input("Press any key to continue")
    main_menu()

#-------------------------------#
#5 Eyewitness Install
#-------------------------------#
def eyewitness():
    os.system('clear')
    print "Eyewitness"
    print OKGREEN + "[*] Installing EyeWitness; Please Wait:" + ENDC
    RESP1 = os.path.isdir('/opt/EyeWitness/')
    if RESP1 == True:
        print WARNING + "[*] EyeWitness is already installed " + ENDC
        INPUT1 = raw_input("Press any key to continue")
    else:
        print OKGREEN + "[*] Pulling EyeWitness from Github" + ENDC
        os.system('cd /opt; git clone https://github.com/ChrisTruncer/EyeWitness.git ')
        print OKGREEN + "[*] EyeWitness has been downloaded " + ENDC
        INPUT1 = raw_input("Press any key to continue")
    main_menu()


#-------------------------------#
#6
#-------------------------------#
#def  ():
#    os.system('clear')



#-------------------------------#
#99 Quit
#-------------------------------#
def quit():
    print ""
    print FAIL + "Enjoy the new tools!!" + ENDC
    print ""
    exit(0)

#-------------------------------#
# Banner
#-------------------------------#
def banner():
    """Just a simple Banner """
    print  FAIL + "" 
    print " ____________________________________________ "
    print "|  ___  ____        _       _____     _____  |"
    print "| |_  ||_  _|      / \     |_   _|   |_   _| |"
    print "|   | |_/ /       / _ \      | |       | |   |"
    print "|   |  __'.      / ___ \     | |   _   | |   |"
    print "|  _| |  \ \_  _/ /   \ \_  _| |__/ | _| |_  |"
    print "| |____||____||____| |____||________||_____| |"
    print "|                                            |"   
    print "|   ADDITIONAL SOFTWARE INSTALL MAIN MENU    |"
    print "|     http://www.ericjonwalker.com           |"
    print "|     Twitter: @ericjonwalker.com            |"
    print "|____________________________________________|\n" + ENDC
#-------------------------------#
# Main Section
#-------------------------------#
if __name__ == "__main__":

#-------------------------------#
#  allow for passing variables 
#-------------------------------#
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--google", action='store_true', default=False, help="Install Google Chrome")
    parser.add_argument("-s", "--smbexec", action='store_true', default=False, help="Install SMBEXEC 2")
    parser.add_argument("-p", "--phantomjs", action='store_true', default=False, help="Install phantomjs")
    parser.add_argument("-r", "--responder", action='store_true', default=False, help="Install Responder")
    parser.add_argument("-e", "--eyewitness", action='store_true', default=False, help="Install EyeWitness")
    args = parser.parse_args()

    if args.google:
       print "Installing Google:"
       google_chrome()
    elif args.smbexec:
       print "Installing SMBEXEC 2:"
       smbexec()
    elif args.phantomjs:
       print "Installing PhantomJS:"
       phantomjs()
    elif args.responder:
       print "Installing Responder:"
       responder()
    elif args.eyewitness:
       print "Installing EyeWitness:"
       eyewitness()
    else: 
       main_menu() 
