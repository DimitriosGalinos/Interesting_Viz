import pandas as pd
import numpy as np

wslat = [56.766667, 55.45, 55.85, 55.683333, 55.683333, 55.283333, 55.3, 55.3,
         55.833333]
wslong = [8.316667, 8.4, 10.6, 12.533333, 12.533333, 14.783333, 14.783333,
          14.783333, 10.616667]
degreez = [-4.9, -3.8, -4.1, -5.2, -6.6, -3.8, -4.9, -8.4, -6.4]

df3 = pd.DataFrame({'Weather Station Long': wslong, 
                    'Weather Station Lat': wslat, 
                    'Max temperature ':degreez
                    })

data1 = pd.read_csv('clean_TX_STAID000106.txt', sep=",")
data1.columns = ["a", "date", "temperature", "etc."]
del data1["a"]
del data1["etc."]
lat1=[56.766667]*40
long1=[8.316667]*40
data1["temperature"]=0.1*data1["temperature"]
#dates = [str(x) for x in data1["date"].to_list()]
datez = data1["date"].to_list()
yearz = [int(x / 10000) for x in datez]
maxi = 0
prev_year = 1979
yearly_max = []
year = []
for xx in range(len(yearz)):
    if prev_year == yearz[xx]:
        if maxi < data1.at[xx, "temperature"]:
            maxi = data1.at[xx, "temperature"]
    else:
        yearly_max.append(round(maxi, 1))
        year.append(prev_year)
        prev_year = yearz[xx]
        maxi = 0
datas1 = pd.DataFrame({"Long":long1, 
                      "Lat":lat1,
                      "Year":year,
                      "Maximum Temperature":yearly_max
                      })

data2 = pd.read_csv('clean_TX_STAID000107.txt', sep=",")
data2.columns = ["a", "date", "temperature", "etc."]
del data2["a"]
del data2["etc."]
lat2=[55.45]*40
long2=[8.4]*40
data2["temperature"]=0.1*data2["temperature"]
maxi = 0
prev_year = 1979
yearly_max = []
year = []
for xx in range(len(yearz)):
    if prev_year == yearz[xx]:
        if maxi < data2.at[xx, "temperature"]:
            maxi = data2.at[xx, "temperature"]
    else:
        yearly_max.append(round(maxi, 1))
        year.append(prev_year)
        prev_year = yearz[xx]
        maxi = 0
datas2 = pd.DataFrame({"Long":long2, 
                      "Lat":lat2,
                      "Year":year,
                      "Maximum Temperature":yearly_max
                      })

data3 = pd.read_csv('clean_TX_STAID000109.txt', sep=",")
data3.columns = ["a", "date", "temperature", "etc."]
del data3["a"]
del data3["etc."]
lat3=[55.85]*40
long3=[10.6]*40
data3["temperature"]=0.1*data3["temperature"]
maxi = 0
prev_year = 1979
yearly_max = []
year = []
for xx in range(len(yearz)):
    if prev_year == yearz[xx]:
        if maxi < data3.at[xx, "temperature"]:
            maxi = data3.at[xx, "temperature"]
    else:
        yearly_max.append(round(maxi, 1))
        year.append(prev_year)
        prev_year = yearz[xx]
        maxi = 0
datas3 = pd.DataFrame({"Long":long3, 
                      "Lat":lat3,
                      "Year":year,
                      "Maximum Temperature":yearly_max
                      })

data4 = pd.read_csv('clean_TX_STAID000113.txt', sep=",")
data4.columns = ["a", "date", "temperature", "etc."]
del data4["a"]
del data4["etc."]
lat4=[55.683333]*40
long4=[12.533333]*40
data4["temperature"]=0.1*data4["temperature"]
maxi = 0
prev_year = 1979
yearly_max = []
year = []
for xx in range(len(yearz)):
    if prev_year == yearz[xx]:
        if maxi < data4.at[xx, "temperature"]:
            maxi = data4.at[xx, "temperature"]
    else:
        yearly_max.append(round(maxi, 1))
        year.append(prev_year)
        prev_year = yearz[xx]
        maxi = 0
datas4 = pd.DataFrame({"Long":long4, 
                      "Lat":lat4,
                      "Year":year,
                      "Maximum Temperature":yearly_max
                      })

