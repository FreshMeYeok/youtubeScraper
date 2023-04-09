import requests
from bs4 import BeautifulSoup

def check_video_availability(video_id):
    # Send a request to the video URL
    print(video_id)
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url)
    
    # Parse the HTML response with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    img_tags = soup.find_all("img")
    print(img_tags)
    # Check if the video is available or not
    unavailable_image = soup.find('img')#, {'src': 'https://www.youtube.com/img/desktop/unavailable/unavailable_video.png'})
    print(unavailable_image)
    
    # if "https://www.youtube.com/img/desktop/unavailable/unavailable_video.png" in soup:
    #   print("?")
    #   return False
    # else:
    #   print("123")
    #   return True
    # if unavailable_image is None:
    #     return True
    # else:
    #     return False
    return soup
# Read the URLs from the text file
input_filename = "input_urls.txt"
available_filename = "available_urls2.txt"
unavailable_filename = "unavailable_urls.txt"
with open(input_filename, "r") as f_in, \
     open(available_filename, "w") as f_available, \
     open(unavailable_filename, "w") as f_unavailable:
    
    urls = f_in.readlines()

    # Check each URL and write the results to the output files
    for url in urls:
        video_id = url.strip().split("=")[-1]
        available = check_video_availability(video_id)
        if not available:
            f_available.write(f"{url.strip()}\n")
            # f_available.write(str(available))
        else:
            f_unavailable.write(f"{url.strip()}\n")
            # f_available.write(str(available))
