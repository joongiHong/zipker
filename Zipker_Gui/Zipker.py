# coding=utf-8

# 모듈 불러오기
import zipfile
import sys
import shutil
import ctypes
import os
import time
from itertools import permutations

# 버전 호출 함수


def version():
    ver = "0.2.0"
    return ver


# 압축파일 존재 유무 함수

def zip_file(filename):
    is_zfile = zipfile.is_zipfile(filename)
    return is_zfile


# 암호 대입 함수

def zip_password(filename, password):
    zfile = zipfile.ZipFile(filename)

    try:
        zfile.extractall(path='temp', pwd=password.encode())
        shutil.rmtree(r"temp")
        return True  # 암호 일치시 True 반환
    except:
        shutil.rmtree(r"temp")
        return False  # 암호 비 일치시 False 반환


# 문자열 선택 함수

def string(num):
    user_string = str(num)
    if user_string == "1":
        password_decrypt_list = ['0', '1', '2', '3',
                                 '4', '5', '6', '7', '8', '9']  # 숫자만
        return password_decrypt_list  # 리스트 내용을 반환함.
    elif user_string == "2":
        password_decrypt_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # 알파벳
        return password_decrypt_list
    elif user_string == "3":
        password_decrypt_list = ['!', '@', '#', '$', '%', '^',
                                 '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '[', ']', ';', ':', '"', '\'', '<', '>', '?', '/']  # 특문
        return password_decrypt_list
    elif user_string == "4":
        password_decrypt_list = ['0', '1', '2', '3',
                                 '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # 숫자 + 알파벳
        return password_decrypt_list
    elif user_string == "5":
        password_decrypt_list = ['0', '1', '2', '3',
                                 '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^',
                                 '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '[', ']', ';', ':', '"', '\'', '<', '>', '?', '/']  # 숫자 + 특문
        return password_decrypt_list
    elif user_string == "6":
        password_decrypt_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^',
                                 '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '[', ']', ';', ':', '"', '\'', '<', '>', '?', '/']  # 알파벳 + 특문
        return password_decrypt_list
    elif user_string == "7":
        password_decrypt_list = ['0', '1', '2', '3',
                                 '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^',
                                 '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '[', ']', ';', ':', '"', '\'', '<', '>', '?', '/']  # 숫자 + 알파벳 + 특문
        return password_decrypt_list
    else:
        return False  # 에러를 반환함.


# 무차별 대입 함수

def zip_decrypt(filename, string, min, max):
    password_decrypt = 0
    decrypt_success = 0
    user_min = int(min)
    user_max = int(max)

    for user_count in range(user_min, user_max+1):
        for password_decrypt_exam in permutations(string, user_count):
            password_decrypt_exam2 = list(password_decrypt_exam)
            password_decrypt = ''.join(password_decrypt_exam2)

            sido = zip_password(filename, str(password_decrypt))
            if sido == True:
                decrypt_success = 1
                break
            else:
                continue

    if decrypt_success == 1:
        return password_decrypt
    else:
        return False


# 비 모듈 실행시 사용 코드

if __name__ == "__main__":
    os.system('cls')
    filename = input(
        "\n        ===================================\n\n[?] 비밀번호를 찾을 압축파일의 이름을 입력하세요.\n\n        ===================================\n>>> ")
    is_filename = zip_file(filename)

    if is_filename != True:
        os.system('cls')
        print(
            "\n        ===================================\n\n[!] 압축파일를 찾지 못하였습니다.")
        print("[!] 입력하신 파일 이름의 철자가 바르지 못할 수 있습니다.")
        print("[!] 다시 시도하여 보시기 바랍니다.\n\n        ===================================")
        sys.exit()

    os.system('cls')
    user_string = input(
        "\n        ===================================\n\n[*] 지금부터 대입에 사용할 문자열을 설정합니다.\n[*] 알맞는 옵션을 선택하여 주십시오.\n\n1. 숫자로만 이루어진 암호\n2. 알파벳으로만 이루어진 암호\n3. 특수문자로만 이루어진 암호\n4. 숫자+알파벳으로 이루어진 암호\n5. 숫자+특수문자로 이루어진 암호\n6. 알파벳+특수문자로 이루어진 암호\n7. 숫자+알파벳+특수문자로 이루어진 암호\n\n        ===================================\n>>> ")
    string = string(user_string)

    os.system('cls')
    user_min_string = int(input(
        "\n        ===================================\n\n[*] 지금부터 대입에 사용할 문자열의 최소 길이를 설정합니다.\n[*] 암호의 최소 길이를 입력해 주십시오. 0은 지정하지 않음입니다.\n\n        ===================================\n>>> "))

    os.system('cls')
    user_max_string = int(input(
        "\n        ===================================\n\n[*] 지금부터 대입에 사용할 문자열의 최대 길이를 설정합니다.\n[*] 암호의 최대 길이를 입력해 주십시오. 0은 지정하지 않음입니다.\n\n        ===================================\n>>> "))

    os.system('cls')
    print("\n        ===================================\n\n[!]", filename,
          "에 대한 무차별 대입 공격을 진행하고 있습니다.\n[!] 오랫동안 찾지 못할 경우 해결이 불가능한 경우이므로 종료하십시오.\n\n        ===================================")

    my_password = zip_decrypt(
        filename, string, user_min_string, user_max_string)

    if my_password == False:
        os.system('cls')
        print(
            "\n        ===================================\n\n[*] 비밀번호를 찾지 못하였습니다.")
        print("[*] 선택하신 문자열이나 최소, 최대 길이가 잘못되었을 수 있습니다.")
        print("[*] 다시 선택하신 후 시도해 보십시오.\n\n        ===================================")
    else:
        os.system('cls')
        print(
            "\n        ===================================\n\n[*] 비밀번호를 찾았습니다.")
        print("[*] 비밀번호는", my_password, "입니다.")
        print("[*] 본 프로그램은 압축 해제를 지원하지 않으므로 타 프로그램을 사용하여 해제하십시오.\n\n        ===================================")
