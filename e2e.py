from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from MainScores import score_server
import time
import sys

url = "http://127.0.0.1:5000"

def test_scores_service():
    service = Service("C:\\Users\ortal\.cache\selenium\chromedriver\win32\108.0.5359.71\chromedriver.exe")
    service.start()
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    score = int(driver.find_element("id", "score").text)
    # driver.quit()

    if score >= 1 and score <= 1000:
        return True
    else:
        return False


def main_function():
    if test_scores_service() is False:
        return -1
    return 0


if __name__ == '__main__':
    if test_scores_service():
        sys.exit(0)
    else:
        sys.exit(-1)

result = main_function()
print(result)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from MainScores import score_server
# import time
#
# url = "http://127.0.0.1:5000"
#
# def test_scores_service():
#     service = Service("C:\\Users\ortal\.cache\selenium\chromedriver\win32\108.0.5359.71\chromedriver.exe")
#     service.start()
#     driver = webdriver.Chrome(service=service)
#     driver.get(url)
#     score = int(driver.find_element("id", "score").text)
#     # driver.quit()
#
#     if score >= 1 and score <= 1000:
#         return True
#     else:
#         return False
#
# test_scores_service()







# from selenium import webdriver
# from MainScores import score_server
# import time
#
#
# url = "http://127.0.0.1:5000"
#
# def test_scores_service():
#     driver = webdriver.Chrome(executable_path = "C:\\Users\ortal\.cache\selenium\chromedriver\win32\108.0.5359.71\chromedriver.exe")
#     driver.get(url)
#     score = int(driver.find_element_by_id("score").text)
#     # driver.quit()
#
#     if score >= 1 and score <= 1000:
#         return True
#     else:
#         return False
#
# test_scores_service()