def truy_cap_phan_tu(tuple_data):
    # Truy cập phần tử đầu tiên
    first_element = tuple_data[0]
    
    # Truy cập phần tử cuối cùng
    last_element = tuple_data[-1]
    return first_element, last_element

# Nhập một tuple từ người dùng
input_tuple = eval(input("Nhập một tuple (ví dụ: (1, 2, 3)): "))
first, last = truy_cap_phan_tu(input_tuple)

print("Phần tử đầu tiên trong tuple là:", first)
print("Phần tử cuối cùng trong tuple là:", last)
