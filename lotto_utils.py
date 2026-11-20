import random
print(random.randint(1, 45))           # 1~45 정수하나
print(random.choice([10, 20, 30]))     # 목록에서하나
nums = [1, 2, 3, 4, 5]
r = random.shuffle(nums)               # 원본순서를섞음
print(nums, r)
print(random.sample(range(1, 46), 6))  # 서로다른6개
print(random.sample(range(1, 46), 6))

a = [33, 7, 21]
b = sorted(a)                 # 정렬된'새' 리스트
print(a, b)
r = a.sort()                  # 원본a를정렬, 돌려주는값None
print(a, r)
print(sorted(a, reverse=True))   # 큰것부터
print(', '.join(['사과', '배', '감']))
print('-'.join(['2026', '11', '08']))
nums = [3, 15, 22]
strs = []
for n in nums:
    strs.append(str(n))       # 숫자→ 글자
print(strs)
print(' - '.join(strs))

import random
import pandas as pd

def make_game() :
    return sorted(random.sample(range(1, 46), 6))
def make_games(count) :
    games = []
    for i in range(count) :
        games.append(make_game())
    return games

def to_text(game) :
    words = []
    for n in game :
        words.append(f'{n:3d}')
    return ' '.join(words)