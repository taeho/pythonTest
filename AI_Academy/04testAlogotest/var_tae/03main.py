# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# In Python3, Use 'input()' function to read data from standard input
# val_inp = 10
# input_list = []

# for i in range(0, val_inp):
#	input_list.append(input())

# for j in range(0, val_inp):
#	print(res_is_panlindrome(input_list[j]))

# 팬린드롬 여부 체크
def res_is_panlindrome(key_input):
    # list 형태로 변경
    list_keyword = list(key_input)
    # for문은 길이 절반만 검사
    for i in range(0, len(list_keyword) // 2):
        # 처음과 뒤를 비교 검사 같으면 넘어가고
        if list_keyword[i] == list_keyword[len(list_keyword) - 1 - i]:
            continue
        else:  # 다르면 no로 반환
            return 'NO'
    return 'YES'  # 다 continue 통과하면 yes


def testcase():
    word = input().strip()
    print(res_is_panlindrome(word))


# YES 혹은 NO를 출력한다.
# print("YES")
# print("NO")

def main():
    for i in range(10):
        testcase()


if __name__ == "__main__":
    main()
