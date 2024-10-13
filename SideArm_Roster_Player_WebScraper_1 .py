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

#this function removes the numbers in the string
def remove_numbers_from_string(input_string):
    return re.sub(r'\d+', '', input_string)

# adds spaces inbetween capital letters. 
def add_space_before_capital_letters(input_string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)

yearNumber = 2023
currentYear = 2011
layout_String = [
  "Player Name  ; Hometown  ;  School  ; Position  ;  Class  ; Height"
]
playerList = []
playerList.append(layout_String)

#this for loop goes through the html_string for every year. 
while (currentYear <= yearNumber):
  html_string = 'https://yalebulldogs.com/sports/field-hockey/roster/' + str(currentYear)

  html_text = requests.get(html_string).text
  ## can do print(html_text) without the .text
  #on the html_text to see the status on the website. 200 is the number
  #now with all the info in .text, do...
  soup = BeautifulSoup(html_text, 'lxml')

  #now we will get all the players using a for loop.
  #the players=soup.find_all() for every player.
  #this creates a list basically for a for loop
  players = soup.find_all(
    'div',
    class_=
    'sidearm-roster-player-details flex flex-align-center large-6 x-small-12 full columns'
  )

  #then make the forloop like this

  for player in players:
    playerElement = []  #made so that every player has there own element
    Name = str(player.find('div', class_='sidearm-roster-player-name').text)
    realName=remove_spaces(Name)
    
    try:
      Hometown = str(player.find('span', class_='sidearm-roster-player-hometown').text)
      realHometown=remove_spaces(Hometown)
      
    except AttributeError:
      Hometown = 'NA'

    try:
      HighSchool = str(player.find('span', class_='sidearm-roster-player-highschool').text)
      realHighSchool=remove_spaces(HighSchool)
    except AttributeError:
      HighSchool = 'NA'

    try:
      Year = str(
        player.find(
          'span',
          class_='sidearm-roster-player-academic-year hide-on-large').text)   
      realYear=remove_spaces(Year)
      
    except AttributeError:
      Year = 'NA'

    try:
      Height = str(
        player.find('span', class_='sidearm-roster-player-height').text)
      realHeight=remove_spaces(Height)
      
    except AttributeError:
      Height = 'NA'

    try:
      Position = str(player.find('span', class_='text-bold').text)
      realPosition=remove_spaces(Position)
    except AttributeError:
      Position = 'NA'

    playerInfo = str(currentYear) + " ;  " + realName + "  ; " + realHometown + '  ; ' + realHighSchool + '  ; ' + realPosition + '  ; ' + realYear + '   ; '

    playerElement.append(playerInfo)
    playerList.append(playerElement)

  currentYear = currentYear + 1  #updating the year for the html

#this writes the players list onto a txt that can be sent out to others.
  with open('FieldHockey.txt', 'w') as tfile:
    for i in range(len(playerList)):
      tfile.write('\n')
      tfile.write('\n'.join(playerList[i]))
