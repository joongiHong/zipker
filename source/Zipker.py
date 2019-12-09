# 임포트 파트
import zipfile
import sys
import shutil
import ctypes
import os
import time

# 각종 함수 선언 파트


def MessageBox(title, text, style):
    # 메시지박스 함수
    return ctypes.windll.user32.MessageBoxW(None, text, title, style)


def zip_decrypt(password):
    zfile.extractall(path='temp', pwd=password.encode())  # 비밀번호 대입 함수


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

# 무차별 대입 시도 파트

os.system('cls')
print("\n        ===================================\n\n[!] 지금부터", zname,
      "에 대한 무차별 대입 공격을 진행하겠습니다.\n[!] 오랫동안 찾지 못할 경우 해결이 불가능한 경우이므로 종료하십시오.\n\n        ===================================")
time.sleep(0.5)

password_decrypt = 0  # 암호 변수
decrypt_success = 0  # 성공 여부 변수

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

# 결과 보고 파트

os.system('cls')
if decrypt_success == 1:
    shutil.rmtree(r"temp")  # 압축 해제한 파일 삭제
    print("\n        ===================================\n\n[*] 비밀번호를 찾았습니다.")
    print("[*] 비밀번호는", password_decrypt, "입니다.")
    print("[*] 본 프로그램은 압축 해제를 지원하지 않으므로 타 프로그램을 사용하여 해제하십시오.\n\n        ===================================")
else:
    print("[!] 비정상적 접근입니다.")
