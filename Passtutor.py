#!/usr/bin/env python

import argparse, sys, time, os

global banner
global Des
banner = '''
 _____           _______    _             
|  __ \         |__   __|  | |            
| |__) |_ _ ___ ___| |_   _| |_ ___  _ __ 
|  ___/ _` / __/ __| | | | | __/ _ \| '__|
| |  | (_| \__ \__ \ | |_| | || (_) | |   
|_|   \__,_|___/___/_|\__,_|\__\___/|_|   
[+]Version 1.1                   @kor3n
'''
Des = '''
This is PassTutor! This tool will help you to remember passwords insted of
relying on password managers.
Author: Joshua Boat | www.ionsec.co.uk | jboat@ionsec.co.uk    
          
'''
print banner
print Des

#Program Arguments
parser = argparse.ArgumentParser(description='PassTutor is a tool will help you to remember passwords insted of relying on password managers.')
parser.add_argument('-p', '--password', help='Enter the password you wish to learn')
parser.add_argument('-lT', '--looktime', help='Time in seconds of how long you would like to look at the password. Default 5 Seconds')
parser.add_argument('-n', help='Do you want incorrect character Notification turned on. Default off.', action='store_true')
args = parser.parse_args()

#Set some global variables
global looktime
global incorrnotif
global passwd
global quit
global cor
global incor

#Setting the variables values
looktime = 5
incorrnotif = 'off'
passwd = ''
quit = 1
cor = 0
incor = 0

#Show help if no arguments were added
if args.password == None:
	parser.print_help()
	sys.exit()
elif args.password != None:
	passwd = args.password

if args.looktime:
	looktime = args.looktime

if args.n:
	incorrnotif = 'on'

def clear(b=0):
	os.system('clear')
	ft = 0
	if b == 1:
		print banner
		if ft == 0:
			print Des
			ft =+ 1

def passlook():
	clear(1)
	print '[+] You have', looktime, 'seconds to remember the password below.\n'
	print '[+]', passwd, '\n'
	time.sleep(float(looktime))
	clear()

passlook()

while quit !=0:
	clear(1)
	print '\n[+] Please guess your password: \n[+] Incorrect:', incor, '\n[+] Correct:' , cor, '\n'
	passtry = raw_input('[+] > ')
	
	if passtry == ':q':
		clear()
		quit = 0
	elif passtry == ':l':
		passlook()
	elif passtry == passwd:
		print '\n[+] You guess of the password was correct :)'
		cor += 1
		time.sleep(1)
	elif passtry != passwd:
		print '\n[+] You guess of the password was incorrect :('
		#time.sleep(1)
		if len(passtry) == len(passwd):
			ch = 0
			print '\n[+] -----------------------------------\n'
			while ch < len(passwd):
				if passtry[ch] == passwd[ch]:
					print '[+]', ch+1, '- Character correct.'
				if passtry[ch] != passwd[ch]:
					if incorrnotif == 'on':
						print '[+]', ch+1, '- Character incorrect(' + passtry[ch] + ').'
					elif incorrnotif == 'off':
						print '[+]', ch+1, '- Character incorrect.'
				ch += 1
				time.sleep(0.25)
			print '\n[+] -----------------------------------'
			raw_input('\n\n[+] Press Enter to Continue...')
		elif len(passtry) != len(passwd):
			print '[+] Password not same lenght!\n'
			time.sleep(2)
		incor += 1
