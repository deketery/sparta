# 다음과 같은 메뉴가 있다고 가정하자
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# Enter number:

# 위에서 1번을 입력하면  "1번을 입력하셨습니다." 라고 출력하고 다시 메뉴를 보여준다.
# 위에서 2번을 입력하면  "2번을 입력하셨습니다." 라고 출력하고 다시 메뉴를 보여준다.
# 위에서 3번을 입력하면 "3번을 입력하셨습니다." 라고 출력하고 다시 메뉴를 보여준다.
# 위에서 4번을 입력하면 "프로그램을 종료합니다." 라고 출력하고, 프로그램을 종료한다.
# 만약 1~4번 이외의 메뉴를 입력하면 "선택한번호는 없는 메뉴입니다."라고 출력하고
# 다시 메뉴를 보여준다.

menu = "1. Add\n2. Del\n3. List\n4. Quit\nEnter number:"

num = int(input(menu))
while num != 4:
    if num ==1:
        print(f'{num}번을 입력하셨습니다.\n')
        num = int(input(menu))
    elif num==2:
        print(f'{num}번을 입력하셨습니다.\n')
        num = int(input(menu))
    elif num==3:
        print(f'{num}번을 입력하셨습니다.\n')
        num = int(input(menu))
    else:
        print("선택한 번호는 없는 메뉴입니다.\n")
        num = int(input(menu))
print("프로그램을 종료합니다.")
