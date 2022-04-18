import datetime
import json
from tkinter import Variable
from bs4 import BeautifulSoup
from numpy import append
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
class Holiday:
      
    def __init__(self,name, date):
        #Your Code Here        
        self.name = name
        self.date = date

    def __str__ (self):
        # String output
        # Holiday output when printed.
        return f"{self.name} ({self.date})"   
   
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------


class HolidayList:
    def __init__(self):
       self.innerHolidays = []
    
    def addHoliday(self, holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
        Object = Holiday(Object.name, Object.date)
        self.innerHolidays.append(Object)

    def findHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays
        # Return Holiday
        for i in self.innerHolidays:
            if i.name==HolidayName and i.date ==Date:
                return i

    def removeHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
        delete = self.findHoliday(HolidayName, Date)
        if delete != None:
            self.innerHolidays.remove(delete)
            print("you have removed a holiday")

    def read_json(self, filelocation):
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.
        f = open ('holidays.json', "r")
        data = json.loads(f.read())
        for holidayObj in data['holidays']:
            self.innerHolidays.append(holidayObj)
        print('You have added a holiday')
        print(self.innerHolidays)



    def save_to_json(self, filelocation):
        # Write out json file to selected file.
        file = open(filelocation, 'w')
        
    def scrapeHolidays(self):
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.
        def getHTML(url):
                response = requests.get(url)
                return response.text

        year_list = ['2020', '2021', '2022', '2023', '2024']
        for year in year_list:
            url = 'https://www.timeanddate.com/holidays/us/'
            holiday_url = url + year
            html = getHTML(holiday_url)
            soup = BeautifulSoup(html,'html.parser')  

            for tr in soup.find_all('tr'):
                title = tr.find('a')
                date = tr.find('th', class_ = 'nw')
                if title != None and date != None:
                    print(title.text)
                    print(date.text)

    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return len(self.innerHolidays)
    
    def filter_holidays_by_week(self, year, week_number):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
        filteredyear = list(filter(lambda x: x.date.year == year, self.innerHolidays))
        filteredweek = list(filter(lambda x: x.date.isocalender().week == week_number, filteredyear))
        return filteredweek

    def displayHolidaysInWeek(self, holidayList):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.
        for i in holidayList:
            print(i)

    def getWeather(self):
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.
        url = "https://community-open-weather-map.p.rapidapi.com/forecast"
        querystring = {"q":"san francisco,us"}
        headers = {
	        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
	        "X-RapidAPI-Key": "83e29e690emsh9d341972b56a483p1a7e46jsnef585f7ca8a3"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()

        weatherlist = []
        for i in range(5):
            weatherlist.append(data['list'][8*i]['weather'][0]['description'])
        return weatherlist


    def viewCurrentWeek(self):
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results
        weatherinput = input('do you want to see the weather')
        currentweek = datetime.date.today().isocalendar().week
        currentyear = datetime.date.today().isocalendar().year
        filterholidays = self.filter_holidays_by_week(currentyear, currentweek)
        dates = []
        if weatherinput == 'n':
            self.displayHolidaysInWeek
        else:
            weatherlist = self.getWeather()
        



def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 
    TheList = HolidayList()
    TheList.read_json('holidays.json')
    TheList.scrapeHolidays()
    TheList.numHolidays()
    user = True

    while user == True:
        print("Holiday Menu")
        print("=========")
        print("1. Add a Holiday")
        print("2. Remove a Holiday")
        print("3. Save Holiday List")
        print("4. View Holidays")
        print("5. Exit")
        choice = input("Pick a number")

        if choice == 1:
            print("Add a Holiday")
            print("===========")
            name = input("Holiday:")
            date = input("Date:")
            TheList.addHoliday(Holiday(name, date))
            print(name + date + " has been added to the Holiday List")

        if choice == 2:
            print("Remove a Holiday")
            print("============")
            name = input("Holiday:")
            date = input("Date:")
            TheList.removeHoliday(name, date)

        if choice == 3:
            print("Save Holiday List")
            print("==========")
            usersinput = input("Are you sure you want to save your changes? [y/n]")
            if usersinput == 'y':
                TheList.save_to_json()
                print("Sucess:")
                print("Your changes have been saved.")
            else:
                print("Cancelled:")
        
        if choice == 4:
            print("View Holidays")
            print("============")
            whichyear = input("Which year?:")
            whichweek = input("Which week?")
            seeweather = input("Would you like to see this week's weather? [y/n]")
            if seeweather == 'y':
                weather = TheList.getWeather()
                TheList.viewCurrentWeek(1, weather)
            TheList.filter_holidays_by_week(whichyear, whichweek)

        if choice == 5:
            print("Exit")
            print("=====")
            user = False











if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.
holiday_list = HolidayList()
holiday_list.scrapeHolidays()


test = Holiday('halloween', '10-31-2021')     
add_test = HolidayList()
add_test.addHoliday(test)
