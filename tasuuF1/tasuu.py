import pandas as pd
from collections import Counter
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

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


maxcategories = [] 

for topic, categories in tasuu.items():
    #print(topic,category)
    maxcategory = max(categories, key=categories.get)
    maxcategories.append(maxcategory)

#print(maxcategories)


df_true = pd.read_excel('正解のデータ複数のみ.xlsx')
C = df_true["カテゴリー"].tolist()
hikaku = []
for i in range(len(C)):
    hikaku.append(C[i])  

#print(hikaku)


precision = precision_score(hikaku, maxcategories, average='weighted', zero_division=1)
print("適合率:", precision)

recall = recall_score(hikaku, maxcategories, average='weighted', zero_division=1)
print("再現率:", recall)

f1 = f1_score(hikaku, maxcategories, average='weighted', zero_division=1)
print("F1スコア:", f1)



"""
from sklearn.metrics import accuracy_score

y_true = ['car', 'car', 'bus', 'car', 'mas', 'car']
y_pred = ['car', 'mas', 'mas', 'car', 'mas', 'bus']

print(accuracy_score(y_true, y_pred))
"""