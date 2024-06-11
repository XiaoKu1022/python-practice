"""
還是一個陣列list，
內容依舊還是抽獎項目，
抽獎設定為：可重複抽
(也意味著這支程式沒有結束條件，因為永遠都還可以抽下一個)
"""


import random   # 引入 隨機 函式庫
import os       # 引入 os 函式庫


list = ["49折","59折","69折","79折","0元"]

while True:    # 永遠執行
    hit = random.choice(list)                   # 陣列 list 中 取出一項，並存入 變數 hit 中
    print(f"\n中 {hit}")                        # 列印出 hit
    os.system("pause")							# 暫停，按下任意鍵繼續抽
    

# 執行結果 :

#    中 79折
#    請按任意鍵繼續 . . . 
#
#    中 0元
#    請按任意鍵繼續 . . . 
#
#        ..... 一直抽, 一直, never stop, forever.....