#!/usr/bin/env python

import random
import config
import string



def HomeScreen():
	print "Welcome To InstaBot Tools - - -"
	print""
	print "< Devolved By Nicholas Impieri > V1.0 "
	print ""



	
	

def LoginOptions():
	

	print "Please Insert your Username and Password"
	
	username1 = raw_input("Username:  ")
	print
	password1 = raw_input("Password:  ")

	if ((username1 == config.logUser) and (password1 == config.logPsw)):
		print "Accesso Eseguito...."
		print""
		return True
	else:
		print "Credenziali non valide..."
		print""
		print "Inserire Nuovamente credenziali"
		print""
		LoginOptions()
		return False
		
	



def SelectionOptions():
	print"***************************************************"
	print "                                                 *"
	print "Premi [1] per Avviare InstaLikeBot               *"
	print"                                                  *"
	print "Premi [2] per Visuallizare i Credits             *"
	print "                                                 *"
	print "Premi [3] per Tornare alla schermata iniziale    *"
	print "                                                 *"
	print "**************************************************"
	print""	
	menu =raw_input("Digita un comando:  ")
	
	if menu == 1:
		import InstaLikeBot
		
	if menu == 2:
		print "<Devolved By Impieri Nicholas>"
		print""
		print "Libraries: Instapy for instagram Scripting base"
		print""
		print"------------Buil 1.0.0-------------------------"
		print""
		
		
	if menu == 3:
		HomeScreen()


	

			


HomeScreen()
LoginOptions()
SelectionOptions()







