#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Logger.py
#  
#  Copyright 2014 user <user@user-HP-Compaq-nc6320-EN186UT-ABA>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 2 as 
#  published by the Free Software Foundation.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
from PyQt4 import QtGui

versionnumber = "0.0.1"


class mainWindow(QtGui.QMainWindow):
	
	
	def __init__(self):
		
		#This does some weird init stuff
		super(mainWindow, self).__init__()
		
		self.initUI()
		
	def initUI(self):
		
		### Menu and Button definition ###
		
		#Exit menu difinition
		
		exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit VE2HKW Logger')
		exitAction.triggered.connect(self.closeEvent)
		
		#New Menu option
		
		newAction = QtGui.QAction('&New', self)
		newAction.setShortcut('Ctrl+N')
		newAction.setStatusTip('Start a new contest!')
		newAction.triggered.connect(self.newEvent)
		
		#Open existing contest function
		
		openAction = QtGui.QAction('&Open', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open an existing contest')
		openAction.triggered.connect(self.openEvent)
		
		#Save current contest function
		
		saveAction = QtGui.QAction('&Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Saves current contest, use export if you want cabrillo or ADIF')
		saveAction.triggered.connect(self.saveEvent)
		
		#Export function for Cabrillo
		
		exportAction = QtGui.QAction('&Export Cabrillo', self)
		exportAction.setStatusTip('Exports a Cabrillo file of the current contest')
		exportAction.triggered.connect(self.exportEvent)
		
		#Setting the startup message in the Statusbar
		
		self.statusBar().showMessage('Welcome to VE2HKW Logger version ' + versionnumber)
		
		#Creation of the main menu bar
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(newAction)
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addSeparator()
		fileMenu.addAction(exportAction)
		fileMenu.addSeparator()
		fileMenu.addAction(exitAction)
		
		###  ###
		
		#General definition of the window geometry and placement
		
		self.resize(600, 400)
		self.center() 
		self.setWindowTitle('VE2HKW Logger')
		self.show()
		
	### Button functionallity is defined here ###
	
	def newEvent(self, event):
		raise NotImplementedError	
	
	def openEvent(self, event):
		raise NotImplementedError
		
	def saveEvent(self, event):
		raise NotImplementedError
		
	def exportEvent(self, event):
		raise NotImplementedError
		
		
	def center(self):
		
		#This is called by the initUI function to determin the center of the window
		
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center() #Determins the center of whatever screen the program is running on
		qr.moveCenter(cp)
		self.move(qr.topLeft()) #This doesn't move the window to the top left of the screen, but to the top left of the center of the screen
		
	def closeEvent(self, event):
		
		#makes a dialog box to confirm that you want to exit
		
		reply = QtGui.QMessageBox.question(self, 'Message',	"Are you sure you want to quit VE2HKW Logger?",	QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.Yes:
			print('It says segfault, but you can ignore it')
			self.destroy()
		else:
			pass



def main():
	
	app = QtGui.QApplication(sys.argv)
	MW = mainWindow()
	sys.exit(app.exec_())
		
#class scoreWindow(QtGui.QWidget):

if __name__ == '__main__':
	main()
