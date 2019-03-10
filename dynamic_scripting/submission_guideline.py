from selenium import webdriver
import csv
def Submission_guidline():
    driver = webdriver.Chrome()
    driver.implicitly_wait(120)
    url="https://www.jobs.af/"
    driver.get(url)

    href=[]
    submisssion_guidline=[]
    elm=driver.find_elements_by_xpath('//div[@class="item-header"]//h2//a')
    for i in elm:
        try:
            href.append(i.get_attribute('href'))
        except Exception as e:
            print(e)

    for i in href:

        driver.get(i)

        try:
            t=driver.find_elements_by_xpath('//*[./preceding-sibling::h3="Submission Guideline:"]//p')



        except:
            t=''

        for i in t:
            submisssion_guidline.append(i.text)

    with open('submission_quidline.csv','w') as f:
        f.write("Url , Title \n")
    with open('submission_quidline', 'a') as data_file:
        for i in range(0,12):

            data_file.write(str(href[i])+ "," + str(submisssion_guidline[i]) + "\n")

    driver.close()
if __name__ == '__main__':
    Submission_guidline()