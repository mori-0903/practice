import pandas as pd
import datetime
import os
import time

year     = 2010
month    = 1
day      = 1
prec_no  = 54
block_no = 997

out_dir = "./jma_data_sumon"
os.makedirs(out_dir, exist_ok=True)

date = datetime.date(year, month, day)

base_url = "https://www.data.jma.go.jp/obd/stats/etrn/view/10min_a1.php?prec_no={:02}&block_no={:04}&year={:04}&month={:02}&day={:02}&view="
tar_url = base_url.format(prec_no,block_no,date.year,date.month,date.day)
# print(tar_url)
while date.month == 1:
    tar_url = base_url.format(prec_no,block_no,date.year,date.month,date.day)
    dfs = pd.read_html(tar_url)

    df_rain = dfs[0]["降水量(mm)"].copy()
    date_n = date + datetime.timedelta(days=1)
    df_rain['time'] = pd.date_range(str(date)+' 00:10:00', str(date_n)+' 00:00:00', freq='10min')

    df_rain = df_rain.set_index("time")
    print(date)
    out_fname = os.path.join(out_dir, "10min_rain_{}.csv".format(date))
    df_rain.to_csv(out_fname, encoding="shift-jis")
    date += datetime.timedelta(days=1)
    time.sleep(1)