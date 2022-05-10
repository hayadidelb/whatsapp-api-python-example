"""
This python 3.8 script contains two function:
    
    1. get_image
        Takes a url (string) of an image and a output file name (string) and 
        downloads the image into a folder called "images" under the desired 
        filename. It then returns the location of the saved image
        
    2. check_link
        Takes a url (string) and checks if it is child-friendly website.
        If so, returns true, otherwise false.
    
    Requirements:
        1. two libraries: "requests" and "os"
        2. block_list.txt should be placed in working directory
"""

import requests
import os

def get_image(url, outfile):
    # Creates images folder if it does not already exist
    os.makedirs(os.path.dirname("../images/"), exist_ok=True)
    
    # Saves the image in the folder
    response = requests.get(url)
    filename = "../images/" + outfile # The images folder is placed next to the working directory 
    file = open(filename, "wb")
    file.write(response.content)
    file.close()
    
    # Returns the link to the image
    return filename
    
def check_link(link):
    
    # Only take the domain of the website
    link = link.split(".")[0]
    
    # Checks if domain is in the block list
    with open("block_list.txt") as block_list:
        if link in block_list.read():
            return False
    
    # Returns False if website is bad, otherwise True
    return True

