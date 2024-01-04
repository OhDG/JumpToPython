f = open("/Users/ohdonggyu/Documents/JumpToPython/04_파이썬의_입출력/04_test/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()