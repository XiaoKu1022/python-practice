"""
程式流程：
    1. 引入函式庫、初始化陣列
    2. 讓使用者輸入抽獎項目
    3. 讓使用者輸入抽獎模式（可重複、不重複）
    4. 開始抽獎
"""


import random   # 引入 隨機 函式庫
import os       # 引入 os 函式庫
import time     # 引入 time 函示庫


list = []       # 宣告 list 為 陣列


while True:     # 重複執行
    enter = input("請輸入獎項 > ")    # 將 變數 enter 設為 使用者輸入內容
    if len(enter) > 0:              # 如果 變數 enter 長度大於 0
        list.append(enter)                  # 將 變數 enter 加入 陣列 list

    else:       # 如果 變數 enter 是空的 (使用者沒有輸入內容)
        break                       # 跳出 while 迴圈


mode = int(input(
    "請選擇模式： \n \t1 : 可重複抽 \n \t2 : 不可重複抽\n 請輸入 [ 1 / 2 ] > ")) # 選擇模式
              # \n <- 為換行 ； \t <- 為 Tab 縮排


if mode == 1: # 可重複抽
    while True:    
        for i in range(len(list)*10):    # 動畫執行次數 = len(list)*10
            time.sleep(i/(len(list)*100))# 暫停設為 i / (len(list)*50)
            hit = random.choice(list)
            print("\r抽獎中 ".format(i)+hit,end=" ")    # 顯示動畫

        print("\r恭喜中獎 ".format(i)+hit,end="\n")  # 顯示中獎
        os.system("pause")              # 暫停，按下任意鍵繼續抽


elif mode == 2: # 不重複抽
    while len(list) > 0:    # 如果 陣列 list 長度大於 0 
        for i in range(len(list)*10):    # 動畫執行次數 = len(list)*10
            time.sleep(i/(len(list)*100))# 暫停設為 i / (len(list)*50)
            hit = random.choice(list)
            print("\r抽獎中 ".format(i)+hit,end=" ")   # 顯示動畫

        list.remove(hit)                # 從 陣列 list 中，移除與 變數 hit 相同 的 內容
        print("\r恭喜中獎 ".format(i)+hit,end="\n")   # 顯示中獎
        os.system("pause")              # 暫停，按下任意鍵繼續抽


else:
    print("Error: Mode Set Number")     # 錯誤，模式選擇不正確


# 執行結果：

#   請輸入獎項 > 49
#   請輸入獎項 > 59
#   請輸入獎項 > 69
#   請輸入獎項 > 0元
#   請輸入獎項 > 
#   請選擇模式： 
#            1 : 可重複抽  
#            2 : 不可重複抽
#   請輸入 [ 1 / 2 ] > 2 
#
#   恭喜中獎 0元
#   請按任意鍵繼續 . . . 
#
#   恭喜中獎 69
#   請按任意鍵繼續 . . . 
#
#   恭喜中獎 59
#   請按任意鍵繼續 . . . 
#
#   恭喜中獎 49
#   請按任意鍵繼續 . . . 