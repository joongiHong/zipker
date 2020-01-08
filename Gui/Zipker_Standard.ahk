/*
 * * * Compile_AHK SETTINGS BEGIN * * *

[AHK2EXE]
Exe_File=D:\2_개발\Zipker\배포\2.0.1\Zipker_Standard.exe
[VERSION]
Set_Version_Info=1
Company_Name=Joongi Hong (ZERO)
File_Description=Zipker 2.0.1
File_Version=2.0.1.0
Inc_File_Version=0
Legal_Copyright=Copyright 2020. Joongi Hong. All rights reserved.
Original_Filename=Zipker_Standard.exe
Product_Name=Zipker
Product_Version=2.0.1.0
Language_ID=79
[ICONS]
Icon_1=%In_Dir%\theme\icon.ico

* * * Compile_AHK SETTINGS END * * *
*/

; 버전 정보 선언
version := "2.0.1"
password := 0

; 윈도우 버전 확인
IF A_OSVersion in WIN_VISTA,WIN_XP
{
	MsgBox, 16, Zipker %version%, 본 운영체제는 지원되지 않는 운영체제입니다.`n상위 버전으로 업그레이드 후 사용하세요.`n`n[Eoor Code : OS-%A_OSVersion%]
}

; 로딩 전 찌끄레기 삭제
IfExist, result.txt
{
	FileDelete, result.txt
}

IfExist, temp
{
	FileRemoveDir, temp, 1
}

; 로딩 전 이미지
Gui, -caption
Gui, Add, Picture, x-7 y-2 w393 h240 , theme\loading.jpg
Gui, Show, w388 h236, Zipker %version%

; 파일 선택
FileSelectFile, zipurl, 1,,, 압축 파일 (*.zip)
if zipurl =
{
	MsgBox, 0, Zipker %version%, 파일 선택이 취소되었습니다.`n동종 에러가 반복될 경우 블로그로 연락해 주세요.`n`n[Error Code : F-001]
	ExitApp
}

Gui, Destroy
Gui, -caption
Gui, Color, 444444
Gui, Add, Picture, x420 y-2 w38 h38 gexit, theme\exit.png
Gui, Font, S18 cFFFFFF Bold, 맑은 고딕 ; 제목 폰트 설정
Gui, Add, Text, x107 y36 w259 h28 , 대입할 문자열의 옵션을
Gui, Add, Text, x155 y74 w163 h28 , 선택해 주세요.
Gui, Font, S8 cFFFFFF Bold, 맑은 고딕 ; 그외 폰트 설정
Gui, Add, CheckBox, x69 y151 w96 h28 vuser_num, 숫자
Gui, Add, CheckBox, x69 y189 w96 h28 vuser_alpha, 알파벳
Gui, Add, CheckBox, x69 y228 w96 h28 vuser_special, 특수문자
Gui, Add, GroupBox, x40 y122 w153 h163 , 문자열 옵션
Gui, Add, GroupBox, x232 y122 w192 h163 , 문자열 길이
Gui, Add, Text, x252 y151 w57 h19 , 최대 길이
Gui, Add, Text, x252 y218 w57 h19 , 최소 길이
Gui, Add, Picture, x150 y300 w150 h50 gfind, theme\find.png
Gui, Font, S8 c000000 Bold, 맑은 고딕 ; 텍박 폰트 설정
Gui, Add, Edit, Number x252 y180 w153 h19 vuser_max, ; 최대 길이
Gui, Add, Edit, Number x252 y247 w153 h19 vuser_min, ; 최소 길이
OnMessage(0x201, "WM_LBUTTONDOWN")
Gui, Show, w460 h370, Zipker %version%
return

WM_LBUTTONDOWN(wParam, IParam)
{
	PostMessage, 0xA1, 2,,, A
	return
}

find:
Gui, Submit, Nohide
If user_num = 1
{
	If user_alpha = 1
	{
		If user_special = 1
		{
			user_string = 7
		}
		else 
		{
			user_string = 4
		}
	}
	else if user_special = 1 
	{
		user_string = 5
	}
	else
	{
		user_string = 1
	}
}
else if user_alpha = 1
{
	If user_special = 1 
	{
		user_string = 6
	}
	else
	{
		user_string = 2
	}
}
else 
{
	user_string = 3
}

user := zipurl . ";" . user_string . ";" . user_min . ";" . user_max

run, engine.exe
Sleep, 500
Send, %user%
Sleep, 600
Send, {enter}
Sleep, 300
WinMinimize, %A_ScriptDir%\engine.exe

goto, findchang
return

findchang:
Gui, Submit, Nohide
Gui, Destroy
Gui, -caption
Gui, Color, 444444
Gui, Add, Picture, x-5 y-2 w364 h297 , theme\finding.png
Gui, Add, Picture, x325 y-2 w38 h38 gexit2, theme\exit.png
Gui, Show, w360 h296, Zipker %version%

loop {
	IfExist, result.txt
	{
		sleep, 1000
		break
	}
}

FileRead, password, result.txt
goto, wait

return

wait:
Gui, Submit, Nohide
if password = 1
{
	MsgBox, 16, Zipker %version%, 파일을 찾지 못하였습니다.`n파일이 올바른 압축파일인지 확인하십시오.`n`n[E-001]
	ExitApp
}
if password = 2
{
	TrayTip, Zipker %version%, 암호를 찾지 못하였습니다.`n자세한 내용은 Zipker에서 확인하세요.,,35
	MsgBox, 16, Zipker %version%, 암호를 찾지 못하였습니다.`n문자열 설정이 올바른지 확인하십시오.`n`n[E-002]
	ExitApp
}

goto, End

End:
TrayTip, Zipker %version%, 암호를 찾았습니다.`n자세한 내용은 Zipker에서 확인하세요.,,33

Gui, Submit, Nohide
Gui, Destroy
Gui, -caption
Gui, Color, 444444
Gui, Add, Picture, x420 y-2 w38 h38 gexit, theme\exit.png
Gui, Font, S18 cFFFFFF Bold, 맑은 고딕 ; 제목 폰트 설정
Gui, Add, Text, x107 y50 w259 h28 +center, 찾아낸 비밀번호
Gui, Font, S35 cFFFFFF Bold, 맑은 고딕 ; 그외 폰트 설정
Gui, Add, Text, x130 y130 w210 +center, %password%
Gui, Font, S9 cFFFFFF Bold, 맑은 고딕 ; 안내 멘트
Gui, Add, Text, x110 y230 +center, 본 프로그램을 압축 해제를 지원하지 않습니다
Gui, Add, Text, x100 y250 +center, 반디집 등 타사 프로그램으로 해제하시기 바랍니다.
OnMessage(0x201, "WM_LBUTTONDOWN")
Gui, Show, w460 h370, Zipker %version%
return

exit2:
MsgBox, 52, Zipker %version%, 정말로 취소하시겠습니까?`n취소하실 경우 처음부터 다시 시도하여야 합니다.
IfMsgBox, Yes
{
	run, taskkill -f -im engine.exe
	goto, exit
}
goto, findchang
return

exit:
ExitApp
