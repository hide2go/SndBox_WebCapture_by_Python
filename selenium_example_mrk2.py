from selenium import webdriver
from PIL import Image

driver = webdriver.Firefox(executable_path=r"D:\Apps\geckodriver.exe");
driver.get('https://www.google.co.in');

element = driver.find_element_by_xpath("//div[@id='lga']");

location = element.location;
size = element.size;

driver.save_screenshot("image.png");

x = location['x'];
y = location['y'];
width = location['x']+size['width'];
height = location['y']+size['height'];

im = Image.open('image.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('image.png')