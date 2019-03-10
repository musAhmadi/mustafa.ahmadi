from selenium import webdriver
import csv
def Qulification():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(120)
    # url1="https://www.jobs.af/all-sitemaps/jobs/jobs.xml"
    url="https://www.jobs.af/"
    driver.get(url)

    href=[]
    qulification=[]
    elm=driver.find_elements_by_xpath('//div[@class="item-header"]//h2//a')
    for i in elm:
        try:
            href.append(i.get_attribute('href'))
        except Exception as e:
            print(e)

    for i in href:

        driver.get(i)

        try:
            t=driver.find_elements_by_xpath('//*[./preceding-sibling::h3="Qualifications:"]//p')

        except:
            t=''

        for i in t:
            qulification.append(i.text)

    for i in qulification:
        print(i)

    # with open('qualification.csv','w') as f:
    #     f.write("Url,Qualification \n")
    # with open('qualification.csv', 'a') as data_file:
    #
    #     for i in range(0,len(qulification)):
    #
    #         data_file.write(str(href[i])+ "," + str(qulification[i]) + "\n")
    #

    driver.close()
if __name__ == '__main__':
    Qulification()