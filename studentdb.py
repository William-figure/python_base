#import tkinter as tk
#import mysql.connector (NEED UPDATE)
#cnx = mysql.connector.connect(user = 'localhost', ) (NEED UPDATE)
class Student:
	def __init__(self, name, id, age, gpa):
		self.name = name
		self.id = id
		self.age = age
		self.gpa = gpa
    
	def get_name(self):
		return self.name
	def get_id(self):
		return self.id
	def get_age(self):
		return self.age
	def get_gpa(self):
		return self.gpa
	
	def set_name(self, name):
		self.name = name
	def set_id(self, id):
		self.id = id
	def set_age(self, age):
		self.age = age
	def set_gpa(self, gpa):
		self.gpa = gpa
