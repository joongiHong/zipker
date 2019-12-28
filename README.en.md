![head](https://user-images.githubusercontent.com/23215270/70505338-14a48b80-1b6b-11ea-93ed-893ebb52e62a.png)

[한국어](https://github.com/joongiHong/zipker/blob/master/README.md) | [English](https://github.com/joongiHong/zipker/blob/master/README.en.md)
 | [中文](https://github.com/joongiHong/zipker/blob/master/README.zh.md) | [日本語](https://github.com/joongiHong/zipker/blob/master/README.ja.md)
<br/><br/>
This project uses a BruteForce to find the password of zip file.<br>
This project's language is Python. and License is GNU GPL 3.0

|1. [About](#about)<br>2. [Module](#module)<br>3. [License](https://github.com/joongiHong/zipker/blob/master/LICENSE)<br>4. [Contact](#contact)|
|:---|

# About
This project uses a BruteForce to find the password of zip file<br>
The functions of this project are as follows:

* Find a password
* Find a password of many Zipfiles
* Any others file support
* Available as a module
* Python Non-User Available

# Module
## string(num)
This function is a function that makes it easy to select the string used for college entrance. Options are available from 1 to 7.

* 1번 : Only number
* 2번 : Only alphabet
* 3번 : Only special character
* 4번 : number + alphabet
* 5번 : number + special character
* 6번 : alphabet + special character
* 7번 : number + alphabet + special character

Returns the corresponding string as a list based on the number entered in the num.

## zip_file(filename)
This function is a function that verifies that a zip file in the filename. The filename contains the file name.String must be inserted in zip format. Returns False if the file does not exist.

## zip_password(filename, password)
This function is a function that is encoded by entering a password in the zip of the filename. Returns True if a match is made and False if it does not match.

## zip_decrypt(filename, string, min, max)
This function is a function to find a password by randomly substituting a string in the zip of the filename. Minimum length of password for min and maximum length for max. Returns the password you found, or False if you don't find it.

# Contact
Please use the Issue Reporter to ask questions regarding this project. If you are in an emergency or if you have a license inquiry, please use the following e-mail:
* joongi1978@naver.com
