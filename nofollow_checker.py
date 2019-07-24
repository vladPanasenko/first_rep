from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
ready_file = open("ready_links.txt", "w", encoding="utf-8")


def parse_txt_to_list():
    empty_list = []

    with open("domains.txt", "r") as links_list:
        each_url = links_list.readlines()

    for url in each_url:
        resp = session.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')
        links_on_the_page = soup.find("a", attrs={"href": "https://www.superiorpapers.com/"})
        empty_list.append(links_on_the_page)

    return empty_list


def detect_nofollow():
    links_to_check = parse_txt_to_list()
    for link in links_to_check:
        if "nofollow" in str(link):
            print(link)


if __name__ == "__main__":
    detect_nofollow()
