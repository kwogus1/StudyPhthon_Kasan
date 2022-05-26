class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.__name = name
        self.__phone_number = phone_number
        self.__e_mail = e_mail
        self.__addr = addr

    def __str__(self) -> str:
        str_res = (f'이  름: {self.__name}\n'
                   f'핸드폰: {self.__phone_number}\n'
                   f'이메일: {self.__e_mail}\n'
                   f'주  소: {self.__addr}')
        return str_res
       
def set_contact():
    (name, phone_number, e_mail, addr) = input('정보입력(이름, 폰번호, 이메일, 주소[구분자/]) : ').split('/')
    print(name, phone_number, e_mail, addr)

def get_menu():
    str_menu = ('주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)
    menu = input('메뉴입력: ')
    return int(menu)


def run():
    # first = Contact('홍길동', '010-0000-1111', 'hgd76@naver.com', '서울특별시')
    # print(first)
    setContact()

if __name__=='__main__': # EntryPoint(프로그램 시작점)
    print(__name__)
    print('프로그램 시작') # 프로그램이 시작됨
    run()


