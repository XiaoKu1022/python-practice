"""
如果要讓使用者輸入多次『抽獎項目』E.g. 49折、59折、69折 .....
那就需要使用 Python 的陣列功能了，
每當使用者新輸入一個抽獎項目時，
將將它加入進陣列中，
直到使用者輸入為空白時才停止增加項目。
"""


list = []       # 宣告 list 為 陣列

while True:     # 重複執行
    enter = input("> ")     # 將 變數 enter 設為 使用者輸入內容
    if len(enter) > 0:      # 如果 變數 enter 長度大於 0 (使用者輸入非空字串)
        list.append(enter)      # 將 變數 enter 加入 陣列 list
    else:                   # 如果 變數 enter 是空的 (使用者沒有輸入內容)
        break                   # 跳出 while 迴圈

print(list)     # 列印出結果



# 執行結果 :

#     > 1
#     > 2
#     > 3
#     > 4
#     > 5
#     >
#    ['1', '2', '3', '4', '5']
