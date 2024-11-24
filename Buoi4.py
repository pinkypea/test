# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# import sys
# app = QApplication(sys.argv)
# window = QWidget()
# button = QPushButton("Click me!!!", window)
# button.setGeometry(100, 100, 100, 50)
# window.show()
# app.exec()


class DongVat:
    def __init__(self, ten, tuoi, loai, moi_truong_song):
        self.ten = ten
        self.tuoi = tuoi
        self.loai = loai
        self.moi_truong_song = moi_truong_song

    def cap_nhat_moi_truong_song_moi(self, moi_truong_song_moi):
        self.moi_truong_song = moi_truong_song_moi
        print(self.moi_truong_song)

    def output(self):
        print("Tên:", self.ten)
        print("Tuổi:", self.tuoi)
        print("Loài:", self.loai)
        print("Môi trường sống:", self.moi_truong_song)

animal = DongVat("Rex", 4, "Sư tử", "Thảo nguyên")
animal.output()
animal.cap_nhat_moi_truong_song_moi("Rừng rậm")