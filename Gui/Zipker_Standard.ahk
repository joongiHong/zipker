/*
 * * * Compile_AHK SETTINGS BEGIN * * *

[AHK2EXE]
Exe_File=D:\2_����\Zipker\����\2.0.1\Zipker_Standard.exe
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

; ���� ���� ����
version := "2.0.1"
password := 0

; ������ ���� Ȯ��
IF A_OSVersion in WIN_VISTA,WIN_XP
{
	MsgBox, 16, Zipker %version%, �� �ü���� �������� �ʴ� �ü���Դϴ�.`n���� �������� ���׷��̵� �� ����ϼ���.`n`n[Eoor Code : OS-%A_OSVersion%]
}

; �ε� �� ������� ����
IfExist, result.txt
{
	FileDelete, result.txt
}

IfExist, temp
{
	FileRemoveDir, temp, 1
}

; �ε� �� �̹���
Gui, -caption
Gui, Add, Picture, x-7 y-2 w393 h240 , theme\loading.jpg
Gui, Show, w388 h236, Zipker %version%

; ���� ����
FileSelectFile, zipurl, 1,,, ���� ���� (*.zip)
if zipurl =
{
	MsgBox, 0, Zipker %version%, ���� ������ ��ҵǾ����ϴ�.`n���� ������ �ݺ��� ��� ��α׷� ������ �ּ���.`n`n[Error Code : F-001]
	ExitApp
}

Gui, Destroy
Gui, -caption
Gui, Color, 444444
Gui, Add, Picture, x420 y-2 w38 h38 gexit, theme\exit.png
Gui, Font, S18 cFFFFFF Bold, ���� ��� ; ���� ��Ʈ ����
Gui, Add, Text, x107 y36 w259 h28 , ������ ���ڿ��� �ɼ���
Gui, Add, Text, x155 y74 w163 h28 , ������ �ּ���.
Gui, Font, S8 cFFFFFF Bold, ���� ��� ; �׿� ��Ʈ ����
Gui, Add, CheckBox, x69 y151 w96 h28 vuser_num, ����
Gui, Add, CheckBox, x69 y189 w96 h28 vuser_alpha, ���ĺ�
Gui, Add, CheckBox, x69 y228 w96 h28 vuser_special, Ư������
Gui, Add, GroupBox, x40 y122 w153 h163 , ���ڿ� �ɼ�
Gui, Add, GroupBox, x232 y122 w192 h163 , ���ڿ� ����
Gui, Add, Text, x252 y151 w57 h19 , �ִ� ����
Gui, Add, Text, x252 y218 w57 h19 , �ּ� ����
Gui, Add, Picture, x150 y300 w150 h50 gfind, theme\find.png
Gui, Font, S8 c000000 Bold, ���� ��� ; �ع� ��Ʈ ����
Gui, Add, Edit, Number x252 y180 w153 h19 vuser_max, ; �ִ� ����
Gui, Add, Edit, Number x252 y247 w153 h19 vuser_min, ; �ּ� ����
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
	MsgBox, 16, Zipker %version%, ������ ã�� ���Ͽ����ϴ�.`n������ �ùٸ� ������������ Ȯ���Ͻʽÿ�.`n`n[E-001]
	ExitApp
}
if password = 2
{
	TrayTip, Zipker %version%, ��ȣ�� ã�� ���Ͽ����ϴ�.`n�ڼ��� ������ Zipker���� Ȯ���ϼ���.,,35
	MsgBox, 16, Zipker %version%, ��ȣ�� ã�� ���Ͽ����ϴ�.`n���ڿ� ������ �ùٸ��� Ȯ���Ͻʽÿ�.`n`n[E-002]
	ExitApp
}

goto, End

End:
TrayTip, Zipker %version%, ��ȣ�� ã�ҽ��ϴ�.`n�ڼ��� ������ Zipker���� Ȯ���ϼ���.,,33

Gui, Submit, Nohide
Gui, Destroy
Gui, -caption
Gui, Color, 444444
Gui, Add, Picture, x420 y-2 w38 h38 gexit, theme\exit.png
Gui, Font, S18 cFFFFFF Bold, ���� ��� ; ���� ��Ʈ ����
Gui, Add, Text, x107 y50 w259 h28 +center, ã�Ƴ� ��й�ȣ
Gui, Font, S35 cFFFFFF Bold, ���� ��� ; �׿� ��Ʈ ����
Gui, Add, Text, x130 y130 w210 +center, %password%
Gui, Font, S9 cFFFFFF Bold, ���� ��� ; �ȳ� ��Ʈ
Gui, Add, Text, x110 y230 +center, �� ���α׷��� ���� ������ �������� �ʽ��ϴ�
Gui, Add, Text, x100 y250 +center, �ݵ��� �� Ÿ�� ���α׷����� �����Ͻñ� �ٶ��ϴ�.
OnMessage(0x201, "WM_LBUTTONDOWN")
Gui, Show, w460 h370, Zipker %version%
return

exit2:
MsgBox, 52, Zipker %version%, ������ ����Ͻðڽ��ϱ�?`n����Ͻ� ��� ó������ �ٽ� �õ��Ͽ��� �մϴ�.
IfMsgBox, Yes
{
	run, taskkill -f -im engine.exe
	goto, exit
}
goto, findchang
return

exit:
ExitApp
