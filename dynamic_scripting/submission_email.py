from selenium import webdriver
import csv
def Submission():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(120)
    url="https://www.jobs.af/"
    driver.get(url)

    href=[]
    submisssion_email=[]
    elm=driver.find_elements_by_xpath('//div[@class="item-header"]//h2//a')
    for i in elm:
        try:
            href.append(i.get_attribute('href'))
        except Exception as e:
            print(e)

    for i in href:

        driver.get(i)

        try:
            t=driver.find_element_by_xpath('//a[@tooltip="Submission Email"]')
            submisssion_email.append(t.get_attribute('href'))
        except:
            submisssion_email=['']


    for i in submisssion_email:
        print(i)


    # with open('submission.csv','w') as f:
    #     f.write("Url,Emial \n")
    # with open('submission.csv', 'a') as data_file:
    #
    #     for i in range(0,len(submisssion_email)):
    #
    #         data_file.write(str(href[i])+ "," + str(submisssion_email[i]) + "\n")
    #

    driver.close()
if __name__ == '__main__':
    Submission()