from selenium import webdriver
import csv
def table():
    driver = webdriver.Chrome()
    driver.implicitly_wait(120)
    url="https://www.jobs.af/"
    driver.get(url)
    driver.maximize_window()

    item={}
    item['post_date'] =['']
    item['reference'] =['']
    item['closing_date'] =['']
    item['work_type'] =['']
    item['nubmer_of_vacancies'] =['']
    item['gender'] =['']
    item['functional_area'] =['']
    item['nationality'] =['']
    item['salary_range'] =['']
    item['year_of_expirence'] =['']
    item['contract_duration_year'] =['']
    item['extension_passibility'] =['']

    item['contract_type'] =['']
    item['probation_month'] =['']
    item['required_langauges'] =['']

    href=[]
    elements=driver.find_elements_by_xpath('//div[@class="item-header"]//h2//a')
    for element in elements:
        try:
            href.append(element.get_attribute('href'))
        except Exception as e:
            print(e)
    # with open('table.csv', 'w') as f:
    #     f.write("'Post_data',Refernce,'Closing_date',Work_type,Nubmer_of_vacancies,Gender,Functional_area,Nationality,Salary_range,year_of exprience,contract_duration,Extention_passibility,contract_type ,probation_month, required_langauges \n")
    for i in href:

        driver.get(i)


        item['post_date'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[1]//td[1]').text)



        item['reference'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[2]//td[1]').text)

        item['closing_date'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[1]//td[2]').text)

        item['work_type'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[2]//td[2]').text)

        item['nubmer_of_vacancies'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[3]//td[1]').text)

        item['gender'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[3]//td[2]').text)

        item['functional_area'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[4]//td[1]').text)

        item['nationality'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[4]//td[2]').text)

        item['salary_range'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[5]//td[1]').text)

        item['year_of_expirence'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[5]//td[2]').text)

        item['contract_duration_year'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[6]//td[1]').text)

        item['extension_passibility'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[6]//td[2]').text)

        item['contract_type'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[7]//td[1]').text)

        item['probation_month'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[7]//td[2]').text)

        item['required_langauges'].append(driver.find_element_by_xpath('//div[@class="table-responsive"]//tbody//tr[8]//td[1]').text)

        # with open('table.csv', 'a') as data_file:
        #     for i in range(0,15):
        #
        #         data_file.write(str(item['post_date']) + "," + str(item['reference'])+ "," + str(item['closing_date'])+ "," +str(item['work_type'])+ "," +str(item['nubmer_of_vacancies'])+ "," +str(item['gender'])+ "," + str(item['functional_area'])+ "," +str(item['nationality'])+ "," +str(item['salary_range'])+ "," +str(item['year_of_expirence'])+ "," +str(item['contract_duration_year'])+ "," + str(item['extension_passibility'])+ "," + str(item['contract_type'])+ "," + str(item['probation_month'])+ "," +str(item['required_langauges']) + "\n")
    for i in item:

        print(item[i])

    driver.close()
if __name__ == '__main__':
    table()