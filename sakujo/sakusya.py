"""
#s = 'New research, published in Circulation: Cardiovascular Quality and Outcomes, finds women who have endometriosis, the abnormal growth of uterine tissue outside the uterus, may face a 60 percent higher risk of developing heart disease than women without the disorder. The potential risk was especially high for women 40 or younger. At least 10 percent of women of reproductive age suffer from endometriosis (endo) says Dr. Stacey Missmer of Brigham and Womens Hospital, who co-authored the study. (UPI) (NBC News)'
#s = "One British woman is killed and two others are wounded in a stabbing attack on a North Queensland backpacker hostel, Australia. (News.com) (ABC News Australia)"
s = "SeaLife Center (endo). (Seward. Alaska)(UPI)"
cleaned_s = s

for i in range(len(s) - 1, -1, -1):
    if s[i] == '.':
        break
    if s[i] == '(':
        j = i
        while s[j] != ')':
            j += 1
        cleaned_s = cleaned_s[:i] + cleaned_s[j + 1:]

print(cleaned_s)
"""


"""
import re

text = "New research, published in Circulation: Cardiovascular Quality and Outcomes, finds women who have endometriosis, the abnormal growth of uterine tissue outside the uterus, may face a 60 percent higher risk of developing heart disease than women without the disorder. The potential risk was especially high for women 40 or younger. At least 10 percent of women of reproductive age suffer from endometriosis (endo) says Dr. Stacey Missmer of Brigham and Women's Hospital, who co-authored the study. (UPI) (NBC News)"

# 括弧 () 内の部分を削除
result = re.sub(r'\([^)]*\)', '', text)

print(result)
"""

import pandas as pd

df = pd.read_excel('出来事複数のみ.xlsx', engine='openpyxl')
event_text = df['出来事']


# 削除する場所
def findsakujo(s):
    kakko = 0  #かっこの中か外か
    sakujo = len(s)  # 削除開始位置

    # 括弧を逆から数え、(UPI.) (NBC News) の外側のピリオドを見つける
    for i in range(len(s) - 1, 0, -1): #-1（後ろ）から始めて0まで、-1ずつしていく
        char = s[i]
        if char == ')':
            kakko += 1
        elif char == '(':
            kakko -= 1
        if kakko == 0 and char == '.':
            sakujo = i 
            break

    return sakujo

# ピリオドの前を取り除く
def honbun(event):
    start = findsakujo(event)  # findsakujo 関数の返り値を start に代入
    aftersakujo = event[:start] #:startでstartより前の文章を持ってくる
    return aftersakujo


# 各行の出来事の本文を取り出す
sakujo_texts = [] 

# 全ての出来事に対して削除を行う
for event in event_text:
    sakujo_event = honbun(event)  
    print(sakujo_event)
    print("-------------------------------")
    sakujo_texts.append(sakujo_event)

#df['削除後の文章'] = sakujo_texts

#df.to_excel("複数の出来事削除後2.xlsx", index=False, engine='openpyxl')

