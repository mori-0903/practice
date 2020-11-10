#!/usr/bin/env python
# coding: utf-8

# # これは和田川の流域平均雨量を求めるプログラムです

# In[27]:


import pandas as pd
# import codecs
from datetime import time
import os
import matplotlib.pyplot as plt
import numpy as np
# % matplotlib inline


# ### ↓は和田川の総面積、広神ダム流域面積、和田川下流域の割合

# In[28]:


wadaka_a =3707792.853
hiro_a   =43874613.77
all_a = wadaka_a + hiro_a
hiro_w = hiro_a / all_a
wadaka_w = wadaka_a / all_a

print("wada_karyu = ",wadaka_w)
print("hirokami   = ",hiro_w)


# ### <div style="text-align: center;">ティーセンパターン</div>
# | 小出 | 守門 | 堀之内 | 
# | :--: | :--: | :----: | 
# |〇   | 〇   | 〇     | 

# In[29]:


#広神ダム流域
p_h_su = 0.818481574
p_h_ko = 0
p_h_ho = 0.181518428

#和田川下流域
p_k_su = 0.516496405
p_k_ko = 0.186083658
p_k_ho = 0.297422381


# ### <div style="text-align: center;">ティーセンパターン1</div>
# | 小出 | 守門 | 堀之内 | 
# | :--: | :--: | :----: | 
# |欠測   | 〇   | 〇     | 

# In[30]:


#広神ダム流域
p_h_su1 = 0.818481573
p_h_ho1 = 0.181518427

#和田川下流域
p_k_su1 = 0.186609912
p_k_ho1 = 0.813390088


# ### <div style="text-align: center;">ティーセンパターン2</div>
# | 小出 | 守門 | 堀之内 | 
# | :--: | :--: | :----: | 
# |〇|欠測   | 〇     | 

# In[31]:


#広神ダム流域
p_h_ko2 = 0.020695811
p_h_ho2 = 0.979304188

#和田川下流域
p_k_ko2 = 0.363465371
p_k_ho2 = 0.636534631


# ### <div style="text-align: center;">ティーセンパターン3</div>
# | 小出 | 守門 | 堀之内 | 
# | :--: | :--: | :----: | 
# |〇| 〇  | 欠測    | 

# In[32]:


#広神ダム流域
p_h_su3 = 0.064715194
p_h_ko3 = 0.935284805

#和田川下流域
p_k_su3 = 0.802685233
p_k_ko3 = 0.197314806


# In[33]:


# upath = '和田川_流域平均雨量/'
# os.makedirs(upath, exist_ok=True) #フォルダ作成
# pd.options.display.float_format = '{:.1f}'.format
    
path_koide =r"Z:\環境防災部\R02年度\60-0374_一級河川和田川洪水浸水想定区域図作成業務委託\07_基礎データ\2_雨量データ\小出（気）\小出_rain_data\all.csv"
path_sumon = r"Z:\環境防災部\R02年度\60-0374_一級河川和田川洪水浸水想定区域図作成業務委託\07_基礎データ\2_雨量データ\守門（気）（入広瀬）\守門_rain_data\all.csv"
path_horinouch = r"Z:\環境防災部\R02年度\60-0374_一級河川和田川洪水浸水想定区域図作成業務委託\07_基礎データ\2_雨量データ\堀之内\all.csv"


df_koide = pd.read_csv(path_koide
                      ,encoding='shift-jis'
                      ,index_col=0
                      ,parse_dates=[0]
                      )
df_sumon = pd.read_csv(path_sumon
                      ,encoding='shift-jis'
                      ,parse_dates=[0]
                      ,index_col=0
                      )
df_horinouch = pd.read_csv(path_horinouch
                          ,encoding='shift-jis'
                          ,parse_dates=[0]
                          ,index_col=0
                          )

df_horinouch.rename(columns = {'降水量(mm)':'堀之内'},inplace=True)
df_horinouch
df_all = pd.DataFrame(df_horinouch['堀之内'])
# df_all = pd.DataFrame(df_koide['小出'])
df_all["守門"]   = df_sumon["守門"]
df_all["小出"] = df_koide["小出"]
# df_all["堀之内"] = df_horinouch["堀之内"]
# pd.DataFrame(df_koide['48時間雨量'].loc[time(9,0)])
df_all["広神ダム流域"]=np.nan
df_all["和田川下流域"]=np.nan
df_all["流域平均雨量"]=np.nan


# In[34]:


len(df_horinouch)


# In[37]:


len(df_koide)


# In[38]:


len(df_all)


# In[39]:


hantei=df_all.isnull()
hantei


# In[ ]:


