# 입력값을 모두 더해 출력하기

# myargv.py

import sys
result = 0
args = sys.argv[1:]
for i in args:
    result += int(i)
print(result)


# 책 정답

# 동일