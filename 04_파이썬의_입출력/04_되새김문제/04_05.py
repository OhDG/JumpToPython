# 프로그램 오류 수정하기 2

f1 = open("test.txt", 'w')
f1.write("Life is too short!")

f2 = open("test.txt", 'r')
print(f2.read())


# 책 정답
# 문제의 예와 같이 파일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다. 따라서 열린 파일 객체를 close로 닫아준 후 다시 열어서 파일의 내용을 읽어야 한다.

# A1
f1 = open("test.txt", 'w')
f1.write("Life is too short!")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

# A2
with open("test.txt", 'w') as f1:
    f1.write("Life is too short!")

with open("test.txt", 'r') as f2:
    print(f2.read())
