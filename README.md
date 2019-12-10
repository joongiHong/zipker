![head](https://user-images.githubusercontent.com/23215270/70505338-14a48b80-1b6b-11ea-93ed-893ebb52e62a.png)

암호가 걸린 압축파일에 무차별 대입 공격을 시도하여 비밀번호를 찾아내는 프로그램입니다.<br>
본 프로젝트는 파이썬으로 작성되었으며 라이선스는 MIT 라이선스 입니다.<br>
자세한 내용은 각 파트를 참고하십시오.

|1. [About](#about)<br>2. [How](#how)<br>3. [FAQ](#faq)<br>4. [License](#license)<br>5. [Contact](#contact)|
|---|

# About
본 프로젝트는 암호가 걸린 압축파일에 무차별 대입 공격(브루트 포스)를 시도하여 비밀번호를 찾아내는 프로그램입니다.<br>
아직은 개발이 완료되지 않아 Zip 형식의 압축파일만 지원하며 속도가 느립니다.<br>
최종적으로 개발이 완료되었을 때 사용가능할 기능은 다음과 같습니다.

* 압축 비밀번호 찾기
* 여러개의 압축파일 자동으로 찾기
* Zip 외에도 7z, Alz 등의 압축 형식 
* Import 형식 지원으로 개발 용이
* py 확장자가 아닌 exe 확장자로 파이썬 미 사용자도 사용가능

# How
* **1. Zipker.py 다운로드**<br>
깃허브 페이지에서 Zipker.py를 다운로드 합니다.<br>

* **2. Zipker.py 세팅**<br>
다운받은 Zipker.py 파일을 비밀번호를 찾을 파일과 같은 위치에 둡니다. 그뒤 해당 폴더에서 Shift 키와 오른쪽 마우스를 누릅니다. 누른 뒤 뜬 창에서 '여기에 PowerShell 창 열기'를 클릭합니다.<br>

* **3. Zipker.py 실행**<br>
열린 파워셀 창에 'python Zipker.py'를 입력합니다. 정상적으로 실행되면 표시되는 절차에 따라 사용합니다. 만일 실행되지 않는다면 **3번 문단 FAQ**를 참고하세요.

# FAQ
### Q. Zipker.py가 실행되지 않습니다.
**2번 문단 How** 2, 3 지침에 따라 진행하였음에도 ''python'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.' 라고 표시되며 실행되지 않을 경우에는 python이 설치가 되지 않았거나 python이 환경변수에 등록되지 않을 것입니다. 자세한 것은 구글에 검색하세요.

### Q. 파일을 찾지 못하였다고 합니다. (F-1 에러)
프로그램의 질의에 따라 압축 파일 이름을 입력하였음에도 찾지 못하였다며 F-1 에러를 발생시키는 경우에는 두가지 이유가 있습니다. 첫번째 이유는 입력시 철자가 틀렸거나 마지막에 .zip 등의 확장자를 입력하지 않은 것입니다. 두번째 이유는 Zipker.py 파일과 해당 압축파일이 동일 디렉토리에 존재하지 않는 것입니다. 디렉토리로 이동 후 실행시켜 주십시오.

# License 
본 프로젝트의 라이선스는 MIT License 입니다.<br>
라이선스에 관한 허가서는 다음과 같습니다.

### MIT License
Copyright (c) 2019 Joongi Hong (Project Dotory)<br>

Permission is hereby granted, free of charge, to any person obtaining a copy<br>
of this software and associated documentation files (the "Software"), to deal<br>
in the Software without restriction, including without limitation the rights<br>
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell<br>
copies of the Software, and to permit persons to whom the Software is<br>
furnished to do so, subject to the following conditions:<br>
<br>
The above copyright notice and this permission notice shall be included in all<br>
copies or substantial portions of the Software.<br>
<br>
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR<br>
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,<br>
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE<br>
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER<br>
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,<br>
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE<br>
SOFTWARE.

### MIT 허가서 (한국 번역)
모든 권리는 Joongi Hong (Project Dotory)에게 귀속됨.<br>
<br>
이 문서에 기하여, 이 소프트웨어와, 이와 관련된 모든 문서(이하 '소프트웨어'라 한다)의<br>
복제본을 보유하게 되는 모든 사용자에 대하여, 다음 권한이 무상 허가된다.<br>
소프트웨어의 사용, 복제, 변경, 통합, 발행, 배포, 재실시, 판매에 대한 제약을 포함한 <br>
어떠한 제약 없이 본 소프트웨어를 취급할 수 있으며, <br>
이는 제3자에 대한 소프트웨어 지급시에도 동일하게 적용된다.<br>
단, 이 모든 사항은 아래의 조건하에 적용된다.<br>
<br>
위 저작권 표시와 본 허가조항은 소프트웨어의 모든 복제본 혹은 중요한 부분에 포함되어야 한다.<br>
<br>
소프트웨어는 "있는 그대로" 제공된다. 판매적격성, 특정 용도에 대한 적합성, 준법성, <br>
혹은 그 이상의 범위를 포함한 사항에 있어서, 명시적 혹은 암시적인 어떠한 보증도 하지 않는다.<br>
계약, 불법행위등의 과정상의 개입여부에 상관없이 어떠한 상황에서도, 본 소프트웨어의 저작자 혹은 저작권자는, <br>
소프트웨어에서 혹은 소프트웨어와 연관되어 발생하는, 또한 사용과정중 혹은 기타 거래도중 발생하는<br>
어떠한 소유권 청구, 피해, 혹은 기타 다른 법적 책임에 대해서도 책임을 지지 아니한다.<br>
<br>
본 MIT 허가서 (한국 번역) MIT License의 한국어 번역 버전으로 원본과 완벽하게 일치함을 보장하지 아니한다.<br>
본 허가서는 저작권자 혹은 복제본을 보유하게 되는 모든 사용자가 쉽게 이해할 수 있도록 돕기위한 것이다.<br>
본 허가서는 법적 효력이 존재하지 아니하며, 법적 효력은 원문인 MIT License만이 해당된다.<br>
<br>
<br>
라이선스와 관련한 자세한 내용은 동 프로젝트의 [LICENSE 파일](https://github.com/joongiHong/zipker/blob/master/LICENSE)을 참고하세요.<br>

# Contact
본 프로젝트와 관련하여 궁금한 점을 이슈 리포터를 이용하여 주십시오. 만약 급한 일이나 라이선스 관련 문의일 경우 다음 이메일을 사용해 주십시오.
* joongi1978@naver.com
