from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
#import pandas as pd
#from tabulate import tabulate
import os
import time


def getSCFT(book, driver, id):
    try:
        selections = driver.find_element_by_id(id)
    except Error:
        return []
    options = [x for x in selections.find_elements_by_tag_name("option")]
    option = []
    for element in options:
        option.append(element.get_attribute("text") )
    return option

def doLinks(file, driver):
    links = driver.find_elements_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a')
    t = '...'
    cont = driver.find_elements_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a[11]')
    j = len(cont)
    while(j != 0):
        links = driver.find_elements_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a')
        time.sleep(3)
        soup = []
        #print(len(links))
        if(len(links)!= 0):
            links = links[1:]
            for i in range(1, len(links)+1, 1):
                driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a['+str(i) + ']').click()
                soup+=BeautifulSoup(driver.page_source, 'lxml')
                time.sleep(5)
        for x in soup:
            clist = x.find_all('span', {'class': 'Title'})
            for item in clist:
                file.write(item.text)
                file.write('\n\n')
        time.sleep(4)
        links = []
        cont = driver.find_elements_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a[11]')
        if (len(cont)>0):
            j = 1
        else:
            j -=1

def getBook(book, driver, file):
    #After opening the url above, Selenium clicks the specific agency link
    driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddbook']/option[text()="+'\"aSTAGga saMgraha\"'+"]").click()
    time.sleep(5)
    sections = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddsection');

    for section in sections:
        driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddsection']/option[text()='"+'\"uttarasthAnam\"'+"']").click()
        time.sleep(2)
        chapters = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddchapter');
        for chapter in chapters:
            if chapter == 'annasvarUpavijJAnIyaH adhyAyaH':
                chapter = 'annasvarUpavijJAnIyaH     adhyAyaH'
            if chapter == 'mUtrAghAtanidAnam adhyAyaH':
                chapter = 'mUtrAghAtanidAnam  adhyAyaH'
            driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddchapter']/option[text()='"+'\"rasAyanavidhiH\"'+"']").click()
            time.sleep(5)
            fm = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddfrom');
            if(len(fm)>0):
                print('from ', fm[0])
                print('from ', fm[1])
                driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddfrom']/option[text()='"+fm[1]+"']").click()
                time.sleep(3)
                to = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddto');
                if(len(to)> 0 ):
                    print('to ', to[len(to) - 1])
                    driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddto']/option[text()='"+to[len(to)-1]+"']").click()
                    time.sleep(5)
                    python_button = driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSearch') #FHSU
                    python_button.click() 
                    time.sleep(7)
                    soup_level1=BeautifulSoup(driver.page_source, 'lxml')
                    clist = soup_level1.find_all('span', {'class': 'Title'})
                    for item in clist:
                        file.write(item.text)
                        file.write('\n\n')
                    #print(clist)
                    #print('=====================')

                    links = driver.find_elements_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a')
                    time.sleep(3)
                    soup = []
                #print(len(links))
                    if(len(links)!= 0):
                        for i in range(1, len(links)+1, 1):
                            driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a['+str(i) + ']').click()
                            soup+=BeautifulSoup(driver.page_source, 'lxml')
                            time.sleep(5)
                    for x in soup:
                        clist = x.find_all('span', {'class': 'Title'})
                        for item in clist:
                            file.write(item.text)
                            file.write('\n\n')
                    time.sleep(4)

                    doLinks(file, driver)

                    #print(clist)
                #    print('=======================')
                #print('$$$$$$$$$$$$$$$$$$$$$$$$$')


        

#launch url
url = "http://ayutexts.dharaonline.org/frmread.aspx"

# create a new Firefox session
driver = webdriver.Chrome('/Users/poojaprakash/Downloads/chromedriver')
driver.implicitly_wait(30)
driver.get(url)

books = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddbook');

for book in books:
    file = open('ayutextsData/'+book+'.txt', 'w+')
    time.sleep(3)
    getBook(book, driver, file)
        
# driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddfrom']/option[text()='0']").click()
# driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddto']/option[text()='140']").click()

# python_button = driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSearch') #FHSU
# python_button.click() #click fhsu link

# time.sleep(5)
# #Selenium hands the page source to Beautiful Soup
# soup_level1=BeautifulSoup(driver.page_source, 'lxml')

# links = driver.find_elements_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a')
# soup = []
# print(len(links))
# if(len(links)!= 0):
#     for i in range(1, len(links)+1, 1):
#         driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a['+str(i) + ']').click()
#         soup+=BeautifulSoup(driver.page_source, 'lxml')
#         time.sleep(2)

# for x in soup:
#     clist = x.find_all('span', {'class': 'Title'})
    
#     print(clist)
 
# datalist = [] #empty list
# x = 0 #counter
# clist = soup_level1.find_all('span', {'class': 'Title'})
# for x in clist:
#     #file.write(x, '\n')
#     print(x)
#Beautiful Soup finds all Job Title links on the agency page and the loop begins
# for link in soup_level1.find_all('a', id=re.compile("^ctl00_ContentPlaceHolder1_dgFullText")):
    
#     #Selenium visits each Job Title page
#     python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
#     python_button.click() #click link
    
#     #Selenium hands of the source of the specific job page to Beautiful Soup
#     soup_level2=BeautifulSoup(driver.page_source, 'lxml')

#     #Beautiful Soup grabs the HTML table on the page
#     table = soup_level2.find_all('table')[0]
    
#     #Giving the HTML table to pandas to put in a dataframe object
#     df = pd.read_html(str(table),header=0)
    
#     #Store the dataframe in a list
#     datalist.append(df[0])
    
#     #Ask Selenium to click the back button
#     driver.execute_script("window.history.go(-1)") 
    
#     #increment the counter variable before starting the loop over
#     x += 1
    
    #end loop block
    
#loop has completed

#end the Selenium browser session
driver.quit()
file.close()

#combine all pandas dataframes in the list into one big dataframe
# result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))],ignore_index=True)

# #convert the pandas dataframe to JSON
# json_records = result.to_json(orient='records')

# #pretty print to CLI with tabulate
# #converts to an ascii table
# print(tabulate(result, headers=["Employee Name","Job Title","Overtime Pay","Total Gross Pay"],tablefmt='psql'))

# #get current working directory
# path = os.getcwd()

# #open, write, and close the file
# f = open(path + "\\fhsu_payroll_data.json","w") #FHSU
# f.write(json_records)
# f.close()
