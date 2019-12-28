![head](https://user-images.githubusercontent.com/23215270/70505338-14a48b80-1b6b-11ea-93ed-893ebb52e62a.png)

[한국어](https://github.com/joongiHong/zipker/blob/master/README.md) | [English](https://github.com/joongiHong/zipker/blob/master/README.en.md)
 | [中文](https://github.com/joongiHong/zipker/blob/master/README.zh.md) | [日本語](https://github.com/joongiHong/zipker/blob/master/README.ja.md)
<br/><br/>
在带有密码的压缩文件中,不分青红皂白地试图对大学进行攻击,找出密码。<br/>
本项目由派森公司制作,授权为GPL 3.0授权。<br/>
详细内容请参考各部分。

|1. [About](#about)<br>2. [Module](#module)<br>3. [License](https://github.com/joongiHong/zipker/blob/master/LICENSE)<br>4. [Contact](#contact)|
|:---|

# About
本项目是密码的,归档中,暴力破解法(BruteForce),找出密码的程序。<br/>
目前开发完毕,形式的压缩文件,Zip支持,速度慢。<br/>
最终完成了开发时可使用的功能如下。

* 压缩密码
* 自动找到多个压缩文件
* Zip 외에도 7z, Alz 등의 압축 형식 지원
* 除了7z、Zip等形式支持压缩Alz
* py 不是扩张者而是exe扩张者,Python美国用户也可以使用

# Module
## string(num)
本市使用的函数代入的选择,简单的函数。 选项1号到7号都有。

* 1号: 只选择数字列。
* 2号: 只选择字母。
* 3号: 只选择特殊文字。
* 4号: 选择数字和字母。
* 5号: 选择数字和特殊文字。
* 6号: 选择字母和特殊文字。
* 7号: 选择数字和字母特殊文字。

根据num中考的号码,将相应的字符列作为列表返还。

## zip_file(filename)
本函数是确认是否存在filename的zip文件的函数。 filename是文件名。需以zip形式插入文字热。 文件存在时,如无True存在,则返还False。

## zip_password(filename, password)
本函数是在filename的zip中输入password进行复弧化的函数。 大学入学并一致时返还True,不一致时返还False。

## zip_decrypt(filename, string, min, max)
本函数是在filename的zip上无差别地输入string来查找密码的函数。 min意味着密码的最小长度,max意味着密码的最大长度。 找出密码时,返还找回的密码,找不到时,返还False。

# Contact
关于本项目,请利用热点回放器对疑问进行解答。 如有急事或有关授权咨询,请使用下列电子邮件:
* joongi1978@naver.com
