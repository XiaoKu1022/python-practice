"""
關於動畫，
可以做成抽了100次後才顯示結果，
"""


import random   # 引入 隨機 函式庫
import time     # 引入 time 函示庫


list = ["49折","59折","69折","79折","0元"]


for i in range(100):    # 執行 100 次
    time.sleep(i/1000)                          # 暫停設為 1000分之i，動畫會越來越慢，因為i值一直在增加
    hit = random.choice(list)
    print("\r抽獎中 ".format(i)+hit,end=" ")	# 顯示動畫

print("\r恭喜中獎 ".format(i)+hit,end=" ")   # 顯示最後的中獎結果