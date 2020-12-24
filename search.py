
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

import pandas as pd

with open("source.csv", mode = 'a') as f:
    writer = csv.writer(f)
    writer.writerow(source)
    source = pd.read_csv("source.csv")

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("見つかりませんでした")

    add = input("追加しますか？ (0:はい 1:いいえ) >>> ")
    if add == "0":
        source.append(word)
    
    df=pd.DataFrame("source.csv")
    df.to_csv("source.csv")
    print(df)
 
if __name__ == "__main__":
    search()