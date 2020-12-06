# フォルダ説明
## convert_prog  
### 主に会社で作成したデータを変換するためのプログラムです。  
- mesh_code_org.py  
    time.d内にある形式の.CSVファイルを社内のソフトウェア用に変換するプログラムです。(※pandasをインストールする必要があります。)  
    実行の方法はgogo_py.shを叩けば実行できます。  
    (python␣mesh_code_org.py␣入力ファイル␣出力ファイルでも実行できます。)
- go_py.sh  
    主に社内で使われているシェルスクリプトの方式に従ってmesh_code_org.pyを動かすために作成したシェルスクリプトファイルです。
- gogo_py.sh
    go_py.sh  
    と同様、社内の方式に従って作成したシェルスクリプトです。  
    上司の方曰く、ループを回さずにかけることがメリットだそうです。

- time.d  
    mesh_code_org.pyを動かすための入力ファイルが入ったフォルダです。
- outcv  
    gogo_py.shを叩くと作成される出力用フォルダです。

## progate

## scrape_jma

## tissen_split
- tissen_split.ipynb  
    新潟県の魚沼地域にある一級河川の和田川という川の流域をティーセン分割するために、とある方式に基づいてティーセン係数を算出させるプログラムです。
- for_2dayraubcal.py  
    tissen_split.ipynb をpythonファイルに変換したものです。