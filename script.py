'''
Created on 05/04/2017

@author: Rachappa
'''
from selenium import webdriver
import time





if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.makemytrip.com/car-rental/ola_cabs-online-booking.php")
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='locCity']/p/span[2]/span[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='ui-active-menuitem']").click()
    driver.find_element_by_xpath(".//*[@id='carsLandingForm']/div[3]/div[4]/table/tbody/tr/td[2]/div/p/span[1]/span/a").click()
    driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[3]/td[4]/a").click()
    driver.find_element_by_xpath(".//*[@id='customerEmail']").send_keys("Rachappahalinge@gmail.com")
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='rightblock']/div[2]/ul/li[1]/a").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='oneway']").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='outFromCity']/p/span[2]/span[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='ui-active-menuitem']").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='outToCity']/p/span[2]/span[2]").send_keys("Mum")
    time.sleep(3)
    driver.find_element_by_xpath("html/body/ul[5]/li[1]/a").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='carsLandingForm']/div[3]/div[4]/table/tbody/tr/td[2]/div/p/span[1]/span/a").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[3]/td[6]/a").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='cal_icn flL']").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[4]/td[2]/a").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='customerEmail']").send_keys("Rachappahalinge@gmail.com")
    driver.execute_script("window.scrollTo(5, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='leftblock']/div[4]/table/tbody/tr[8]/td[6]/a").click()

    
    
    #driver.find_element_by_xpath("//a[class='ui-corner-all']").click
    
    #driver.find_element_by_xpath(".//*[@id='source']").send_keys("Bidar")
    #driver.find_element_by_xpath(".//*[@id='destination']").send_keys("Bangalore")
    #driver.find_element_by_xpath(".//*[@id='datepicker1']").click()
    #driver.find_element_by_xpath("//a[text()='24']").click()
    #driver.find_element_by_xpath(".//*[@id='datepicker2']").click()
    #driver.find_element_by_xpath("//a[text()='26']").click()
    #driver.find_element_by_xpath(".//*[@id='roundTrip']/a").click()
