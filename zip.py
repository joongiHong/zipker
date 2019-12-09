# 임포트 파트
import zipfile
import sys
import shutil

# ZIP 정보 수집 파트
# 압축파일 이름을 zname으로 받음
zname = input(
    "===================================\n\n[?] 비밀번호를 찾을 압축파일의 이름을 입력하세요.\n\n===================================\n>>> ")
is_zname = zipfile.is_zipfile(zname)  # 파일 유무를 True와 False로 저장함
zfile = zipfile.ZipFile(zname)  # 추후 사용할 zfile 지정

if is_zname != True:
    print('[!] 입력하신', zname, '압축파일이 존재하지 않습니다.')  # 파일 미존재
    sys.exit

# 해제 함수 선언 파트


def zip_decrypt(password):
    zfile.extractall(path='temp', pwd=password.encode())


# 무차별 대입 시도 파트

print("\n\n===================================\n\n[!] 지금부터", zname,
      "에 대한 무차별 대입 공격을 진행하겠습니다.\n[!] 오랫동안 찾지 못할 경우 해결이 불가능한 경우이므로 종료하십시오.\n\n===================================")

password_decrypt = 0  # 암호 변수
decrypt_success = 0  # 성공 여부 변수

while decrypt_success != 1:
    try:
        zip_decrypt(str(password_decrypt))
        decrypt_success = 1
    except:
        password_decrypt = password_decrypt + 1
        pass

# 결과 보고 파트

if decrypt_success == 1:
    shutil.rmtree(r"temp")  # 압축 해제한 파일 삭제
    print("\n\n===================================\n\n[*] 비밀번호를 찾았습니다.")
    print("[*] 비밀번호는", password_decrypt, "입니다.")
    print("[*] 본 프로그램은 압축 해제를 지원하지 않으므로 타 프로그램을 사용하여 해제하십시오.\n\n===================================")
else:
    print("[!] 비정상적 접근입니다.")
