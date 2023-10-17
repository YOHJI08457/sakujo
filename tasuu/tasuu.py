"""
import collections

l = ['International relations', 'International relations', 'International relations', 'Health and medicine', 'Health and medicine', 'Business and economics', 'Armed conflicts and attacks']

c = collections.Counter(l)
print(c)

print(c.most_common()[0])

"""

"""
import pandas as pd
from collections import Counter

# エクセルファイルを読み込む
df = pd.read_excel('出来事複数のみ.xlsx')  # エクセルファイルのパスを指定

# 「TOPIC」と「出来事」の列のデータを取得
A = df["TOPIC"].tolist()
B = df["カテゴリー"].tolist()

result = {}  # 結果を格納する辞書

for a, b in zip(A, B):
    if a not in result:
        result[a] = []  # 新しい要素の場合、空のリストを作成
    result[a].append(b)

# 結果の表示
for key, value in result.items():
    c = Counter(value)  # 各要素に対してCounterを作成
    most_common = c.most_common(1)[0]  # 最も一般的な要素を取得
    print(f"{key} : {most_common[0]}")
"""

import pandas as pd
from collections import Counter

df = pd.read_excel('出来事複数のみ.xlsx') 

A = df["TOPIC"].tolist()
B = df["カテゴリー"].tolist()


tasuu = {}
for i in range(len(A)):
    topic = A[i]
    category = B[i]
    
    if topic not in tasuu: #新しいトピックなら新しいリストを作る
        tasuu[topic] = {}
    
    if category not in tasuu[topic]: #今のカテゴリーがそのリスト内に含まれているかどうか
        tasuu[topic][category] = 0 #含まれていなかったら新しい枠を作る
    
    tasuu[topic][category] += 1

for topic, category in tasuu.items():
    print(topic,category)
    maxcate = max(category, key=category.get)
    print(maxcate)