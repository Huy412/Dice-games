import random
import time
import datetime
from colorama import Fore, Style
min_val = 1
max_val = 6
x = datetime.datetime.now()
print(x.strftime(Fore.GREEN + "%I:%M %p\n%A, %d %B, %Y"))
print(Style.RESET_ALL)
while True:
    roll_again = input("Muốn tung xúc xắc không ? (yes / no):").lower()

    if roll_again not in ("yes", "no"):
        print("Chọn lại đi bạn 🤣")
    elif roll_again in "no":
        user_name = input(Fore.LIGHTMAGENTA_EX + "Bạn đặt tên người dùng là: ")
        e_star = input(Fore.RED + "Bạn đánh giá bao nhiêu sao ? (1-5) :")
        if e_star not in ("1", "2", "3", "4", "5"):
           print("Tạm biệt và hẹn gặp lại! 😥")
           time.sleep(1)
           break
        else:
           with open("tek4vn.txt", 'a', encoding='utf-8') as file:
                file.write(user_name)
                file.write(":")
                file.write(e_star)
                file.write("\n")
           print(Fore.LIGHTBLUE_EX + "Cảm ơn bạn đã đánh giá 💖💖")
           break
    else:
        print("Đang tung xúc xắc.....")
        time.sleep(2)
        print("Loading......🤖")
        time.sleep(2)
        print(Fore.CYAN + "Con số may mắn là :")
        vl_e = random.randint(min_val, max_val)
        vl_d = random.randint(min_val, max_val)
        print(vl_e, "và", vl_d)
        print(Style.RESET_ALL)
        if vl_e == 6 or vl_d == 6:
            print(Fore.YELLOW + "Hooray!! 🎉")
            print(Style.RESET_ALL)
        else:
            print("Chúc bạn may mắn lần sau :)))")
        c = vl_e + vl_d
        print("Tổng giá trị là :", c)
        time.sleep(1)
