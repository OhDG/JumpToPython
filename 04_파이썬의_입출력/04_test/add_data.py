f = open("/Users/ohdonggyu/Documents/JumpToPython/04_파이썬의_입출력/04_test/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()