#OLD VERSION. DO NOT USE THIS SCRIPT.
#VERSION 2 IS NOW AVALIABLE.

#Script adaptado por github.com/joadson-araujo

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagramBot:

  def __init__(self, username, password): #necessário baixar o geckodriver.exe para Mozilla Firefox
    self.username = username
    self.password = password
    self.bot = webdriver.Firefox(executable_path = '<pasta do geckodriver>') #exemplo: 'C:/Joad-Notebook/Downloads/geckodriver.exe'
  
  def login(self):
    bot = self.bot
    bot.get('https://www.instagram.com/accounts/login')
    time.sleep(5)
    bot.find_element_by_name('username').send_keys(self.username)
    bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
    time.sleep(3)
    
  def procurar(self):
    bot = self.bot
    bot.get('<inserir o endereço do instagram a ser curtido>') #exemplo: https://instagram.com/__joadson

  def like(self,amount):
    bot = self.bot
    bot.find_element_by_class_name('v1Nh3').click()
    
    #devido às atualizações no front-end, os IDs das TAGs podem sofrer alterações. Favor informar caso positivo.
    i=1
    while i <= amount:
        time.sleep(2)
        bot.find_element_by_class_name('fr66n').click()
        bot.find_element_by_css_selector('div.l8mY4').click()
        i+=1

insta = instagramBot('<seu_login>', '<sua_senha>')
insta.login()
insta.procurar()
insta.like(100) #inserir a quatidade de fotos para like
