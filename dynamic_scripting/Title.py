from selenium import webdriver
import csv
def Title():
    driver = webdriver.Chrome()
    driver.implicitly_wait(120)
    url="https://www.jobs.af/"
    driver.get(url)

    href=[]
    title=[]
    elm=driver.find_elements_by_xpath('//div[@class="item-header"]//h2//a')
    for i in elm:
        try:
            href.append(i.get_attribute('href'))
        except Exception as e:
            print(e)

    for i in href:

        driver.get(i)

        try:
            t=driver.find_element_by_xpath('//div[@class="item-header job-view"]//h1//span').text.encode('utf-8')

            title.append(t)

        except Exception as e:
            print(e)



    with open('write_data.csv','w') as f:
        f.write("Url , Title \n")
    with open('write_data.csv', 'a') as data_file:
        for i in range(0,12):

            data_file.write(str(href[i])+ "," + str(title[i]) + "\n")

    driver.close()
if __name__ == '__main__':
    Title()