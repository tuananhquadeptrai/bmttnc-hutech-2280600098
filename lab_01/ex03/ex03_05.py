def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

input_string = input("Nhập danh sách các số cách nhau bằng dấu phẩy: ")

word_list= input_string.split(",")
so_lan_xuat_hien= dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các số trong danh sách là:", so_lan_xuat_hien)
