#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os
import csv
import sys

args = sys.argv

indata = args[1]
outdata = args[2] 

outdata = os.path.join("./outcv",outdata)

# filename="fv_oyabe.dat"

# df = pd.read_csv("MAXALL_TIME.CSV",encoding="EUC-JP",skiprows=2)
df = pd.read_csv(indata,encoding="shift-jis",skiprows=2)

df["FV_meshcode"]=np.nan


df["FV_meshcode"] = df["メッシュコード"].astype(str).str[:4].map('{:0>4}'.format)+"-"+\
                    df["メッシュコード"].astype(str).str[4:6].map('{:0>2}'.format)+"-"+\
                    df["メッシュコード"].astype(str).str[6:8].map('{:0>2}'.format)+'-'+\
                    df["メッシュコード"].astype(str).str[9:11].map('{:0>4}'.format)+\
                    df["メッシュコード"].astype(str).str[11:13].map('{:0>4}'.format)

df_c = pd.DataFrame()
df_c['FV_meshcode'] = df["FV_meshcode"].copy()
df_c['0.5m浸水継続時間']  = df["0.5m浸水継続時間"].copy() / 60.0
df_c = df_c.round({'0.5m浸水継続時間': 2})
# c = df_c.values.tolist()
# c.insert([0],[200,200])
# c = pd.DataFrame(c)
# print(c[0])
# os.remove('test.csv')
if(os.path.exists(outdata)):
    os.remove(outdata)

with open(outdata, 'w') as f:
    f.write(' 40 40'+"\n")
print(df_c)
df_c.to_csv(outdata,encoding="utf-8",index=False,sep=' ',doublequote=False,header=False,mode='a')
# os.remove('test')
