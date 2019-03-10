from selenium import webdriver
import csv
def Skill():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(120)
    url="https://www.jobs.af/"
    driver.get(url)

    href=[]
    skill_required=[]
    elm=driver.find_elements_by_xpath('//div[@class="item-header"]//h2//a')
    for i in elm:
        try:
            href.append(i.get_attribute('href'))
        except Exception as e:
            print(e)

    for i in href:

        driver.get(i)

        try:
            t=driver.find_elements_by_xpath('//div[@class="item-skills"]//span[@class="skill-item ng-star-inserted"]//span')

        except:
            t=''

        for i in t:
            skill_required.append(i.text)


    with open('submission.csv','w') as f:
        f.write("Url , Title \n")
    with open('submission.csv', 'a') as data_file:

        for i in range(0,len(skill_required)):

            data_file.write(str(href[i])+ "," + str(skill_required[i]) + "\n")


    driver.close()
if __name__ == '__main__':
    Skill()