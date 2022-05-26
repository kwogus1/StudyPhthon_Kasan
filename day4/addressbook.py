# 주소록 프로그램 
# 여러줄 주석은 ''' ''' 사용
''' 
주소록 프로그램 v1.0
작성일 2022-05-26 09:14
작성자 jh
주소록 프로그램 테스트
'''
import numbers
import os
from re import I # 운영체제 명령용 모듈

# 주소록 클래스
class Contact:
    name = ''; phone_number = ''; e_mail = ''; addr = ''

    # 생성자(contructor)
    def __init__(self, name, phone_number, e_mail, addr) -> None:
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def __str__(self) -> str:
        res_str = f'이름 : {self.name}\n' \
                  f'폰번호 : {self.phone_number}\n' \
                  f'이메일 : {self.e_mail}\n' \
                  f'주소 : {self.addr}'
        return res_str

# 화면 클리어 함수
def clearConsole():
    command = 'clear' # UNIX, LINUX, MACOS
    if os.name in ('nt', 'dos'): # Window
        command = 'cls'

    os.system(command)

# 사용자 정보 입력    
def setContact():
    try:
        (name, phone_number, e_mail, addr) = input('정보입력(이름, 폰번호, 이메일, 주소[구분자/]) : ').split('/')
    
    # print(name, phone_number, e_mail, addr)
    member = Contact(name, phone_number, e_mail, addr)
    return member

# 연락처 리스트 출력 함수 
def printContacts(contacts):
    for item in contacts: # 리스트 원소(Contact 객체)
        print(item)    

# 연락처 삭제 함수
def delContact(contacts, name):
    for i, item in enumerate(contacts):
        if item.isNameExist(name) == True:
            del contacts[i]

# 메뉴출력
def getMenu():
    str_menu = ('주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 프로그램 종료\n')
    print(str_menu)
    menu = input('메뉴선택: ')
    return int(menu)

# 화면 클리어 함수
def clearConsole():
    command = 'clear' # UNIX, LINUX, MACOS
    if os.name in ('nt', 'dos'): # Window
        command = 'cls'

    os.system(command)

# 기본 실행 함수
def run():
    # member = Contact('홍길동', '010-0000-1111', 'hgd76@naver.com', '서울특별시')
    # print(member)
    # setContact()
    contacts = [] # 빈 리스트 변수 초기화
    clearConsole()

    while True : 
        sel_menu = getMenu()
        if sel_menu == 1: # 연락처 추가
            clearConsole()
            member = getContact()
            contacts.append(number) # 연락처 리스트에 새연락처 추가

            input('계속하려면 아무키나 누르세요')
            clearConsole()
        elif sel_menu == 4:
            break
        else:
            clearConsole()

if __name__=='__main__': # EntryPoint(프로그램 시작점)
    print(__name__)
    print('프로그램 시작') # 프로그램이 시작됨
    run()

print('프로그램 종료')