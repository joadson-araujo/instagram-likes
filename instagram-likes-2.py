#Script adaptado por github.com/joadson-araujo
#Colocar o geckodriver na pasta informada no def __init__

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagramBot:

  def __init__(self, username, password): #necessário baixar o geckodriver.exe para Mozilla Firefox
    self.username = username
    self.password = password
    self.bot = webdriver.Firefox(executable_path = '<dir>') #exemplo: 'C:/Joad-Notebook/Downloads/geckodriver.exe'
  
  def login(self):
    bot = self.bot
    bot.get('https://www.instagram.com/accounts/login')
    time.sleep(5)
    bot.find_element_by_name('username').send_keys(self.username)
    bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
    time.sleep(5)
    
  def procurar(self):
    bot = self.bot
    bot.get('<url ig profile>') #exemplo: https://instagram.com/__joadson
    time.sleep(3)
    
  def like(self,amount):
    bot = self.bot
    time.sleep(3)
    bot.find_element_by_class_name('_aagw').click()
        
    #Devido às atualizações no front-end, os IDs das TAGs podem sofrer alterações. Favor informar caso positivo.
    i=1
    while i <= amount:
        time.sleep(2)

        element = bot.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
        bot.execute_script("arguments[0].click()", element)
        bot.find_element_by_css_selector('._aaqg > button:nth-child(1)').click()
        time.sleep(1)	

        i+=1

insta = instagramBot('<user>', '<password>') #inserir o usuario e senha
insta.login()
insta.procurar()
insta.like(10) #inserir a quatidade de fotos para like