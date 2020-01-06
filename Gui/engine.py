# -*- coding: utf-8 -*-

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
    filename, user_string, f_user_min_string, f_user_max_string = str(
        input()).split(";")

    string = string(user_string)
    user_min_string = int(f_user_min_string)
    user_max_string = int(f_user_max_string)

    # 존재 여부 (없을 경우 1 반환)
    is_filename = zip_file(filename)
    if is_filename != True:
        f = open('result.txt', 'w')
        f.write("1")
        f.close()
        sys.exit()

    # 대입
    my_password = zip_decrypt(
        filename, string, user_min_string, user_max_string)

    if my_password == False:
        f = open('result.txt', 'w')
        f.write("2")
        f.close()
        sys.exit()
    else:
        f = open('result.txt', 'w')
        f.write(my_password)
        f.close()
        sys.exit()
