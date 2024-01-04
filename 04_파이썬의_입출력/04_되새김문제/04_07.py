# 파일의 문자열 바꾸기

# Life is too short
# you need java

f = open('test.txt', 'r')
body = f.read()
f.close()
body = body.replace("java", "python")
f = open('test.txt', 'w')
f.write(body)
f.close()


# 책 정답

# 동일