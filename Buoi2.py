# class pet:
#     name = ""
#     age = 0
#     type = ""
#     weight = 0
#     color = ""

# my_dog = pet()

# my_dog.name = "Nick"
# my_dog.age = 4
# my_dog.type = "Shiba"
# my_dog.weight = 7
# my_dog.color = "Yellow"

# print(my_dog.name)
# print(my_dog.age)
# print(my_dog.type)
# print(my_dog.weight)
# print(my_dog.color)

# Khởi tạo 1 class là laptop, có thuộc tính:
# - Hãng
# - Màu
# - Kiểu dáng
# - RAM
# - Disk
# - Màn hình
# - AI (true/false)
# - Giá

# Sau đó khởi tạo 1 object thông qua class laptop.
# Và in ra các giá trị của object đó.

class laptop:
    hang = ""
    mau = ""
    kieu_dang = ""
    RAM = 0
    Disk = 0
    man_hinh = 0
    AI = True
    gia = 0

    def __init__(self, hang, mau, kieu_dang, RAM, Disk, man_hinh, AI, gia):
        self.hang = hang
        self.mau = mau
        self.kieu_dang = kieu_dang
        self.RAM = RAM
        self.Disk = Disk
        self.man_hinh = man_hinh
        self.AI = AI
        self.gia = gia

my_laptop1 = laptop("Lenovo", "Bạc", "Doanh nhân", 16, 512, 14.6, False, 17000000)

my_laptop = laptop()
my_laptop.hang = "Lenovo"
my_laptop.mau = "bac"
my_laptop.kieu_dang = "doanh nhân"
my_laptop.RAM = 16
my_laptop.Disk = 512
my_laptop.man_hinh = 14.6
my_laptop.AI = False
my_laptop.gia = 17000000

print(my_laptop.hang)
print(my_laptop.mau)
print(my_laptop.kieu_dang)
print(my_laptop.RAM)
print(my_laptop.Disk)
print(my_laptop.man_hinh)
print(my_laptop.AI)
print(my_laptop.gia)

class Xe:

    def __init__(self, hang, so_cho_ngoi, mau_sac):
        self.hang = hang
        self.so_cho_ngoi = so_cho_ngoi
        self.mau_sac = mau_sac

my_car = Xe("Audi", 4, "Đen")
