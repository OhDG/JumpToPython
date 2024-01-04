f = open("/Users/ohdonggyu/Documents/JumpToPython/04_파이썬의_입출력/04_test/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
