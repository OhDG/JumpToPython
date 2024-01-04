# 출력 결과가 다른 것은?

print("you" "need" "python")
# youneedpython
print("you" + "need" + "python")
# youneedpython
print("you", "need", "python")
# you need python
print("".join(["you", "need", "python"]))
# youneedpython


# 책 정답

# 쉼표(,)가 있는 경우 공백이 삽입되어 더해진다.