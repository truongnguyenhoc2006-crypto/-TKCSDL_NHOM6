import os
import sqlite3
from tkinter import *
from tkinter import messagebox

DB_NAME = "sinhvien.db"

class DangNhapClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng Nhập Hệ Thống Quản Lý Sinh Viên")
        self.root.geometry("650x450+600+150")
        self.root.config(bg="white")

        # Tiêu đề
        Label(self.root, text="QUẢN LÝ SINH VIÊN", font=("Times New Roman", 40, "bold"),
              bg="white", fg="darkblue").place(x=100, y=60)

        # Nhãn và entry
        Label(self.root, text="Mã sinh viên:", font=("Times New Roman", 17, "bold"),
              bg="white", fg="black").place(x=30, y=170)
        Label(self.root, text="Mật khẩu:", font=("Times New Roman", 17, "bold"),
              bg="white", fg="black").place(x=30, y=220)

        self.var_tendangnhap = StringVar()
        self.var_mk = StringVar()

        self.txt_tendangnhap = Entry(self.root, textvariable=self.var_tendangnhap,
                                     font=("Times New Roman", 17, "bold"), bg="beige")
        self.txt_tendangnhap.place(x=210, y=170, width=390)

        self.txt_mk = Entry(self.root, textvariable=self.var_mk, show="*",
                            font=("Times New Roman", 17, "bold"), bg="beige")
        self.txt_mk.place(x=210, y=220, width=390)

        Button(self.root, text="ĐĂNG NHẬP", font=("Times New Roman", 17, "bold"),
               bg="darkblue", fg="white", cursor="hand2", command=self.dang_nhap).place(x=210, y=290, width=390, height=45)

        self.txt_tendangnhap.focus_set()

        # Tạo database và bảng nếu chưa có
        self.tao_database()

    def tao_database(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SINH_VIEN (
                MaSV TEXT PRIMARY KEY,
                MatKhau TEXT NOT NULL,
                HoTen TEXT NOT NULL,
                NgaySinh TEXT,
                GioiTinh TEXT,
                Lop TEXT,
                DiemTB REAL
            )
        ''')
        # Tạo tài khoản mặc định nếu chưa có
        cursor.execute("SELECT COUNT(*) FROM SINH_VIEN WHERE MaSV='SV001'")
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO SINH_VIEN (MaSV, MatKhau, HoTen, NgaySinh, GioiTinh, Lop, DiemTB)
                VALUES 
                ('SV001', '123456', 'Nguyễn Văn A', '2000-01-01', 'Nam', 'CNTT1', 8.5),
                ('SV002', '123456', 'Trần Thị B', '2001-02-02', 'Nữ', 'CNTT2', 7.2),
                ('admin', 'admin123', 'Quản Trị Viên', '1990-01-01', 'Nam', 'Admin', 0)
            ''')
        conn.commit()
        conn.close()

    def dang_nhap(self):
        username = self.var_tendangnhap.get().strip()
        password = self.var_mk.get()

        if not username or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ mã sinh viên và mật khẩu!", parent=self.root)
            return

        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("SELECT MatKhau FROM SINH_VIEN WHERE MaSV = ?", (username,))
            row = cursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Lỗi", "Mã sinh viên không tồn tại!", parent=self.root)
            elif row[0] != password:
                messagebox.showerror("Lỗi", "Mật khẩu không chính xác!", parent=self.root)
            else:
                messagebox.showinfo("Thành công", "Đăng nhập thành công!", parent=self.root)
                self.root.destroy()
                # Mở giao diện quản lý
                os.system("python QuanLySinhVien.py")
        except Exception as ex:
            messagebox.showerror("Lỗi DB", f"Lỗi kết nối CSDL:\n{ex}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = DangNhapClass(root)
    root.mainloop()