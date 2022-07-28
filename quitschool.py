'''
    從大專院校平台下載於學年底處於休學狀態之人數-以「校(含學制班別)」統計之資料表，
    使用pandas進行資料讀取、資料分析與視覺化圖表
    (P.S 由於無法用import的方式傳遞DataFrame物件，故在同一介面操作資料下載與資料分析)
'''


import pandas as pd
import plotly.express as px


# 創建QuitSchoolSource的類別，專門存放解析資料的方法
# ------------讀取資料開始-----------------#
class QuitSchoolSource:

    def __init__(self):
        # 休學資料庫的檔案名稱，excel檔已重新命名為英文方便辨識
        self.source = "QuitSchool_DataBase.xlsx"

    # 讀取檔案的函式
    def readfile(self):
        # 設條件確認檔案名稱無誤
        import os
        # 除錯與例外
        if os.path.isfile(self.source):
            # 如果正確就讀取檔案，錯誤則顯示訊息
            quitschool = pd.read_excel(self.source)
            return quitschool
        else:
            print("檔案名稱有誤或不存在!!!")

#-------------讀取資料結束-----------------#

# 創建QuitSchoolAnaysis的類別，專門存放資料分析的方法
#-------------分析資料開始-----------------#
class QuitSchoolAnaysis:

    def __init__(self):
        # 建立QuitSchoolSource的物件，並取出資料
        self.quitschoolsource = QuitSchoolSource()
        self.quitschooldata = self.quitschoolsource.readfile()

#-------------資料檢查開始-----------------#
    # 此函式進行資料的整體描述
    def info(self):
        info = self.quitschooldata.info()
        # 回傳休學資料的整體資料樣貌
        return info
    # 此函式進行資料的遺漏值統計
    def null_staitsitcs(self):
        null = self.quitschooldata.isna().sum()
        # 回傳各欄位null值統計，根據回傳結果並沒有遺漏值
        return null

#--------------資料檢查結束--------------------#

#--------------休學率統計開始------------------#

    # 存放休學率公式的函式(輸出資料轉成字串百分比)
    def suspension_rate_string(self, df):
        # 休學人數總和除於在學學生數的總和
        suspension_rate = (df["於學年底處於休學狀態之人數-總計"].sum()/df["在學學生數"].sum())
        # 新增回傳series的欄位名稱
        rate_column = {"休學率(百分比%)": suspension_rate}
        # 轉換成Series物件，並增加百分比的單位，取到小數第一位並四捨五入
        data = pd.Series(rate_column).map(lambda x:format(x,".1%"))
        return data

    # 存放休學率公式的函式(輸出資料以浮點數呈現)
    def suspension_rate_number(self, df):
        # 休學人數總和除於在學學生數的總和，取到小數第一位並四捨五入
        suspension_rate = ((df["於學年底處於休學狀態之人數-總計"].sum()/df["在學學生數"].sum())*100).round(1)
        # 新增回傳series的欄位名稱
        rate_column = {"休學率(百分比%)": suspension_rate}
        # 轉換成Series物件
        data = pd.Series(rate_column)
        return data


    # 計算所有大專院校休學率的聚合函式
    def college_dropout_rate(self):
        # 使用groupby將學校名稱、學年度為分組欄位，並透過suspension_rate函式進行休學率的計算
        # 回傳結果是各個學校每一個學年度的全校休學率
        # 排序以學校名稱第一個字筆畫多寡來排列
        dropout_rate = (
            self.quitschooldata
            .groupby(["學校名稱","學年度"])
            .apply(self.suspension_rate_string) #在此使用字串型態的休學率函式，以方便閱讀
            .reset_index() # 將學校名稱、學年度欄位扁平化，以整齊版面
        )

        return dropout_rate

    # 輸出excel檔的函式
    def excel(self):
        import os
        # 以college變數儲存已計算完所有大專院校休學率的DataFrame物件
        college = self.college_dropout_rate()
        # 檢查excel檔是否有建立，沒有就建立
        # 如果檔案已存在或未建立成功，則顯示錯誤訊息
        if not os.path.isfile("college_dropout_rate.xlsx"):
            college.to_excel("college_dropout_rate.xlsx")
            print("檔案建立成功!!!")
        else:
            print("檔案已存在或檔案建立失敗")

#----------------休學率統計結束-------------------#

#----------------視覺化圖表開始-------------------#

    # 本專案使用Python函式庫中的Plotly Express進行繪圖

    def visualization(self):
        # 篩選出師大以及台清陽交成政作為比較對象
        university = self.quitschooldata["學校名稱"].isin(["國立臺灣師範大學","國立臺灣大學","國立清華大學","國立陽明交通大學","國立成功大學","國立政治大學"])
        # 同樣以先前升學率聚合函式進行groupby，並存放在visual_data
        visual_data = (
            self.quitschooldata[university]
            .groupby(["學校名稱","學年度"])
            .apply(self.suspension_rate_number) # 在此使用以浮點數呈現的休學率函式，以利進行統計繪圖
            .reset_index()
            )
        # 使用Plotly Express繪製折線圖
        fig = px.line(data_frame=visual_data,
                      x="學年度",
                      y="休學率(百分比%)",
                      title="師大與其他國立大學各年度休學率趨勢比較圖",
                      color="學校名稱",
                      range_y=[0,20]
                      )
        # 調整x軸使學年度以整數呈現(原先預設以浮點數出現)
        # 標題置中、增加標題大小、增加文字大小
        fig.update_layout(xaxis=dict(tickmode="array",tickvals=[105,106,107,108,109]),
                          title_x=0.5,
                          title_font_size=22,
                          font_size=16
                          )
        fig.show()
        # 輸出html檔
        fig.write_html("linecharts.html")


#----------------視覺化圖表結束------------------------#

#----------------分析資料結束-------------------------#

#----------------主流程開始--------------------------#


# 建立QuitSchoolAnaysis的物件，並存放在quitschool_main的變數中
quitschool_main = QuitSchoolAnaysis()

'''
    建議執行以下任一程式碼需要先註解掉其他區塊的程式碼，方便查看執行結果。
'''


# # 查詢休學資料庫的整體描述
# quitschool_main.info()

# # 查詢休學資料庫各個欄位的遺漏值數量
# null = quitschool_main.null_staitsitcs()
# print(null)

# # 計算所有全台大專院校105-109年度的休學率，並以DataFrame物件輸出
# dropout_rate = quitschool_main.college_dropout_rate()
# print(dropout_rate)

# # 將上述的全台大專院校休學率DataFrame，以excel檔輸出
# # 建立成功或失敗會在console顯示訊息
# excel = quitschool_main.excel()

# # 建立師大與其他國立大學各年度休學率趨勢比較的折線圖
# quitschool_main.visualization()

#-----------------主流程結束---------------------#

