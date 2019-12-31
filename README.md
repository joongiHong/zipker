![head](https://user-images.githubusercontent.com/23215270/70505338-14a48b80-1b6b-11ea-93ed-893ebb52e62a.png)

<br/><br/>
암호가 걸린 압축파일에 무차별 대입 공격을 시도하여 비밀번호를 찾아내는 프로그램입니다.<br>
본 프로젝트는 파이썬으로 작성되었으며 라이선스는 GPL 3.0 입니다.<br>
자세한 내용은 각 파트를 참고하십시오.

|1. [About](#about)<br>2. [Module](#module)<br>3. [License](https://github.com/joongiHong/zipker/blob/master/LICENSE)<br>4. [Contact](#contact)|
|:---|

# About
본 프로젝트는 암호가 걸린 압축파일에 무차별 대입 공격(브루트 포스)를 시도하여 비밀번호를 찾아내는 프로그램입니다.<br>
아직은 개발이 완료되지 않아 Zip 형식의 압축파일만 지원하며 속도가 느립니다.<br>
최종적으로 개발이 완료되었을 때 사용가능할 기능은 다음과 같습니다.

* 압축 비밀번호 찾기
* 여러개의 압축파일 자동으로 찾기
* Zip 외에도 7z, Alz 등의 압축 형식 지원
* Import 형식 지원으로 개발 용이
* py 확장자가 아닌 exe 확장자로 파이썬 미 사용자도 사용가능

# Module
## string(num)
본 함수는 대입 시 사용하는 문자열을 손쉽게 선택할 수 있도록 하는 함수입니다. 옵션은 1번부터 7번까지 있습니다.

* 1번 : 숫자열만 선택합니다.
* 2번 : 알파벳만 선택합니다
* 3번 : 특문만 선택합니다.
* 4번 : 숫자 + 알파벳만 선택합니다.
* 5번 : 숫자 + 특문만 선택합니다.
* 6번 : 알파벳 + 특문만 선택합니다.
* 7번 : 숫자 + 알파벳 + 특문만 선택합니다.

num에 대입된 번호에 따라 해당되는 문자열을 리스트로서 반환합니다.

## zip_file(filename)
본 함수는 filename의 zip 파일이 존재하는지 확인하는 함수입니다. filename에는 파일명.zip 형식으로 문자열이 삽입되어야 합니다. 파일이 존재할 경우에는 True를 존재하지 않을 경우에는 False를 반환합니다.

## zip_password(filename, password)
본 함수는 filename의 zip에 password를 입력하여 복호화하는 함수입니다. 대입하여 일치할 경우에는 True를 반환하고 일치하지 않을 경우에는 False를 반환합니다.

## zip_decrypt(filename, string, min, max)
본 함수는 filename의 zip에 string을 무차별 대입하여 비밀번호를 찾아내는 함수입니다. min의 경우에는 비밀번호의 최소 길이, max의 경우에는 비밀번호의 최대 길이를 의미합니다. 비밀번호를 찾아낼 경우에는 찾아낸 비밀번호를 반환하며 찾아내지 못할 경우 False를 반환합니다.

# Contact
본 프로젝트와 관련하여 궁금한 점을 이슈 리포터를 이용하여 주십시오. 만약 급한 일이나 라이선스 관련 문의일 경우 다음 이메일을 사용해 주십시오.
* joongi1978@naver.com
