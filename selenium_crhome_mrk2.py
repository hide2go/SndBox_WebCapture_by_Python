from selenium import webdriver
from PIL import Image
from enum import Enum
import chromedriver_binary
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

v_stock_code="8604"
s_suffix_chart_type = ''
s_file_name = ''
s_mode = 1

class Chart_Type(Enum):
    daily = 1
    weekly = 2
    min_5 = 3

class execute_mode(Enum):
    eod = 1
    zaraba = 2

def s_choose_chart_type(in_chart_type):
    global s_suffix_chart_type
    global s_file_name
    global v_stock_code
    print('Execute s_choose_chart_type')
    if in_chart_type == Chart_Type.daily:
        #日足
        print('s_choose_chart_type == 1')
        driver.find_element_by_id('kc_ashi_1').click()
        driver.find_element_by_id('kc_tech1_4').click()
        driver.find_element_by_id('kc_tech2_11').click()
        s_suffix_chart_type = "_DLY"
    elif in_chart_type == Chart_Type.weekly:
        #週足
        driver.find_element_by_id('kc_ashi_2').click()
        driver.find_element_by_id('kc_tech1_4').click()
        driver.find_element_by_id('kc_tech2_11').click()
        s_suffix_chart_type = '_WKLY'
    elif in_chart_type == Chart_Type.min_5:
        #5分足
        driver.find_element_by_id('kc_ashi_5').click()
        driver.find_element_by_id('kc_tech1_4').click()
        driver.find_element_by_id('kc_tech2_11').click()
        s_suffix_chart_type = '_5MIN'

    s_file_name = v_stock_code + "_image" + s_suffix_chart_type + '.png'

# ブラウザーを起動
chrome_options = Options()
chrome_options.add_argument('-headless')
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("start-maximised")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://kabutan.jp/stock/chart?code='+ v_stock_code);

element = driver.find_element_by_xpath("//*[@id='kc_area']");
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()

print('s_mode = ' + str(s_mode))
print('execute_mode.eod = ' + str(execute_mode.eod))
if s_mode == execute_mode.eod:
    s_choose_chart_type(Chart_Type.daily)
    location = element.location
    size = element.size
    print('s_file_name = ' + s_file_name)

    driver.save_screenshot(s_file_name);

    x = location['x'];
    y = location['y'];
    width = location['x']+size['width'];
    height = location['y']+size['height'];

    im = Image.open(s_file_name);
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(s_file_name)

    s_choose_chart_type(Chart_Type.min_5)
    location = element.location
    size = element.size
    print('s_file_name = ' + s_file_name)

    driver.save_screenshot(s_file_name);

    x = location['x'];
    y = location['y'];
    width = location['x'] + size['width'];
    height = location['y'] + size['height'];

    im = Image.open(s_file_name);
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(s_file_name)

    s_choose_chart_type(Chart_Type.weekly)
    location = element.location
    size = element.size
    print('s_file_name = ' + s_file_name)

    driver.save_screenshot(s_file_name);

    x = location['x'];
    y = location['y'];
    width = location['x'] + size['width'];
    height = location['y'] + size['height'];

    im = Image.open(s_file_name);
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(s_file_name)
elif s_mode == execute_mode.zaraba:
    s_choose_chart_type(Chart_Type.min_5)
    location = element.location
    size = element.size
    print('s_file_name = ' + s_file_name)

    driver.save_screenshot(s_file_name);

    x = location['x'];
    y = location['y'];
    width = location['x'] + size['width'];
    height = location['y'] + size['height'];

    im = Image.open(s_file_name);
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(s_file_name)



# ブラウザーを終了
driver.quit();


