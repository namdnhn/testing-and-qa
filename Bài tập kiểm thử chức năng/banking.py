list_of_client = {
    'donhuhoangnam': 10000000,
    'nguyenthingocminh': 9000000,
    'hothugiang': 8000000,
    'nguyenphuonglinh': 15000000,
    'trinhkieuanh': 14000000,
    'phananhngoc': 19000000
}

def doSomething(id: str, mission: str, money: int):
    if id not in list_of_client:
        print("ID không tồn tại.")
        return
    if mission == 'withdraw':
        if money <= 0:
            print("Số tiền phải lớn hơn 0.")
            return
        if money > list_of_client[id]:
            print("Số dư của bạn không đủ.")
        list_of_client[id] -= money
        print(f"Bạn đã rút thành công {money} VNĐ. Số dư của bạn là {list_of_client[id]}.")
    elif mission == 'deposit':
        if money <= 0:
            print("Số tiền phải lớn hơn 0.")
            return
        else:
            list_of_client[id] += money
            print(f"Bạn đã nạp thành công {money} VNĐ. Số dư của bạn là {list_of_client[id]}.")
    else:
        print("Thao tác không hợp lệ")
    
while(True):
    id = input("Nhập vào id của bạn: ")
    mission = input("Nhập vào thao tác bạn muốn thực hiện: ")
    if mission == 'exit' or mission == 'quit':
        print("Good bye.")
        break
    money = int(input("Nhập vào số tiền mà bạn muốn thao tác: "))
    
    doSomething(id, mission, money)