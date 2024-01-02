# 조건문의 참과 거짓

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# shirt


# 책 정답

# 결괏값으로 shirt가 출력된다.

# 1 첫 번째 조건: "wife"라는 단어는 a 문자열에 없으므로 거짓이다.
# 2 두 번째 조건: "python"이라는 단어는 a 문자열에 있지만 "you" 역시 a 문자열에 있으므로 거짓이다.
# 3 세 번째 조건: "shirt"라는 단어가 a 문자열에 없으므로 참이다.
# 4 네 번째 조건: "need"라는 단어가 a 문자열에 있으므로 참이다.

# 가장 먼저 참이 되는 것이 세 번째 조건이므로 "shirt"가 출력된다.