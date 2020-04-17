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
    time.sleep(3)
    soup = []
    print(len(links))
    if(len(links)!= 0):
        links = driver.find_elements_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a')
        links = links[1:]
        print('inside links', links)
        for i in range(2, len(links)+2, 1):
            driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a['+str(i) + ']').click()
            soup+=BeautifulSoup(driver.page_source, 'html.parser')
            time.sleep(5)
    for x in soup:
        clist = x.find_all('span', {'class': 'Title'})
        for item in clist:
            print(item.text)
            file.write(item.text)
            file.write('\n\n')
    time.sleep(4)
    links = []
    cont = driver.find_elements_by_xpath('//a[contains(text(),\'...\')]')
    print(len(cont))
    if(len(cont)==1):
        links = driver.find_elements_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a')
        time.sleep(3)
        soup = []
        print(len(links))
        if(len(links)!= 0):
            links = links[1:]
            print('inside links2', links)
            for i in range(9, len(links)+2, 1):
                driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a['+str(i) + ']').click()
                soup+=BeautifulSoup(driver.page_source, 'html.parser')
                time.sleep(5)
        for x in soup:
            clist = x.find_all('span', {'class': 'Title'})
            for item in clist:
                print(item.text)
                file.write(item.text)
                file.write('\n\n')
        time.sleep(4)
        soup_level1=BeautifulSoup(driver.page_source, 'html.parser')
        clist = soup_level1.find_all('span', {'class': 'Title'})
        for item in clist:
            file.write(item.text)
            file.write('\n\n')
        print('in do links', clist)

        return
    

def getBook(book, driver, file):
    #After opening the url above, Selenium clicks the specific agency link
    driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddbook']/option[text()='"+book+"']").click()
    time.sleep(5)
    sections = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddsection');

    for section in sections:
        driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddsection']/option[text()='"+section+"']").click()
        time.sleep(2)
        chapters = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddchapter')
        for chapter in chapters:
            print('chapter ', chapter, 'xx')
            if chapter == 'annasvarUpavijJAnIyaH adhyAyaH':
                chapter = 'annasvarUpavijJAnIyaH     adhyAyaH'
            if chapter == 'mUtrAghAtanidAnam adhyAyaH':
                chapter = 'mUtrAghAtanidAnam  adhyAyaH'
            if chapter == 'atha vAtavyAdhinidAnam':
                chapter = 'atha vAtavyAdhinidAnam '
            if chapter == 'atha mUtrakRcchranidAnam':
                chapter = 'atha mUtrakRcchranidAnam '
            if chapter == 'atha CArIravraNanidAnam':
                chapter = 'atha CArIravraNanidAnam '
            if chapter == 'atha CUkadoSanidAnam':
                chapter = 'atha CUkadoSanidAnam '
            if chapter == 'atha nAsAroganidAnam':
                chapter = 'atha nAsAroganidAnam '
            if chapter == 'atha yonikandanidAnam':
                chapter = 'atha yonikandanidAnam '
            if chapter == 'atha stanyaduSTinidAnam':
                chapter = 'atha stanyaduSTinidAnam '
            if chapter == 'atha viSaroganidAnam':
                chapter = 'atha viSaroganidAnam '
            if chapter == 'atha viSayAnukramaNikA':
                chapter = 'atha viSayAnukramaNikA '
                continue
            if chapter == 'atha yakRdrogAdhikAraH':
                chapter = 'atha  yakRdrogAdhikAraH '
            if chapter == 'grahaNIroge pathyApathyam':
                chapter = 'grahaNIroge  pathyApathyam'
            if chapter == 'dantaroge pathyam':
                chapter = 'dantaroge~pathyam'
            if chapter == 'viSAroge pathyApathyam':
                time.sleep(7)
                driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddchapter']/option[text()='"+chapter+"']").click()
                time.sleep(5)
                fm = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddfrom');
                if(len(fm)>0):
                    print('from ', fm[1])
                    countFile.write('\n' + str(fm[1]))
                    driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddfrom']/option[text()='"+fm[1]+"']").click()
                    time.sleep(3)
                    to = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddto');
                    if(len(to)> 0 ):
                        print('to ', '\n'+ str(to[len(to) - 1]))
                        countFile.write(to[len(to) - 1])
                        driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddto']/option[text()='"+to[len(to)-1]+"']").click()
                        time.sleep(5)
                        python_button = driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSearch') #FHSU
                        python_button.click() 
                        time.sleep(7)
                        

                        links = driver.find_elements_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a')
                        time.sleep(3)
                        soup = []
                        print('starting 2nd page', len(links))
                        if(len(links)!= 0):
                            for i in range(1, len(links)+1, 1):
                                print(str(i))
                                time.sleep(5)
                                driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dgFullText"]/tbody/tr[13]/td/a['+str(i) + ']').click()
                                soup +=BeautifulSoup(driver.page_source, 'lxml')
                                time.sleep(5)
                            for x in soup:
                                clist = x.find_all('span', {'class': 'Title'})
                                for item in clist:
                                    print('clist ', item.text)
                                    file.write(item.text)
                                    file.write('\n\n')
                            time.sleep(4)

                        soup_level1=BeautifulSoup(driver.page_source, 'lxml')
                        clist = soup_level1.find_all('span', {'class':'Title'})
                        for item in clist:
                            print(item.text)
                            file.write(item.text)
                            file.write('\n\n')
                        print('=====================')
                        t = '...'
                        cont = driver.find_elements_by_xpath('//a[contains(text(),\'...\')]')
                        j = len(cont)
                        print('number of paginations', j)
                        if(len(cont) > 0):
                            print('in do links')
                            doLinks(file, driver)
                            print('=======================')
                        print('$$$$$$$$$$$$$$$$$$$$$$$$$')


        

#launch url
url = "http://ayutexts.dharaonline.org/frmread.aspx"

# create a new Firefox session
driver = webdriver.Chrome('/Users/poojaprakash/Downloads/chromedriver')
driver.implicitly_wait(30)
driver.get(url)

books = getSCFT('caraka saMhita', driver, 'ctl00_ContentPlaceHolder1_ddbook')

books = books[1:]
for book in books:
    # 
    if(book != 'caraka samhitA' and book != 'suCruta samhitA' and book != 'aSTAGga hRdaya' and book != 'aSTAGga saMgraha' and book != 'mAdhava nidAna'):
        file = open('ayutextsData/'+book+'.txt', 'w+')
        countFile = open('ayutextsData/'+book+'counts.txt', 'w+')
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
