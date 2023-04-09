import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
from time import sleep


def check_video(i, url):
    # Replace the URL with the webpage you want to check
    # url = "https://www.youtube.com/watch?v=EY8x-fyQkbk"
    # url = "https://www.youtube.com/watch?v=f482qwPz7ns&ab_channel=CarCrashesTime"

    # Create a new instance of the Chrome driver

    driver = webdriver.Chrome()
    # Navigate to the URL
    driver.get(url)

    # Find all the img tags on the webpage
    # img_tags = driver.find_element(By.TAG_NAME, "img")
    imgResults = driver.find_elements(By.XPATH,"//img[contains(@src,'https://www.youtube.com/img/desktop/unavailable/unavailable_video.png')]")
    

    # sleep(2)
    print(imgResults)
    driver.quit()
    # Check if there are any img tags
    if imgResults:
        print(str(i)+"불가능")
        return i+1, False
    else:
        print(str(i)+"사용 가능")
        return i+1, True

# Close the browser window
input_filename = "input_urls.txt"
available_filename = "available_urls.txt"
unavailable_filename = "unavailable_urls.txt"
with open(input_filename, "r") as f_in, \
     open(available_filename, "w") as f_available, \
     open(unavailable_filename, "w") as f_unavailable:
    
    urls = f_in.readlines()
    i = 1
    # Check each URL and write the results to the output files
    for url in urls:
        # video_id = url.strip().split("=")[-1]
        i, available = check_video(i, url)
        if available:
            f_available.write(f"{url.strip()}\n")
            # f_available.write(str(available))
        else:
            f_unavailable.write(f"{url.strip()}\n")
            # f_available.write(str(available))
            

