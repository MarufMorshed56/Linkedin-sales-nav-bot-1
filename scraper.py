# import collections
import profile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# import clipboard
import time
from threading import Thread
import var
import shutil
from pyautogui import alert, write, press


class Scraper():
    def __init__(self):
        self.email = var.email
        self.password = var.password
        Thread(target=self.stop, daemon=True).start()

    def run(self):
        try:
            # login handle
            """ There was three case in total here.
            1. Remember me : true
            2. Remember me : true different account
            3. Remember me : false """

            if var.remember_me:
                chrome_options = Options()
                chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                chrome_options.add_argument("user-data-dir=selenium")

                if self.email == var.cookies_of:

                    self.driver = webdriver.Chrome(
                        executable_path='chromedriver.exe', chrome_options=chrome_options)
                    # changed this line from => executable_path='chromedriver', chrome_options=chrome_options)
                    self.driver.get(var.primary_link)
                    try:
                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(
                                (By.ID, "global-typeahead-search-input")))
                        self.driver.find_element_by_id(
                            "global-typeahead-search-input")
                    except:
                        print("Logging in....")
                        self.login()

                else:
                    try:
                        shutil.rmtree("selenium")
                    except:
                        print("Can't delete")
                    chrome_options = Options()
                    chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                    self.driver = webdriver.Chrome(
                        executable_path='chromedriver', chrome_options=chrome_options)
                    self.login()

                var.cookies_of = self.email

            else:
                chrome_options = Options()
                chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                self.driver = webdriver.Chrome(
                    executable_path='chromedriver.exe', chrome_options=chrome_options)
                # changed this line from => self.driver = webdriver.Chrome(executable_path='chromedriver')
                self.login()

            var.driver = self.driver
            # wait till start button is pushed
            # self.scrap()
            print("Login Done ...")
        except Exception as e:
            print("Exeception occured at scraper init :{}".format(e))
            var.status = False
            var.stop = True

        # finally:
        #     print("closing the thread")

    def login(self):
        self.driver.get(var.primary_link)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)
        self.driver.find_element_by_tag_name("body").send_keys(
            Keys.TAB + self.email + Keys.TAB + self.password + Keys.ENTER)

        time.sleep(1)

    def scrap(self):
        links = []
        Name = []
        CompanyName = []
        Designation = []
        Location = []
        normal_link = []
        # sup = []
        print("starting to scrape....")
        # start_time = time()
        limit = var.page_number
        profile_count = 0
        var.remaining_page = limit
        var.profile_count = profile_count
        step = var.scrolling_step
        try_count = var.try_count
        link = 0
        b = 0
        c = 0
        delay_time = var.delay
        count3 = 0
        try:
            
            # looping through every page

            self.driver.maximize_window()
            time.sleep(1)

            for count3 in range(0, limit):
                count3 = (count3 + 1)
                # limit is total page number & count3 is the iterator
                if var.stop == True:
                    break
                count = 0

                normal_link = []
                link = 0
                b = 0
                c = 0

                for i in range(try_count):
                    count = count + step
                    self.driver.execute_script(
                        "document.querySelector('#content-main > div > div.full-width > div.p4._vertical-scroll-results_1igybl').scrollTop={}".format(count))
                    time.sleep(0.5)
                # runs the scrolling action, try_count = number of scrolls, count = number of pixels to scroll per time

                temp = list()
                try:

                    try:

                        all_lists = self.driver.find_elements_by_css_selector(
                            'a[data-anonymize="person-name"]')
                        print("links {}".format(len(all_lists)))
                        for lists in all_lists:
                            if var.stop == True:
                                break
                            profile_count += 1
                            var.profile_count = profile_count
                            #  updates the gui profile variable , Scrapping the lnkedin_sales_navigator urls of each profile
                            try:
                                link = lists.get_attribute("href")
                                links.append(link)

                                b = link.split(',')[0]

                                # print(b)

                                c = b.replace("/sales/people/", "/in/")

                                # print(c)

                                normal_link.append(c)

                            except Exception as e:
                                links.append("not available")
                    except Exception as e:
                        print("can't get links")

                    try:
                        names = self.driver.find_elements_by_css_selector(
                            'a[data-anonymize="person-name"]')

                        for item in names:
                            if var.stop == True:
                                break
                            try:
                                Name.append(item.text)
                            except Exception as e:
                                Name.append("not available")
                        print("Name {}".format(len(names)))
                    except Exception as e:
                        print("can't get Names")

                    try:
                        #  Scrapes the total "Company_name & position" div then  splits the inner info into chunks & gets the Array which contains the "position" information
                        company_names = self.driver.find_elements_by_css_selector(
                            'div[data-test-lead-result-entity="title-at-company"]')
                        for item in company_names:
                            if var.stop == True:
                                break
                            try:
                                try:
                                    link = item.find_element_by_class_name(
                                        "ember-view")
                                    CompanyName.append(link.text)

                                except Exception as e:
                                    str = item.get_attribute('innerHTML')
                                    str_1 = (str.split('>'))
                                    str_2 = ''
                                    # print(new_str)
                                    for sentence in str_1:
                                        if 'aria-label' in sentence:
                                            str_2 = sentence

                                    str_3 = (str_2.split('"')[0])
                                    company_op = (str_3.split('<')[0])
                                    
                                    company_op2 = company_op.strip()

                                    company_name = company_op2.replace(
                                        "amp;", "")

                                   
                                    CompanyName.append(company_name)

                                    # print("////////////////////////////////")
                            except Exception as e:
                                CompanyName.append("not found")
                                # print(company)
                        print("company_names {}".format(len(company_names)))
                    except Exception as e:
                        print("Exeception occured at scrap : {} ".format(e))
                        # print("can't get Company Names")

                    try:
                        lists = self.driver.find_elements_by_css_selector(
                            'div[data-test-lead-result-entity="title-at-company"]')
                        #  Scrapes the total "Company_name & position" div then  splits the inner info into chunks & gets the Array which contains the "position" information
                        for item in lists:
                            try:
                                str = item.get_attribute('innerHTML')
                                position_str = (str.split('<span>')[-1])
                                designation_op = (position_str.split('<')[0])

                                designation = designation_op.replace(
                                    "amp;", "")

                                Designation.append(designation)

                            except:
                                Designation.append("not available")
                        print("lists {}".format(len(lists)))

                    except Exception as e:
                        print("can't get position")

                    try:
                        locations = self.driver.find_elements_by_css_selector(
                            'div[data-test-lead-result-entity="geo"]')

                        for item in locations:
                            try:
                                Location.append(item.text)
                            except Exception as e:
                                Location.append("not available")
                        print("locations {}".format(len(locations)))
                    except Exception as e:
                        print("can't get positions")

                    try:
                        # Scrapes the linkedin Premium icon data: boolean(true / false)
                        premium_divs = self.driver.find_elements_by_css_selector(
                            'div[class="artdeco-entity-lockup__content ember-view"]')
    
                        for premium_div in premium_divs:
                            try:
                                profile_status = premium_div.find_element_by_css_selector(
                                    'li-icon[type="linkedin-premium-gold-icon"]')
                                
                                ProfileStatus.append("Premium")
                            except:
                                ProfileStatus.append("Not")
                        x = len(ProfileStatus)
                        print('profile_status {}'.format(len(ProfileStatus)))
                        

                    except Exception as e:
                        print("can't get profile premium info")

                    for i in range(len(Name)):
                        leStatus[i] = "this 25 data may be corrupted"

                        try:
                            tempDict = {
                                "Key_Code": '',
                                "Sort_Code": '',
                                "List_Code": '',
                                "Mr_Mrs": '',
                                "First_Last": Name[i],
                                "Org": CompanyName[i],
                                "Job_title": Designation[i],
                                "Location": Location[i],
                                "LinkedIn_Link": normal_link[i],
                                "Sales_nav_link": links[i]
                            }

                            temp.append(tempDict.copy())
                            # print(Name[i])
                            # print( Location[i])
                            # print( Designation[i])
                            # print( CompanyName[i])
                            # print( links[i])
                            # print(ProfileStatus[i])
                            # print(i)
                            # print("\n")
                            # collection.append(tempDict.copy())
                            # elem.remove(item)
                        except Exception as e:
                            print("Exeception occured at scrap : {} ".format(e))
                            print("can't scrape data")
                            pass

                except Exception as e:
                    print("Exeception occured at scrap : {} ".format(e))

                for item in temp:
                    var.scrap_data.append(item)

                var.remaining_page = limit - (count3)


                var.profile_count = profile_count
                print("  Page Count : {} \n  Profile Count : {} ".format(
                    count3, profile_count))
                

                Name = []
                Designation = []
                Location = []
                CompanyName = []
                links = []
                ProfileStatus = []

                if(count3 < (limit)):
                    time.sleep(1)
                    try:
                        next_btn = self.driver.find_element_by_css_selector(
                            'button[aria-label="Next"]')
                        next_btn.click()
                    except Exception as e:
                        print("no more page exist")
                        break

                time.sleep(delay_time)



            alert(text='Total Profile : {}'.format(
                profile_count), title='', button='OK')

        except Exception as e:
            print("Exeception occured at scrap : {} ".format(e))
            var.status = False
            var.stop = True

        finally:
            var.scarp_start = False
            print("scrap func finished")

    def stop(self):
        while True:
            time.sleep(1)
            if var.stop == True:
                try:
                    var.status = False
                    self.driver.quit()
                    print("Process : Closing the browser")
                except Exception as e:
                    print("Exeception occured at stop : {} ".format(e))
                finally:
                    break


def run():
    scraper = Scraper()
    scraper.run()
    while var.status == True:
        time.sleep(1)
        if var.scarp_start == True:
            scraper.scrap()
            print("out of scrap func")
    var.status = False
    var.scarp_start = False
    print("Closing the thread")


if __name__ == "__main__":
    pass
