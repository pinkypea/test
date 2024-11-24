# class Xe:
#     def __init__(self, loai_xe, hang_xe, mau_sac, so_cho_ngoi, so_banh_xe, gia_tien):
#         self.loai_xe = loai_xe
#         self.hang_xe = hang_xe
#         self.mau_sac = mau_sac
#         self.so_cho_ngoi = so_cho_ngoi
#         self.so_banh_xe = so_banh_xe
#         self.gia_tien = gia_tien

#     # Tạo phương thức để in ra thông tin
#     def information(self):
#         print("Loại xe:", self.loai_xe)
#         print("Hãng xe:", self.hang_xe)
#         print("Màu sắc:", self.mau_sac)
#         print("Số chỗ ngồi:", self.so_cho_ngoi)
#         print("Số bánh xe:", self.so_banh_xe)
#         print("Gía tiền:", self.gia_tien)

# class xe_dap(Xe):
#     ghidong = True
#     potan = True

# my_bycicle = xe_dap("Xe đạp", "Trek", "Xanh lục", 1, 2, 5000000)
# my_bycicle.ghidong = True
# my_bycicle.potan = False
# my_bycicle.information()
# my_car = Xe("Ô tô", "Porsche", "Vàng", 4, 4, 11000000000)
# # Gọi ra phương thức để sử dụng
# my_car.information()


# Viết 1 class hinh_chu_nhat gồm:
#     - Phương thức __init__ để khởi tạo chiều dài và chiều rộng
#     - Phương thức tinh_chu_vi để tính chu vi HCN.
#     - Phương thức tinh_dien_tich để tính diện tích HCN.

# class hinh_chu_nhat:
#     def __init__(self, chieu_dai, chieu_rong):
#         self.chieu_dai = chieu_dai
#         self.chieu_rong = chieu_rong

#     def tinh_chu_vi(self):
#         print((self.chieu_dai + self.chieu_rong) * 2)

#     def tinh_dien_tich(self):
#         print(self.chieu_dai * self.chieu_rong)

# HCN = hinh_chu_nhat(10, 5)
# HCN.tinh_chu_vi()
# HCN.tinh_dien_tich()

class Xe:
    def __init__(self, hang, mau_sac, gia_tien):
        self.hang = hang
        self.mau_sac = mau_sac
        self.gia_tien = gia_tien

    def khoi_dong(self):
        print("Xe {self.hang} đang khởi động")

class XeHoi(Xe):
    def chay_bang_bon_banh(self):
        print("Xe {self.hang} đang chạy về phía trước bằng động cơ")

class XeDap(Xe):
    def dap_bang_hai_chan(self):
        print("Xe {self.hang} đang được đạp về phía trước")