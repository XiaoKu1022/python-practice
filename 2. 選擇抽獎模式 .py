"""
將『允許重複抽』和『不重複抽』視為：
  『１模式』    和『２模式』
"""


mode = int(input(
	"請選擇模式： \n \t1 : 可重複抽 \n \t2 : 不可重複抽\n 請輸入 [ 1 / 2 ] > "))
                # \n <- 為換行 ； \t <- 為 Tab 縮排

print(f"抽獎模式為 {mode}")


# 執行結果 :

#    請選擇模式： 
#            1 : 可重複抽  
#            2 : 不可重複抽
#    請輸入 [ 1 / 2 ] > 1 
#    抽獎模式為 1