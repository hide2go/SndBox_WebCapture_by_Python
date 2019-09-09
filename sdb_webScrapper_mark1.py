import time
import re
from selenium import webdriver

#URLのドメイン抽出パターン作成
pat = r"https?://(www.)?([\w-]+).[\w.]"

# コマンドラインよりURL取得。「,」区切りで複数入力可能
inp = input("URLを入力\n")

# 「,」でリストへ分割。さらに左右の空白消去
URLS = list(map(str.strip,(inp.split(","))))

# プラウザ起動（Chrome）
driver = webdriver.Chrome()

# リストからURLをひとつづつ処理
for url in URLS :
    # ドメインの一部をファイル名として設定
    site_name = re.search(pat,url)
    file_name = "{0}.png".format(site_name.group(2))
    # URLを開く
    driver.get(url)
    # ウィンドウサイズとズームを設定
    driver.set_window_size(1250, 1036)
    driver.execute_script("document.body.style.zoom='90%'")
    # 読み込み待機時間
    time.sleep(2)
    # imagesフォルダにスクリーンショットを保存
    driver.save_screenshot("./images/" + file_name)

# プラウザを閉じる
driver.quit()