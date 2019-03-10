from selenium import webdriver
import csv
def Skill():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(120)
    url="https://www.jobs.af/"
    driver.get(url)

    href=[]
    duties_responsibilty=[]
    elm=driver.find_elements_by_xpath('//div[@class="item-header"]//h2//a')
    for i in elm:
        try:
            href.append(i.get_attribute('href'))
        except Exception as e:
            print(e)

    for i in href:

        driver.get(i)

        try:
            t=driver.find_elements_by_xpath('//*[./preceding-sibling::h3="Duties & Responsibilities:"]//p')

        except:
            t=''

        for i in t:
            duties_responsibilty.append(i.text)


    with open('submission.csv','w') as f:
        f.write("Url , Title \n")
    with open('submission.csv', 'a') as data_file:

        for i in range(0,12):

            data_file.write(str(href[i])+ "," + str(duties_responsibilty[i]) + "\n")


    driver.close()
if __name__ == '__main__':
    Skill()