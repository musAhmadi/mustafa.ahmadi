from selenium import webdriver
import csv
def JobLocation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(120)
    url="https://www.jobs.af/"
    driver.get(url)

    href=[]
    job_location=[]
    elm=driver.find_elements_by_xpath('//div[@class="item-header"]//h2//a')
    for i in elm:
        try:
            href.append(i.get_attribute('href'))
        except Exception as e:
            print(e)

    for i in href:

        driver.get(i)

        try:
            t=driver.find_element_by_xpath('//div[@class="vertical-stats small ng-star-inserted"]//span[@itemprop="jobLocation"]//span[@itemprop="address"]')
            job_location.append(t.text)
        except:
            job_location=['']




    with open('joblocation.csv','w') as f:
        f.write("Url,Joblocation \n")
    with open('joblocation.csv', 'a') as data_file:

        for i in range(0,12):

            data_file.write(str(href[i])+ "," + str(job_location[i]) + "\n")


    driver.close()
if __name__ == '__main__':
    JobLocation()