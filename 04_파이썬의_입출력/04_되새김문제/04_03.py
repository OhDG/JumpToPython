# 프로그램 오류 수정하기 1

input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")

total = input1 + input2
print("두 수의 합은 %s입니다" % total)


input1 = int(input("첫 번째 숫자를 입력하세요: "))
input2 = int(input("두 번째 숫자를 입력하세요: "))

total = input1 + input2
print("두 수의 합은 %s입니다" % total)


# 책 정답
input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다" % total)