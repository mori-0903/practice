# フォルダ説明
## convert_prog  
主に会社で作成したデータを変換するためのプログラムです。  
- mesh_code_org.py  
    time.d内にある形式の.CSVファイルを社内のソフトウェア用に変換するプログラムです。(※pandasをインストールする必要があります。)  
    実行の方法はgogo_py.shを叩けば実行できます。  
    (python␣mesh_code_org.py␣入力ファイル␣出力ファイル でも実行できます。)
- go_py.sh  
    主に社内で使われているシェルスクリプトの方式に従ってmesh_code_org.pyを動かすために作成したシェルスクリプトファイルです。
- gogo_py.sh
    go_py.sh  
    と同様、社内の方式に従って作成したシェルスクリプトです。  
    上司の方曰く、  
    
    > ループを回さずにかける  
    
    ことがメリットだそうです。

- time.d  
    mesh_code_org.pyを動かすための入力ファイルが入ったフォルダです。
- outcv  
    gogo_py.shを叩くと作成される出力用フォルダです。

## progate
主にプロゲートで学習したもののアウトプットです。
- programnote.txt  
    プロゲートで学習した内容をメモしたファイルです。
- index.html, stylesheet.css, _config.yml  
    プロゲートで学習したものの副産物です。

## scrape_jma
気象庁から時間雨量をスクレイピングするファイルです。
- scrape_pd_moriyama.py  
主にpandasを用いて気象庁から新潟県の**守門**地域の**時間雨量データ**を**1か月分**スクレイピングするプログラムです。  
(※pandas, lxmlが必要です。)  
jma_data_sumonの中に1日ごとのデータがcsvファイルとして出力されます。  
(Windows上で読みやすいようにshift-jis形式になっています。)
- scrape_pd_1h_gui.py  
誰でも使いやすくするためにguiにしようとしたプログラムです。今回pysimpleguiを使ったのは初めてだったので、粗が目立ちます。また、動作も不安定です。  
PySimpleGUIをインストールする必要があります。また、UNIX上では出力モニタを設定しないと動作しません。
- scrape_pd_1h_gui_tk.py  
tinkerというライブラリを使った方法でguiにしようとしたプログラムです。作成途中でまだ実行できません。
- jma_data_sumon
scrape_pd_moriyama.pyを実行されると作成される出力用フォルダです。エンコードがshift-jis形式のcsvファイルが作成されています。  

## tissen_split
convert_progフォルダと同様、主に会社で業務上必要となった際に作成したプログラムです。
- tissen_split.ipynb  
    新潟県の魚沼地域にある一級河川の**和田川**という川の流域をティーセン分割するために、とある方式に基づいてティーセン係数を算出させるプログラムです。
- for_2dayraubcal.py  
    tissen_split.ipynb をpythonファイルに変換したものです。