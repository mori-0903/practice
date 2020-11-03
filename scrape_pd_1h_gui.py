# coding: utf-8
import pandas as pd
import datetime
import os
import time
import PySimpleGUI as sg

month     = 1
day       = 1

layout = [
    [sg.Text("気象庁から（のみ）時間データ（雨量）を収集します")],
    [sg.Text("参照：",size=(10,1)),sg.InputText("http://k-ichikawa.blog.enjoy.jp/etc/HP/htm/jmaP0.html")],
    [sg.Text("開始年",size=(20,1)),sg.InputText("2010")],
    [sg.Text("終了年",size=(20,1)),sg.InputText("2012")],
    [sg.Text("prec_no",size=(20,1)),sg.InputText("54")],
    [sg.Text("block_no",size=(20,1)),sg.InputText("997")],
    [sg.Submit(button_text="実行",key="bt"), sg.Cancel()],
]

def scrape_jma(year,end_year,prec_no,block_no):
    year      = year #開始年
    end_year  = end_year
    prec_no   = prec_no
    block_no  = block_no
    # data_type = "10min"
    data_type = "hourly"
    out_dir   = "./jma_data_1h"
    os.makedirs(out_dir, exist_ok=True)
    date     = datetime.date(year, month, day)
    date_c   = datetime.date(year, month, day)
    base_url = "https://www.data.jma.go.jp/obd/stats/etrn/view/{}_a1.php?prec_no={:0>2}&block_no={:0>4}&year={:0>4}&month={:0>2}&day={:0>2}&view="
    df_all = pd.DataFrame() #空のデータフレーム作成

    while date.year < end_year + 1:
        tar_url = base_url.format(data_type,prec_no,block_no,date.year,date.month,date.day)
        dfs = pd.read_html(tar_url)
        df_rain = dfs[0]["降水量(mm)"].copy()
        date_n = date + datetime.timedelta(days=1)
        df_rain['time'] = pd.date_range(str(date)+' 01:00:00', str(date_n)+' 00:00:00', freq='H')
        df_rain = df_rain.set_index("time")
        print(date)
        df_all = pd.concat([df_all, df_rain]) #df_rainをdf_allに追加してゆく
        date_c += datetime.timedelta(days=1)
        if date.year != date_c.year: #ここで年が切り替わったらdf_allをリセットして次の年から書き直す
            print(date.year)
            out_fname = os.path.join(out_dir, "{}年.csv".format(date.year))
            df_all.to_csv(out_fname, encoding="shift-jis")
            df_all = pd.DataFrame() #ここでリセットする
        date += datetime.timedelta(days=1) 
        time.sleep(1)
#        sg.OneLineProgressMeter('One Line Meter Example', i + 1, 1000, 'key')
    out_fname = os.path.join(out_dir, "{}_rain.csv".format(date.year))
    df_all.to_csv(out_fname, encoding="shift-jis")    


window = sg.Window('気象庁からのデータ収集',layout)


while True:
    event, values = window.read()
    if event in (None,'Cancel'):
        print("exit")
        break

    if event == "bt": 
        scrape_jma(int(values[1]),int(values[2]),int(values[3]),int(values[4]))
        sg.popup('処理を実行しました')

window.close()
