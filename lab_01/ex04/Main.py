from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()
while (1==1):
    print("Chương trình quản lý sinh viên")
    
    print("\n============MENU=============")
    print("1.Them sinh vien")
    print("2.Cap nhat thong tin sinh vien boi ID")
    print("3.Xoa sinh vien boi ID")
    print("4.Tim kiem sinh vien theo ten")
    print("5.Sap xep danh sach sinh vien theo diem trung binh")
    print("6.Sap xep danh sach sinh vien theo ten chuyen nganh")
    print("7.Hien thi danh sach sinh vien")
    print("0.Thoat")
    print("=============================")
    key =int(input("Nhap lua chon cua ban: "))
    if (key == 1):
     print("\n1.Thêm sinh viên")
     qlsv.nhapSinhVien()
     print("Thêm sinh viên thành công!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien()>0):
            print("\n2.Cập nhật sinh viên")
            print("\nNhập ID sinh viên cần cập nhật: ")
            ID=int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sách sinh viên rỗng!")
    elif (key==3):
        if(qlsv.soLuongSinhVien()> 0):
            print("\n3.Xoa Sinh Vien")
            print("\nNhap ID sinh vien can xoa: ")
            ID=int(input())
            if(qlsv.deleteByID(ID)):
                print("\nSinhVien id = ",ID," da xoa thanh cong!")
            else:
                print("\nKhong tim thay sinh vien co id = ",ID)
        else:
            print("Danh sach sinh vien rong!")
    elif (key==4):
        if(qlsv.soLuongSinhVien()>0):
            print("\n4.Tim kiem sinh vien theo ten")
            print("\nNhap ten sinh vien can tim: ")
            keyword=input()
            searchResult=qlsv.findByName(keyword)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien rong!")
    elif (key==5):
        if(qlsv.soLuongSinhVien()>0):
            print("\n5.Sap xep danh sach sinh vien theo diem trung binh")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong!")
    elif (key==6):
        if(qlsv.soLuongSinhVien()>0):
            print("\n6.Sap xep danh sach sinh vien theo ten ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong!")
    elif (key==7):
        if(qlsv.soLuongSinhVien()>0):
            print("\n7.Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong!")
    elif (key==0):
        print("\n0.Thoat chuong trinh")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\n Hay chon chuc nang khac")
            