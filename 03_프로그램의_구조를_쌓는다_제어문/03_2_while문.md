# while 문

> 문장을 반복해서 수행해야 할 경우 while 문을 사용한다. 그래서 while 문을 '반복문'이라고도 부른다.

## while 문의 기본 구조

`while 문의 기본 구조`

```python
while 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3
    ...
```

> while 문은 조건문이 참인 동안 while 문에 속한 문장들이 반복해서 수행된다.

```python
treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
# 나무를 1번 찍었습니다.
# 나무를 2번 찍었습니다.
# 나무를 3번 찍었습니다.
# 나무를 4번 찍었습니다.
# 나무를 5번 찍었습니다.
# 나무를 6번 찍었습니다.
# 나무를 7번 찍었습니다.
# 나무를 8번 찍었습니다.
# 나무를 9번 찍었습니다.
# 나무를 10번 찍었습니다.
# 나무 넘어갑니다.
```

> while 문의 조건문은 treeHit < 10이다. 즉, treeHit가 10보다 작은 동안 while 문에 포함된 문장들을 계속 수행한다. <br>
> while문 안의 문장을 보면 가장 먼저 treeHit = treeHit + 1로 treeHit 값이 계속 1씩 증가한다는 것을 알 수 있다. 그리고 나무를 treeHit번만큼 찍었다는 것을 알리는 문장을 출력하고 treeHit가 10이 되면 "나무 넘어갑니다."라는 문장을 출력한다. <br>
> 그러고 나면 treeHit < 10 조건문이 거짓이 되므로 while 문을 빠져나가게 된다.

| treeHit | 조건문 | 조건 판단 | 수행하는 문장                            | while 문 |
| ------- | ------ | --------- | ---------------------------------------- | -------- |
| 0       | 0<10   | 참        | 나무를 1번 찍었습니다.                   | 반복     |
| 1       | 1<10   | 참        | 나무를 2번 찍었습니다.                   | 반복     |
| 2       | 2<10   | 참        | 나무를 3번 찍었습니다.                   | 반복     |
| 3       | 3<10   | 참        | 나무를 4번 찍었습니다.                   | 반복     |
| 4       | 4<10   | 참        | 나무를 5번 찍었습니다.                   | 반복     |
| 5       | 5<10   | 참        | 나무를 6번 찍었습니다.                   | 반복     |
| 6       | 6<10   | 참        | 나무를 7번 찍었습니다.                   | 반복     |
| 7       | 7<10   | 참        | 나무를 8번 찍었습니다.                   | 반복     |
| 8       | 8<10   | 참        | 나무를 9번 찍었습니다.                   | 반복     |
| 9       | 9<10   | 참        | 나무를 10번 찍었습니다. 나무 넘어갑니다. | 반복     |
| 10      | 10<10  | 거짓      |                                          | 종료     |

## while 문 만들기

```python
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

# 1. Add
# 2. Del
# 3. List
# 4. Quit
#
# Enter number:
1

# 1. Add
# 2. Del
# 3. List
# 4. Quit
#
# Enter number:
4
```

## while 문 강제로 빠져나가기

```python
coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
```

> money가 300으로 고정되어 있고 while money:에서 조건문인 money는 0이 아니기 때문에 항상 참이다. 따라서 무한히 반복되는 무한 루프를 돌게 된다. <br>
> 만약 coffee가 0이 되면 if coffee == 0: 문장에서 coffee == 0이 참이 되므로 if 문 다음 문장 "커피가 다 떨어졌습니다. 판매를 중지합니다."가 출력되고 break 문이 호출되어 while 문을 빠져나가게 된다.

```python
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려 주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 돈을 넣어주세요: 500
# 거스름돈 200을 주고 커피를 줍니다.
# 돈을 넣어주세요: 300
# 커피를 줍니다.
# 돈을 넣어주세요: 100
# 돈을 다시 돌려 주고 커피를 주지 않습니다.
# 남은 커피의 양은 8개 입니다.
# 돈을 넣어주세요:
```

## while 문의 맨 처음으로 돌아가기

> 프로그래밍을 하다 보면 while 문을 빠져나가지 않고 while 문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우가 생기게 된다. 이때 사용하는 것이 바로 `continue` 문이다.

> 1부터 10까지의 숫자 중에서 홀수만 출력하는 것을 while 문을 사용해서 작성한다.

```python
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
# 1
# 3
# 5
# 7
# 9
```

## 무한 루프

> 무한 루프란 무한히 반복한다는 의미이다.

`무한 루프의 기본 형태`

```python
while True:
    수행할_문장1
    수행할_문장2
    ...
```

```python
while True:
    print("Ctrl+C를 눌러야 while 문을 빠져나갈 수 있습니다.")
# Ctrl+C를 눌러야 while 문을 빠져나갈 수 있습니다.
# Ctrl+C를 눌러야 while 문을 빠져나갈 수 있습니다.
# Ctrl+C를 눌러야 while 문을 빠져나갈 수 있습니다.
# ...
```
