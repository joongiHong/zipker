# coding=utf-8

# 임포트 파트
import zipfile
import sys
import shutil
import ctypes
import os
import time
from itertools import permutations

# 각종 함수 선언 파트


def MessageBox(title, text, style):
    # 메시지박스 함수
    return ctypes.windll.user32.MessageBoxW(None, text, title, style)


def zip_decrypt(password):
    zfile.extractall(path='temp', pwd=password.encode())  # 비밀번호 대입 함수


# 이전에 시도한 적이 있는지 검사하는 파트

if os.path.isdir("temp") == True:
    print(
        "\n        ===================================\n\n[!] 본 프로그램이 이전에 비정상적으로 종료된 적이 있는 것 같습니다.\n[!] 다시 실행하여 주십시오.\n\n        ===================================")
    shutil.rmtree(r"temp")
    time.sleep(0.5)
    sys.exit()


# ZIP 정보 수집 파트
# 압축파일 이름을 zname으로 받음

while True:
    zname = input(
        "\n        ===================================\n\n[?] 비밀번호를 찾을 압축파일의 이름을 입력하세요.\n\n        ===================================\n>>> ")
    is_zname = zipfile.is_zipfile(zname)  # 파일 유무를 True와 False로 저장함

    if is_zname != True:
        user_error_yn = MessageBox('Zipker - 압축파일 비밀번호 해제',
                                   '입력하신 Zip 파일을 찾지 못하였습니다.\n[Error Code = F-1]\n\n입력하신 이름이 올바른지 다시 한번 확인하여 주시고\n본 파일과 동일한 디렉토리에 존재하는지 확인하여 주십시오.\n자세한 내용은 동봉된 설명서를 참고하세요.', 5)
        if user_error_yn <= 2:
            sys.exit()
        else:
            os.system('cls')
            continue
    else:
        break

zfile = zipfile.ZipFile(zname)  # 추후 사용할 zfile 지정

# 문자열 선택 파트

os.system('cls')
user_string = int(input(
    "\n        ===================================\n\n[*] 지금부터 대입에 사용할 문자열을 설정합니다.\n[*] 알맞는 옵션을 선택하여 주십시오.\n\n1. 숫자로만 이루어진 암호\n2. 알파벳으로만 이루어진 암호\n3. 특수문자로만 이루어진 암호\n4. 숫자+알파벳으로 이루어진 암호\n5. 숫자+특수문자로 이루어진 암호\n6. 알파벳+특수문자로 이루어진 암호\n7. 숫자+알파벳+특수문자로 이루어진 암호\n\n        ===================================\n>>> "))

if user_string == 1:
    password_decrypt_list = ['0', '1', '2', '3',
                             '4', '5', '6', '7', '8', '9']  # 숫자만
elif user_string == 2:
    password_decrypt_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # 알파벳
elif user_string == 3:
    password_decrypt_list = ['!', '@', '#', '$', '%', '^',
                             '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '[', ']', ';', ':', '"', '\'', '<', '>', '?', '/']  # 특문
elif user_string == 4:
    password_decrypt_list = ['0', '1', '2', '3',
                             '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # 숫자 + 알파벳
elif user_string == 5:
    password_decrypt_list = ['0', '1', '2', '3',
                             '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^',
                             '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '[', ']', ';', ':', '"', '\'', '<', '>', '?', '/']  # 숫자 + 특문
elif user_string == 6:
    password_decrypt_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^',
                             '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '[', ']', ';', ':', '"', '\'', '<', '>', '?', '/']  # 알파벳 + 특문
elif user_string == 7:
    password_decrypt_list = ['0', '1', '2', '3',
                             '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^',
                             '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '[', ']', ';', ':', '"', '\'', '<', '>', '?', '/']  # 숫자 + 알파벳 + 특문

# 문자열 길이 범위 선택 파트

os.system('cls')
user_min_string = int(input(
    "\n        ===================================\n\n[*] 지금부터 대입에 사용할 문자열의 최소 길이를 설정합니다.\n[*] 암호의 최소 길이를 입력해 주십시오. 0은 지정하지 않음입니다.\n\n        ===================================\n>>> "))

os.system('cls')
user_max_string = int(input(
    "\n        ===================================\n\n[*] 지금부터 대입에 사용할 문자열의 최대 길이를 설정합니다.\n[*] 암호의 최대 길이를 입력해 주십시오. 0은 지정하지 않음입니다.\n\n        ===================================\n>>> "))

# 무차별 대입 시도 파트

os.system('cls')
print("\n        ===================================\n\n[!]", zname,
      "에 대한 무차별 대입 공격을 진행하고 있습니다.\n[!] 오랫동안 찾지 못할 경우 해결이 불가능한 경우이므로 종료하십시오.\n\n        ===================================")

password_decrypt = 0  # 암호 변수
decrypt_success = 0  # 성공 여부 변수

for user_count in range(user_min_string, user_max_string+1):
    for password_decrypt_exam in permutations(password_decrypt_list, user_count):
        password_decrypt_exam2 = list(password_decrypt_exam)
        password_decrypt = ''.join(password_decrypt_exam2)
        try:
            zip_decrypt(str(password_decrypt))
            decrypt_success = 1
            break
        except:
            pass

'''
while decrypt_success != 1:
    try:
        os.system('cls')
        print("\n        ===================================\n\n[*] 지금", zname,
              "에 대한 무차별 대입 공격을 진행중입니다...\n[*] 암호의 길이에 따라 많은 시간이 소요될 수 있습니다...\n\n지금 대입중인 문자열 :", password_decrypt, "\n\n        ===================================")
        zip_decrypt(str(password_decrypt))
        decrypt_success = 1
    except:
        password_decrypt = password_decrypt + 1
        pass
'''

# 결과 보고 파트

os.system('cls')
if decrypt_success == 1:
    shutil.rmtree(r"temp")  # 압축 해제한 파일 삭제
    print("\n        ===================================\n\n[*] 비밀번호를 찾았습니다.")
    print("[*] 비밀번호는", password_decrypt, "입니다.")
    print("[*] 본 프로그램은 압축 해제를 지원하지 않으므로 타 프로그램을 사용하여 해제하십시오.\n\n        ===================================")
else:
    print(
        "\n        ===================================\n\n[*] 비밀번호를 찾지 못하였습니다.")
    print("[*] 선택하신 문자열이나 최소, 최대 길이가 잘못되었을 수 있습니다.")
    print("[*] 다시 선택하신 후 시도해 보십시오.\n\n        ===================================")
