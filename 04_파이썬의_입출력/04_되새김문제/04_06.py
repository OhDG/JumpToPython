# 사용자 입력 저장하기

user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()


# 책 정답

# 동일