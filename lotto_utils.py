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

# [블록4] CSV 읽기→ 번호별당첨횟수딕셔너리
COLS = ['당첨번호1', '당첨번호2', '당첨번호3','당첨번호4', '당첨번호5', '당첨번호6']

def load_counts(fname):
    df = pd.read_csv(fname, encoding='utf-8-sig')
    count = {}
    for n in range(1, 46):
        count[n] = 0
    for col in COLS:
        for n in df[col]:
            count[n] += 1
    return count

# [블록5] 자주나온번호top개(횟수내림차순)
def top_numbers(count, top=20):
    items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    nums = []
    for n, c in items[:top]:
        nums.append(n)
    return nums

# [블록6] 자주나온번호20개중에서한게임
def make_hot_game(count):
    return sorted(random.sample(top_numbers(count), 6))

# [블록7] 내가고른번호+ 나머지는자동
def fill_game(picked):
    rest = []
    for n in range(1, 46):
        if n not in picked:
            rest.append(n)
    game = list(picked) + random.sample(rest, 6 - len(picked))
    return sorted(game)