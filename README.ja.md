![head](https://user-images.githubusercontent.com/23215270/70505338-14a48b80-1b6b-11ea-93ed-893ebb52e62a.png)

[한국어](https://github.com/joongiHong/zipker/blob/master/README.md) | [English](https://github.com/joongiHong/zipker/blob/master/README.en.md)
 | [中文](https://github.com/joongiHong/zipker/blob/master/README.zh.md) | [日本語](https://github.com/joongiHong/zipker/blob/master/README.ja.md)
<br/><br/>
暗号がかかった圧縮ファイルに無差別に代入攻撃を試み、パスワードを見つけるプログラムです。<br>
本プロジェクトはパイサンで作成され、ライセンスはMITライセンスです。<br>
詳細は各パーツをご参照ください。

|1. [About](#about)<br>2. [Module](#module)<br>3. [License](https://github.com/joongiHong/zipker/blob/master/LICENSE)<br>4. [Contact](#contact)|
|:---|

# About
本プロジェクトは、暗号のかかった圧縮ファイルに無差別な代入攻撃(BruteForce)を試み、パスワードを探し出すプログラムです。<br>
まだ開発が完了していないので、Zip形式の圧縮ファイルだけをサポートし、速度が遅いです。<br>
最終的に開発が完了した時に使用できる機能は次の通りです。

* 圧縮パスワード検索
* 複数の圧縮ファイルを自動で探す
* Zipのほかにも7z、Alzなどの圧縮形式の支援
* インポート形式サポートで開発が容易
* py 拡張子ではなくexe 拡張子でパイサン米ユーザーも使用可能

# Module
## string(num)
本関数は、大学入学時に使用する文字列を簡単に選択できるようにする関数です。 オプションは1番から7番まであります。

* 1番バス:数字列だけを選択します。
* 2番バス:アルファベットだけを選択します
* 3番バス:トゥクムンだけを選択します。
* 4番バス:数字+アルファベットだけを選択します。
* 5番バス:数字+トゥクムンだけを選択します。
* 6番バス:アルファベット+トゥクムンだけを選択します。
* 7番バス:数字+アルファベット+トゥクムンだけを選択します。

num に代入された番号によって該当する文字列をリストとして返却します。

## zip_file(filename)
本関数は、filenameのzipファイルが存在していることを確認する関数です。 filenameにはファイル名。zip 形式で文字列が挿入されなければなりません。 ファイルが存在する場合には、Trueが存在しない場合は、Falseを返却します。

## zip_password(filename, password)
本関数は、filenameのzipにpasswordを入力して復号する関数です。 代入して一致する場合は、Trueを返還し、一致しない場合は、Falseを返還します。

## zip_decrypt(filename, string, min, max)
本関数は、filename のzip にstring を無差別に代入してパスワードを見つける関数です。 min の場合はパスワードの最小長、max の場合はパスワードの最大長を意味します。 パスワードを見つける場合は、発見されたパスワードを返却し、発見できない場合は、Falseを返却します。

# Contact
本プロジェクトと関連して知りたい点をイシューレポをご利用ください。 もし急な仕事やライセンスに関するお問い合わせの場合は、次のメールをお使いください。
* joongi1978@naver.com
