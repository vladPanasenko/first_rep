from selenium import webdriver
from time import sleep

path_to_driver = "chromedriver.exe"


def open_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--headless')
    browser = webdriver.Chrome(executable_path=path_to_driver, options=chrome_options)
    url = 'https://www.google.com.ua'
    browser.get(url)
    search_field = browser.find_element_by_name('q')
    print("Enter keyword to parse!")
    keyword = input()
    search_field.send_keys(keyword)
    sleep(4)

    tips = search_field.find_elements_by_xpath('//div[@class="sbl1"]/span')
    tips_list = []

    for tip in tips:
        tips_list.append(tip.text)

    return tips_list

    browser.quit()


def add_to_file(tips_to_add):

    with open("tips.txt", "w", encoding="utf-8") as file:
        for i in tips_to_add:
            file.writelines(i + "\n")


if __name__ == '__main__':
    add_to_file(open_browser())
