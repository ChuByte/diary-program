# 다이어리 프로그램
## 날짜를 입력하고, 일기를 작성
## 날짜를 입력하고 작성된 일기를 출력
### dd-mm-yyyy.txt

def menu():
    print("1. 오늘 하루 기억하기 ")
    print("2. 추억 불러오기 ")
    print("3. 일기장 덮기 ")
    choice = int(input("원하는 행동의 숫자를 입력해주세요 ⭐️ "))

    if choice == 1:
        write_diary()
    elif choice ==2:
        read_diary()
    elif choice ==3:
        return 1

def write_diary():
    date = input("🎀 날짜를 입력하세요 (dd-mm-yyyy) : ")
    text = input("🎀 오늘 하루는 어땠나요 ? ")

    with open(f"{date}.txt","w") as file :
        file.write(text)
        print(" 🌈 일기를 저장해 놓을게요 🌈 ")

def read_diary():
    date = input("🎀 돌아보고 싶은 날짜를 입력하세요 (dd-mm-yyyy) : ")

    with open(f"{date}.txt","r") as file:
        print(file.read())

while True:
    if menu():
        break