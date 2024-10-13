#import the below things. Lxml will read the html file. 
#requests will grab the website information.
#don't use install for replit, use import. 
from bs4 import BeautifulSoup
import parser
import requests
import lxml
import xlsxwriter
import os
import re

#this function removes the spaces using the add_space function. 
def remove_spaces(input_string):
  Text_Without_Spaces = input_string.replace(' ', "")
  Text_Without_Spaces = "".join(input_string.split())
  input_string = Text_Without_Spaces
  realText=add_space_before_capital_letters(input_string)
  input_string=realText
  return input_string

#this function removes the words with height_units
def remove_height(input_string):
    height_units = ['ft', 'feet', 'foot', "'", "''"]
    for unit in height_units:
        input_string = input_string.replace(unit, '')

    return input_string.strip()

# adds spaces inbetween capital letters. 
def add_space_before_capital_letters(input_string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)

#this function removes numbers numbers in a string
def remove_numbers(input_string):
  pattern = r'\d+'  # This regular expression pattern matches one more digits
  result_string=re.sub(pattern, '', input_string)
  return result_string


yearNumber=2011
currentYear=2024
layout_String=["Player Name  ; Hometown  ;  School  ; Position  ;  Class  ; Height"]
playerList=[]
playerList.append(layout_String)


#this for loop goes through the html_string for every year. 
for i in range(yearNumber,currentYear):
  html_string='https://gocolumbialions.com/sports/field-hockey/roster/'+ str(yearNumber) 
  
  html_text = requests.get(html_string).text
## can do print(html_text) without the .text
#on the html_text to see the status on the website. 200 is the number
#now with all the info in .text, do...
  soup=BeautifulSoup(html_text, 'lxml')

#now we will get all the players using a for loop. 
#the players=soup.find_all() for every player.
#this creates a list basically for a for loop
  players=soup.find_all('li', class_='sidearm-roster-player')

#then make the forloop like this
  
  for player in players:
    playerElement=[]  #made so that every player has there own element
    # the following try and except are lookng 
    # strings for name, hometown, highschool, year, position, 
    #and height. the except AttributeError is shown when the 
    #find for a class is not shown. 
    try:
      Name=str(player.find('div', class_='sidearm-roster-player-name').text)
      Name=remove_spaces(Name)
      Name=remove_numbers(Name)
      
    except AttributeError:
      Name='NA'
    
    try:
      Hometown=str(player.find('span', class_ = 'sidearm-roster-player-hometown').text)
    except AttributeError:
      Hometown='NA'

    try:
      HighSchool=str(player.find('span', class_='sidearm-roster-player-highschool').text)
    except AttributeError:
      HighSchool='NA'
  

    try:
      Year=str(player.find('span', class_='sidearm-roster-player-academic-year hide-on-large').text)
    except AttributeError:
      Year='NA'
    
    try:
     Position=str(player.find('span', class_='sidearm-roster-player-academic-year hide-on-large').text)
     realPosition=remove_spaces(Position)
     realPosition=remove_height(realPosition)
    
    except AttributeError:
      Position='NA'

    try:
      Height=str(player.find('span', class_='sidearm-roster-player-height').text)
    except AttributeError:
      Height='NA'
   
    
    
  #ties all the player info into a string
    playerInfo = str(yearNumber)+ " ;  " +Name+ "  ; " + Hometown + '  ; ' + HighSchool + '  ; ' + Position + '  ; ' + Year+ '   ; ' + Height

    playerElement.append(playerInfo)
    playerList.append(playerElement)
    

  
  
  yearNumber=yearNumber+1 #updating the year for the html

  


#this writes the players list onto a txt that can be sent out to others. 
with open('FieldHockey.txt','w')as tfile:
  for i in range(len(playerList)):
    tfile.write('\n')
    tfile.write('\n'.join(playerList[i]))
