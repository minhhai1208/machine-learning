def fun_one(num):
    i = 0
    while(i<len(num)):
        if(num[i]%10==0):
            del num[i]
        else:
            i += 1

def fun_two(num):
    i = 0
    while (i < len(num)):
        if (num[i] % 11 == 0):
            del num[i]
        else:
            i += 1


def fun_three(num):
    condition = int(input("Nhập vào số: "))
    i = 0
    while (i < len(num)):
        if (num[i] % 10 == condition):
            del num[i]
        else:
            i += 1

def fun_four(num):
    print("Lấy hay bỏ ?")
    condition = input("Lựa chọn: ")
    if condition == "lay":
        print("Chẵn hay lẻ ?")
        condition1 = input("Lựa chọn: ")
        if condition1 == "chan":
            i = 0
            while (i < len(num)):
                if (num[i] % 2 != 0):
                    del num[i]
                else:
                    i += 1
        else:
            i = 0
            while (i < len(num)):
                if (num[i] % 2 == 0):
                    del num[i]
                else:
                    i += 1
    else:
        print("Chẵn hay lẻ ?")
        condition1 = input("Lựa chọn: ")
        if condition1 == "chan" :
            i = 0
            while (i < len(num)):
                if (num[i] % 2 == 0):
                    del num[i]
                else:
                    i += 1
        else:
            i = 0
            while (i < len(num)):
                if (num[i] % 2 != 0):
                    del num[i]
                else:
                    i += 1

def fun_five(num):
    for i in num:
        print(i,end=" ")
    print()

def fun_six(num):
    con_num = int(input("Nhập vào số: "))
    i = 0
    while(i<len(num)):
        if(num[i] // 10 == con_num ):
            del num[i]
        else:
            i += 1

first_number = int(input("Nhập vào số bắt đầu: "))
last_number = int(input("Nhập váo số kết thúc: "))

numbers = []
for i in range(first_number,last_number+1):
    numbers.append(i)

functions = [fun_one, fun_two, fun_three, fun_four, fun_five, fun_six]
con_num = 1
while con_num != 9:
    print("0/Bỏ chục")
    print("1/Bỏ cặp")
    print("2/Bỏ đuôi")
    print("3/Lấy hoặc bỏ chẵn lẻ")
    print("4/In ra kết quả")
    print("5/Bỏ hàng chục")
    print("9/Kết thúc")
    con_num = int(input("Nhập lựa chọn: "))
    if con_num == 9:
        continue
    else:
        functions[con_num](numbers)

for i in numbers:
    print(i,end=" ")



