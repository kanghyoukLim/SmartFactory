"""
###############################################################################
# 파일의 경로 다루기
###############################################################################
import os

cwd = os.getcwd()                   # get current working directory
flist = os.listdir(cwd)             # 현재폴더의 폴더 및 파일 리스트
'Ex02_Path.py' in flist             # True/False
os.path.exists('Ex02_Path.py')      # 파일/폴더의 존재여부 확인

os.chdir('..')                      # change directory
os.chdir('Literacy2023')

fullfname = os.path.join(cwd, 'Ex02_Path.py')   # OS에 맞춰 파일경로를 만들어 줌

os.path.dirname(fullfname)                      # Directory만 얻기
os.path.basename(fullfname)                     # Filename만 얻기
path, fname = os.path.split(fullfname)          # Directory, Filename 각각 얻기

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # 현재파일의 경로 구하기

###############################################################################
# 텍스트 파일 불러오기
###############################################################################
import os

# 다양한 파일경로 설정방법
fname = os.path.join(os.getcwd(), 'hello.txt')
fname = 'D:\\52-Python\\Literacy2023\\hello.txt'
fname = r'D:\52-Python\Literacy2023\hello.txt'
fname = 'D:/52-Python/Literacy2023/hello.txt'
# fname = os.path.join(os.getcwd(), '인사말.txt')


# 파일객체 생성: r,w,a/t,b
f = open(fname, 'rt', encoding='utf-8')
f.encoding      # 기본 인코딩방식 : 'cp949'

# 파일 읽기
contents = f.read()             # 방법1 : 한꺼번에 읽기 - read(n) : n문자
print(contents)

lines = f.readlines()           # 방법2 : 모든 라인을 리스트로 반환
print(lines)
f.seek(0)                       # 파일포인터 이동 (byte 단위)
f.tell()                        # 파일포인터 위치 반환
for line in lines:              # 한 라인씩 순회하며 읽음
    print(line, end='')

while True:
    line = f.readline()         # 방법3 : 한 라인씩 읽기
    if not line:
        break
    print(line, end='')

# 파일객체를 닫음
f.close()

###############################################################################
# 텍스트 파일 저장하기
###############################################################################
import os


# 파일 출력
f = open('D:\\12-Python\\Lecture\\filewrite.txt', 'wt', encoding='utf-8')

f.write('write 사용\n첫째 줄\n둘째 줄\n셋째 줄\n')     # 글자수 반환: 24
f.flush()

lines = ['writelines 사용\n', '첫째 줄\n', '둘째 줄\n', '셋째 줄\n']
f.writelines(lines)
f.close()

# 파일 컨텍스트를 이용한 편의문법 : 코딩이 줄고, 자동 close
fname = os.path.join(os.getcwd(), '인사말.txt')
with open(fname, 'r', encoding='utf-8') as f:
    contents = f.read()
print(contents)

"""
###############################################################################
# (실습2) 텍스트 파일 불러오기
###############################################################################
import os


# 다양한 파일경로 설정방법
fname = os.path.join(os.getcwd(), 'Ex01_HowtoEdit.py')
fname = 'D:\\52-Python\\Literacy2023\\Ex01_HowtoEdit.py'
fname = r'D:\52-Python\Literacy2023\Ex01_HowtoEdit.py'
fname = 'D:/52-Python/Literacy2023/Ex01_HowtoEdit.py'

# 파일객체 생성: r,w,a/t,b
f = open(fname, 'rt', encoding='utf-8')
f.encoding      # 기본 인코딩방식 : 'cp949'

# 파일 읽기
contents = f.read()             # 방법1 : 한꺼번에 읽기 - read(n) : n문자
print(contents)

f.tell()                        # 파일포인터 위치 반환: 1890
f.seek(0)                       # 파일포인터 이동 (byte 단위)
lines = f.readlines()           # 방법2 : 모든 라인을 리스트로 반환
print(lines)
for line in lines:              # 한 라인씩 순회하며 읽음
    print(line, end='')

f.seek(0)
while True:
    line = f.readline()         # 방법3 : 한 라인씩 읽기
    if not line:
        break
    print(line, end='')

with open(fname, 'r', encoding='utf-8') as f:
    data = f.read()
print(data)

# 파일객체를 닫음
f.close()
