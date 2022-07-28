# 105-109學年度全台灣大專院校休學率統計
## 一、專案描述

【專案簡述】

本專案可快速得知105-109學年度全台灣各大專院校的休學率統計，以及繪製出師大與其他國立大學各年度休學率趨勢折線圖。本專案資料來源來自大專校院校務資訊公開平台的「學13-2.於學年底處於休學狀態之人數-以「校(含學制班別)」統計」之資料。而專案所使用的IDE為PyCharm Community Edition2021.2的版本，它目前是Python開發主流選擇之一，符合本專案的開發需求。

【資料分析】

本專案採用Python函式庫中的Pandas進行資料分析。首先透過Pandas進行Excel檔的解析，變成DataFrame物件。接著進行此資料庫的資料檢查，確保沒有遺漏值的問題。最後，透過groupby與休學率公式等函式，彙整出105-109學年度全台各大專院校的休學率統計，並可以匯出成Excel檔儲存。

【資料視覺化】

本專案採用Plotly Express進行資料視覺化。絕大部分的處理都與上述休學率資料分析雷同，但為了有效比較師大與幾間知名國立大學的休學率趨勢，有篩選出如師大、台大、成大、清大、陽明大與政大這幾間大學。並透過Plotly Express進行折線圖的繪製，快速呈現師大與各國立大學的休學率趨勢消長。

## 二、執行結果

此章節將透過截圖來呈現本專案各程式碼的執行結果，展現本專案資料分析與資料視覺化的成果。

**(一) 查詢休學資料庫的整體描述**
1. 執行下列程式碼

![Imgur](https://i.imgur.com/kbCnXB6.png)

2. 可以知道此資料庫的整體資料特徵

![Imgur](https://i.imgur.com/7pBVyrC.png)
![Imgur](https://i.imgur.com/p84twZj.png)

**(二) 查詢休學資料庫各個欄位的遺漏值數量**
1. 執行下列程式碼

![Imgur](https://i.imgur.com/BuNDXol.png)

2. 執行結果可以發現此資料庫各欄位並無遺漏值

![Imgur](https://i.imgur.com/qs6rvRr.png)

**(三) 計算全台灣大專院校105-109年度的休學率，並以DataFrame物件輸出**
1. 執行下列程式碼

![Imgur](https://i.imgur.com/0K9dyMJ.png)

2. 在console顯示部分全台大專院校105-109年度的休學率資料

![Imgur](https://i.imgur.com/13xzhHd.png)

**(四) 將全台灣大專院校休學率的DataFrame，以excel檔輸出**
1. 執行下列程式碼

![Imgur](https://i.imgur.com/uohrIVB.png)

2. 如果執行成功將顯示"檔案建立成功!!!"的訊息

![Imgur](https://i.imgur.com/3tnXi9O.png)

3. 如果發生錯誤將顯示"檔案已存在或檔案建立失敗!!!"的訊息

![Imgur](https://i.imgur.com/81AjLQz.png)

**(五) 師大與其他國立大學各年度休學率趨勢比較圖**
1. 執行下列程式碼

![Imgur](https://i.imgur.com/syErezu.png)

2. 將會直接連接到網頁，並出現繪製完成的折線圖
(P.S 目前只能以PNG檔呈現，無法以網頁動態呈現深感抱歉！)

![Imgur](https://i.imgur.com/BdY085o.png)

## 三、參考資料

**1. 專書**

Matt Harrison、Theodore Petrou著，蔣佑仁、李祐穎譯，2021，《Python資料分析必備套件!Pandas資料清理、重塑、過濾、視覺化》。臺北市：旗標科技

**2. 網路資料**

[Python 散佈圖／折線圖（Scatter/Line Charts）](https://waynestalk.com/python-scatter-line-charts/)

[plotly.express.line 官方文件](https://plotly.com/python-api-reference/generated/plotly.express.line.html)

[Setting the Font, Title, Legend Entries, and Axis Titles in Python](https://plotly.com/python/figure-labels/)

## 四、版權聲明
版權所有 © 2022 codyxyz8





