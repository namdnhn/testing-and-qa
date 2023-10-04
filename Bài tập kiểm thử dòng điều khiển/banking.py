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
        return "ID không tồn tại."
    if mission == 'withdraw':
        if money <= 0:
            return "Số tiền phải lớn hơn 0."
        if money > list_of_client[id]:
            return "Số dư của bạn không đủ."
        list_of_client[id] -= money
        return f"Bạn đã rút thành công {money} VNĐ. Số dư của bạn là {list_of_client[id]} VNĐ."
    elif mission == 'deposit':
        if money <= 0:
            return "Số tiền phải lớn hơn 0."
        else:
            list_of_client[id] += money
            return f"Bạn đã nạp thành công {money} VNĐ. Số dư của bạn là {list_of_client[id]} VNĐ."
    else:
        return "Thao tác không hợp lệ"
    
if __name__ == '__main__':
    while(True):
        id = input("Nhập vào id của bạn: ")
        mission = input("Nhập vào thao tác bạn muốn thực hiện: ")
        if mission == 'exit' or 'quit':
            print("Good bye.")
            break
        money = int(input("Nhập vào số tiền mà bạn muốn thao tác: "))
        
        doSomething(id, mission, money)