from selenium import webdriver
import csv
def JobKeyword():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(120)
    url="https://www.jobs.af/"
    driver.get(url)

    href=[]
    job_keyword=[]
    elm=driver.find_elements_by_xpath('//div[@class="item-header"]//h2//a')
    for i in elm:
        try:
            href.append(i.get_attribute('href'))
        except Exception as e:
            print(e)

    for i in href:

        driver.get(i)

        try:
            t=driver.find_elements_by_xpath('//*[./preceding-sibling::h3="Job Keywords:"]')

        except:
            t=''

        for i in t:
            job_keyword.append(i.text)


    #
    # with open('jobkeyword.csv','w') as f:
    #     f.write("Url,Emial \n")
    # with open('jobkeyword.csv', 'a') as data_file:

    for i in job_keyword:
        print("-----------------------------------")
        print(i)
        print("-----------------------------------")



    driver.close()
if __name__ == '__main__':
    JobKeyword()