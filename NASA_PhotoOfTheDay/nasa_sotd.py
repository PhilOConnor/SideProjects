"""
Scrape NASA's Astronomy Shot of the Day and set it as the wallpaper

"""

import ctypes
import re
import bs4
import requests

def get_image():
    result = requests.get("https://apod.nasa.gov/apod/astropix.html")
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    sotd = soup.select('a')[1].get('href')
    pattern = '.jpg$'
    # Pick out the second link
    try:
        # Check that the link is to a jpg
        re.search(pattern, sotd).group()
        image_link = '/'.join(['https://apod.nasa.gov/apod', sotd])
        image = requests.get(image_link)
        #image_link.content

    except:
        # if no jpg found, this image will be downloaded
        image_link = '''https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/thumbnails/image/sts111-306-012_orig.jpg'''
        image = requests.get(image_link)

    image_save = open('C:\\Users\\phil\\Pictures\\DesktopBackground\\screensaver.jpg', 'wb')
    image_save.write(image.content)
    image_save.close()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:\\Users\\phil\\Pictures\\DesktopBackground\\screensaver.jpg', 0)

get_image()
