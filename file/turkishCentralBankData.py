import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


key="E7GPkfpvjZ" #we got key api in turkish central bank

data=pd.read_csv("https://evds2.tcmb.gov.tr/service/evds/datagroups/key={}&mode=0&type=csv".format(key))

data.drop(["CATEGORY_ID","METADATA_LINK","REV_POL_LINK_ENG",
         "APP_CHA_LINK_ENG","REV_POL_LINK","APP_CHA_LINK",
         "METADATA_LINK_ENG","DATAGROUP_NAME_ENG","DATASOURCE_ENG"], 
          axis=1,inplace=True)

#we gonna choose datagroup_code in data variables 

print(data.iloc[:][["DATAGROUP_CODE","DATAGROUP_NAME"]])



group_code="bie_abres2"# this reserve amount of turkish central bank
alt_veri = pd.read_csv("https://evds2.tcmb.gov.tr/service/evds/serieList/key={}&type=csv&code={}".format(key,group_code))


series="TP.AB.C2" #you can look series code of alt veri in variable explorer , this forex 

series_name="Altın(Milyon ABD Doları)"
startDate= "01-01-%202019"
endDate="01-12-%202319"
typee="csv"
aggregationTypes="avg"
formulas="0"
frequency = "1"
url=url= 'https://evds2.tcmb.gov.tr/service/evds/series={}&startDate={}&endDate={}&type={}&key={}&aggregationTypes={}&formulas={}&frequency={}'.format(series,startDate,endDate,typee,key,aggregationTypes,formulas,frequency)
Forex_Data = pd.read_csv(url)

print("Turkish Central Bank Forex UDS/TRY ")
Forex_Data.loc[:,"TP_AB_C2"]=Forex_Data.loc[:,"TP_AB_C2"]*1000
Forex_Data.loc[:,"TP_AB_C2"]=Forex_Data.loc[:,"TP_AB_C2"]
print(Forex_Data.loc[:,["Tarih","TP_AB_C2"]])



import matplotlib.pyplot as plt

plt.figure()
plt.plot(Forex_Data["TP_AB_C2"])
plt.xlabel("01.01.2019 - 2023 ")
plt.ylabel("usd")


