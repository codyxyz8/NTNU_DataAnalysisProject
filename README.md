# 105-109學年度全台大專院校休學率統計
## 一、專案描述

【專案簡述】

本專案可快速得知105-109學年度全台各大專院校的休學率統計，以及繪製出師大與其他國立大學各年度休學率趨勢折線圖。本專案資料來源來自大專校院校務資訊公開平台的「學13-2.於學年底處於休學狀態之人數-以「校(含學制班別)」統計」之資料。而專案所使用的IDE為PyCharm Community Edition2021.2的版本，它目前是Python開發主流選擇之一，符合本專案的開發需求。

【資料分析】

本專案採用Python函式庫中的Pandas進行資料分析。首先透過Pandas進行Excel檔的解析，變成DataFrame物件。接著進行此資料庫的資料檢查，確保沒有遺漏值的問題。最後，透過groupby與休學率公式等函式，彙整出105-109學年度全台各大專院校的休學率統計，並可以匯出成Excel檔儲存。

【資料視覺化】

本專案採用Plotly Express進行資料視覺化。絕大部分的處理都與上述休學率資料分析雷同，但為了有效比較師大與幾間知名國立大學的休學率趨勢，有篩選出如師大、台大、成大、清大、陽明大與政大這幾間大學。並透過Plotly Express進行折線圖的繪製，快速呈現師大與各國立大學的休學率趨勢消長。

## 二、執行結果

此章節將透過截圖來呈現本專案各程式碼的執行結果，展現本專案資料分析與資料視覺化的成果。



