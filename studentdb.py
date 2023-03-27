import tkinter as tk
#import mysql.connector (NEED UPDATE)
#cnx = mysql.connector.connect(user = 'localhost', ) (NEED UPDATE)
class Student:
	def __init__(self, name, id, age, gpa):
		self.name = name
		self.id = id
		self.age = age
		self.gpa = gpa
    
	def get_name():
		return self.name
	def get_id():
		return self.id
	def get_age():
		return self.age
	def get_gpa():
		return self.gpa
	
	def set_name(name):
		self.name = name
	def set_id(id):
		self.id = id
	def set_age(age):
		self.age = age
	def set_gpa(gpa):
		self.gpa = gpa
