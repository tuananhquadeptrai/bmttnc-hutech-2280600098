def chia_het_cho_5(so_nhi_phan):
    # Chuyển đổi số nhị phân thành số thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    
    # Kiểm tra chia hết cho 5
    return so_thap_phan % 5 == 0

chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
chuoi_so_nhi_list = chuoi_so_nhi_phan.split(",")
so_chia_het_cho_5 = [so for so in chuoi_so_nhi_list if chia_het_cho_5(so)]

if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là: ", ket_qua)
    print("Số lượng số nhị phân chia hết cho 5 là: ", len(so_chia_het_cho_5))
else:
    print("Không có số nhị phân nào chia hết cho 5.")