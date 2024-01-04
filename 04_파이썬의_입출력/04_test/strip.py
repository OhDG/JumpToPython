f = open("/Users/ohdonggyu/Documents/JumpToPython/04_파이썬의_입출력/04_test/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()