for i in range(len(df_all)):
    if hantei["小出"][i] == True and hantei["守門"][i] == False and hantei["堀之内"][i] == False: # パターン1
        df_all["広神ダム流域"][i] = df_all["守門"][i]*p_h_su1 + df_all["堀之内"][i]*p_h_ho1
        df_all["和田川下流域"][i] = df_all["守門"][i]*p_k_su1 + df_all["堀之内"][i]*p_k_ho1
        df_all["流域平均雨量"][i] = df_all["広神ダム流域"][i]*hiro_w + df_all["和田川下流域"][i]*wadaka_w
#         print(df_all.index[i],"caution!小出なし")
    elif hantei["守門"][i] == True and hantei["堀之内"][i] == False and hantei["小出"][i] == False: # パターン2
        df_all["広神ダム流域"][i] = df_all["堀之内"][i]*p_h_ho2 + df_all["小出"][i]*p_h_ko2
        df_all["和田川下流域"][i] = df_all["堀之内"][i]*p_k_ho2 + df_all["小出"][i]*p_k_ko2
        df_all["流域平均雨量"][i] = df_all["広神ダム流域"][i]*hiro_w + df_all["和田川下流域"][i]*wadaka_w
#         print(df_all.index[i],"caution!守門なし")
    elif hantei["堀之内"][i] == True and hantei["守門"][i] == False and hantei["小出"][i] == False: # パターン3
        df_all["広神ダム流域"][i] = df_all["守門"][i]*p_h_su3 + df_all["小出"][i]*p_h_ko3
        df_all["和田川下流域"][i] = df_all["守門"][i]*p_k_su3 + df_all["小出"][i]*p_k_ko3
        df_all["流域平均雨量"][i] = df_all["広神ダム流域"][i]*hiro_w + df_all["和田川下流域"][i]*wadaka_w
#         print(df_all.index[i],"caution!堀之内なし")       
    elif hantei["堀之内"][i] == False and hantei["守門"][i] == False and hantei["小出"][i] == False: # パターンall
        df_all["広神ダム流域"][i] = df_all["守門"][i]*p_h_su + df_all["小出"][i]*p_h_ko + df_all["堀之内"][i]*p_h_ho
        df_all["和田川下流域"][i] = df_all["守門"][i]*p_k_su + df_all["小出"][i]*p_k_ko + df_all["堀之内"][i]*p_k_ho
        df_all["流域平均雨量"][i] = df_all["広神ダム流域"][i]*hiro_w + df_all["和田川下流域"][i]*wadaka_w
      
    elif hantei["守門"][i] == True and hantei["小出"][i] == True and hantei["堀之内"][i] == False: #堀之内のみ
        df_all["広神ダム流域"][i] = df_all["堀之内"][i]
        df_all["和田川下流域"][i] = df_all["堀之内"][i]
        df_all["流域平均雨量"][i] = df_all["堀之内"][i]
        print(df_all.index[i],"caution!堀之内のみ")
    elif hantei["堀之内"][i] == True and hantei["小出"][i] == True and hantei["守門"][i] == False: #守門のみ
        df_all["広神ダム流域"][i] = df_all["守門"][i]
        df_all["和田川下流域"][i] = df_all["守門"][i]
        df_all["流域平均雨量"][i] = df_all["守門"][i]
        print(df_all.index[i],"caution!守門のみ")    
    elif hantei["堀之内"][i] == True and hantei["守門"][i] == True and hantei["小出"][i] == False: #小出のみ
        df_all["広神ダム流域"][i] = df_all["小出"][i]
        df_all["和田川下流域"][i] = df_all["小出"][i]
        df_all["流域平均雨量"][i] = df_all["小出"][i]
        print(df_all.index[i],"caution!小出のみ")
    else:
        pass
        print(df_all.index[i],"caution!caution!caution!caution!caution!")
        

df_all


# In[27]:


df_all['48時間雨量'] = df_all['流域平均雨量'].rolling(48).sum() #48時間雨量
df_all
df_all.to_csv("流域平均雨量と48時間雨量.csv",encoding="shift-jis")


# In[28]:


df_b=pd.DataFrame(df_all['48時間雨量'].loc[time(9,0)])
print(df_all.isnull().any())
df_b.rename(columns = {'48時間雨量':'2日雨量'},inplace=True)
df_b.to_csv("2日雨量_流域平均.csv",encoding="shift-jis")


# # ↓は年最大の雨量を抽出した。値はあっているが、<br> 日付は合っていない。直し方不明</br>
# 

# In[29]:


df_c = df_b.resample('1Y').max()
df_c.to_csv("各年最大_2日雨量_流域平均.csv",encoding="shift-jis")


# In[30]:


df_c


# In[ ]:




