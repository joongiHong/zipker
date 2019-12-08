import zipfile

zname = input("압축 파일의 파일명을 입력하십시오.")
is_zname = zipfile.is_zipfile(zname)

if is_zname == True:
    print('압축 파일이 존재합니다.')
else:
    print('압축 파일이 존재하지 않습니다.')