data5 = pd.read_csv('clean_TX_STAID000116.txt', sep=",")
data5.columns = ["a", "date", "temperature", "etc."]
del data5["a"]
del data5["etc."]
lat5=[55.683333]*40
long5=[12.533333]*40
data5["temperature"]=0.1*data5["temperature"]
maxi = 0
prev_year = 1979
yearly_max = []
year = []
for xx in range(len(yearz)):
    if prev_year == yearz[xx]:
        if maxi < data5.at[xx, "temperature"]:
            maxi = data5.at[xx, "temperature"]
    else:
        yearly_max.append(round(maxi, 1))
        year.append(prev_year)
        prev_year = yearz[xx]
        maxi = 0
datas5 = pd.DataFrame({"Long":long5, 
                      "Lat":lat5,
                      "Year":year,
                      "Maximum Temperature":yearly_max
                      })

data6 = pd.read_csv('clean_TX_STAID000117.txt', sep=",")
data6.columns = ["a", "date", "temperature", "etc."]
del data6["a"]
del data6["etc."]
lat6=[55.283333]*40
long6=[14.783333]*40
data6["temperature"]=0.1*data6["temperature"]
maxi = 0
prev_year = 1979
yearly_max = []
year = []
for xx in range(len(yearz)):
    if prev_year == yearz[xx]:
        if maxi < data6.at[xx, "temperature"]:
            maxi = data6.at[xx, "temperature"]
    else:
        yearly_max.append(round(maxi, 1))
        year.append(prev_year)
        prev_year = yearz[xx]
        maxi = 0
datas6 = pd.DataFrame({"Long":long6, 
                      "Lat":lat6,
                      "Year":year,
                      "Maximum Temperature":yearly_max
                      })

data7 = pd.read_csv('clean_TX_STAID000118.txt', sep=",")
data7.columns = ["a", "date", "temperature", "etc."]
del data7["a"]
del data7["etc."]
lat7=[55.3]*40
long7=[14.783333]*40
data7["temperature"]=0.1*data7["temperature"]
maxi = 0
prev_year = 1979
yearly_max = []
year = []
for xx in range(len(yearz)):
    if prev_year == yearz[xx]:
        if maxi < data7.at[xx, "temperature"]:
            maxi = data7.at[xx, "temperature"]
    else:
        yearly_max.append(round(maxi, 1))
        year.append(prev_year)
        prev_year = yearz[xx]
        maxi = 0
datas7 = pd.DataFrame({"Long":long7, 
                      "Lat":lat7,
                      "Year":year,
                      "Maximum Temperature":yearly_max
                      })


data8 = pd.read_csv('clean_TX_STAID000119.txt', sep=",")
data8.columns = ["a", "date", "temperature", "etc."]
del data8["a"]
del data8["etc."]
lat8=[55.3]*40
long8=[14.783333]*40
data8["temperature"]=0.1*data8["temperature"]
maxi = 0
prev_year = 1979
yearly_max = []
year = []
for xx in range(len(yearz)):
    if prev_year == yearz[xx]:
        if maxi < data8.at[xx, "temperature"]:
            maxi = data8.at[xx, "temperature"]
    else:
        yearly_max.append(round(maxi, 1))
        year.append(prev_year)
        prev_year = yearz[xx]
        maxi = 0
datas8 = pd.DataFrame({"Long":long8, 
                      "Lat":lat8,
                      "Year":year,
                      "Maximum Temperature":yearly_max
                      })



data9 = pd.read_csv('clean_TX_STAID000305.txt', sep=",")
data9.columns = ["a", "date", "temperature", "etc."]
del data9["a"]
del data9["etc."]
lat9=[55.833333]*40
long9=[10.616667]*40
data9["temperature"]=0.1*data9["temperature"]
maxi = 0
prev_year = 1979
yearly_max = []
year = []
for xx in range(len(yearz)):
    if prev_year == yearz[xx]:
        if maxi < data9.at[xx, "temperature"]:
            maxi = data9.at[xx, "temperature"]
    else:
        yearly_max.append(round(maxi, 1))
        year.append(prev_year)
        prev_year = yearz[xx]
        maxi = 0
datas9 = pd.DataFrame({"Long":long9, 
                      "Lat":lat9,
                      "Year":year,
                      "Maximum Temperature":yearly_max
                      })


final_data = pd.concat([datas1, datas2, datas3, datas4, datas5, datas6, 
                        datas7, datas8, datas9])

zozo=final_data.loc[final_data['Year'] == 1979]