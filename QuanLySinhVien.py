import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

DB_NAME = "sinhvien.db"

class QuanLySinhVienClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Sinh viên")
        self.root.geometry("1100x700+200+50")
        self.root.config(bg="beige")

        Label(self.root, text="QUẢN LÝ THÔNG TIN SINH VIÊN", bg="beige", fg="darkblue",
              bd=10, relief=RIDGE, font=("Times New Roman", 30, "bold"), pady=5).pack(side=TOP, fill=X)

        self.setup_tab_sinhvien()
        self.load_data()

    def connect_db(self):
        return sqlite3.connect(DB_NAME)

    # ==================== TAB SINH VIÊN ====================
    def setup_tab_sinhvien(self):
        # Biến StringVar
        self.ma_var = StringVar()
        self.matkhau_var = StringVar()
        self.hoten_var = StringVar()
        self.ngaysinh_var = StringVar()
        self.gioitinh_var = StringVar()
        self.lop_var = StringVar()
        self.diem_var = StringVar()

        # Frame nhập liệu
        frame_input = LabelFrame(self.root, text="Thông tin sinh viên", bg="beige",
                                 fg="Green", bd=8, relief=RIDGE, font=("Times New Roman", 13, "bold"))
        frame_input.place(x=10, y=70, width=400, height=480)

        Label(frame_input, text="Mã SV:", bg="beige", font=("Times New Roman", 12, "bold")).grid(row=0, column=0, sticky=W, padx=15, pady=10)
        Entry(frame_input, textvariable=self.ma_var, font=("Times New Roman", 12), width=20).grid(row=0, column=1, padx=10, pady=10)

        Label(frame_input, text="Mật khẩu:", bg="beige", font=("Times New Roman", 12, "bold")).grid(row=1, column=0, sticky=W, padx=15, pady=10)
        Entry(frame_input, textvariable=self.matkhau_var, font=("Times New Roman", 12), width=20, show="*").grid(row=1, column=1, padx=10, pady=10)

        Label(frame_input, text="Họ tên:", bg="beige", font=("Times New Roman", 12, "bold")).grid(row=2, column=0, sticky=W, padx=15, pady=10)
        Entry(frame_input, textvariable=self.hoten_var, font=("Times New Roman", 12), width=20).grid(row=2, column=1, padx=10, pady=10)

        Label(frame_input, text="Ngày sinh (YYYY-MM-DD):", bg="beige", font=("Times New Roman", 10, "bold")).grid(row=3, column=0, sticky=W, padx=15, pady=10)
        Entry(frame_input, textvariable=self.ngaysinh_var, font=("Times New Roman", 12), width=20).grid(row=3, column=1, padx=10, pady=10)

        Label(frame_input, text="Giới tính:", bg="beige", font=("Times New Roman", 12, "bold")).grid(row=4, column=0, sticky=W, padx=15, pady=10)
        self.cbo_gioitinh = ttk.Combobox(frame_input, textvariable=self.gioitinh_var, font=("Times New Roman", 11), width=18, state="readonly")
        self.cbo_gioitinh['values'] = ("Nam", "Nữ", "Khác")
        self.cbo_gioitinh.grid(row=4, column=1, padx=10, pady=10)

        Label(frame_input, text="Lớp:", bg="beige", font=("Times New Roman", 12, "bold")).grid(row=5, column=0, sticky=W, padx=15, pady=10)
        Entry(frame_input, textvariable=self.lop_var, font=("Times New Roman", 12), width=20).grid(row=5, column=1, padx=10, pady=10)

        Label(frame_input, text="Điểm TB:", bg="beige", font=("Times New Roman", 12, "bold")).grid(row=6, column=0, sticky=W, padx=15, pady=10)
        Entry(frame_input, textvariable=self.diem_var, font=("Times New Roman", 12), width=20).grid(row=6, column=1, padx=10, pady=10)

        # Frame nút chức năng
        frame_btn = Frame(self.root, bd=8, relief=RIDGE, bg="beige")
        frame_btn.place(x=10, y=560, width=400, height=80)

        Button(frame_btn, text="Thêm", command=self.them_sv, font=("Times New Roman", 12, "bold"), bg="lightgreen", width=7).grid(row=0, column=0, padx=5, pady=15)
        Button(frame_btn, text="Cập nhật", command=self.capnhat_sv, font=("Times New Roman", 12, "bold"), bg="lightgreen", width=7).grid(row=0, column=1, padx=5, pady=15)
        Button(frame_btn, text="Xóa", command=self.xoa_sv, font=("Times New Roman", 12, "bold"), bg="lightgreen", width=7).grid(row=0, column=2, padx=5, pady=15)
        Button(frame_btn, text="Làm mới", command=self.lam_moi, font=("Times New Roman", 12, "bold"), bg="lightgreen", width=7).grid(row=0, column=3, padx=5, pady=15)

        # Các nút chức năng phụ
        frame_chucnang = Frame(self.root, bd=8, relief=RIDGE, bg="beige")
        frame_chucnang.place(x=430, y=560, width=600, height=80)

        Button(frame_chucnang, text="🔍 Tìm kiếm", command=self.tim_kiem, font=("Times New Roman", 12, "bold"), bg="lightblue", width=10).grid(row=0, column=0, padx=10, pady=15)
        Button(frame_chucnang, text="📈 Thống kê", command=self.thong_ke, font=("Times New Roman", 12, "bold"), bg="lightblue", width=10).grid(row=0, column=1, padx=10, pady=15)
        Button(frame_chucnang, text="⬆ Sắp xếp (điểm)", command=self.sap_xep_diem, font=("Times New Roman", 12, "bold"), bg="lightblue", width=10).grid(row=0, column=2, padx=10, pady=15)
        Button(frame_chucnang, text="⬆ Sắp xếp (tên)", command=self.sap_xep_ten, font=("Times New Roman", 12, "bold"), bg="lightblue", width=10).grid(row=0, column=3, padx=10, pady=15)

        # Frame bảng hiển thị
        frame_table = Frame(self.root, bd=8, relief=RIDGE, bg="beige")
        frame_table.place(x=430, y=70, width=600, height=480)

        scroll_y = ttk.Scrollbar(frame_table, orient=VERTICAL)
        scroll_x = ttk.Scrollbar(frame_table, orient=HORIZONTAL)

        self.table_sv = ttk.Treeview(frame_table, columns=("masv", "hoten", "ngaysinh", "gioitinh", "lop", "diem"),
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.table_sv.yview)
        scroll_x.config(command=self.table_sv.xview)

        self.table_sv.heading("masv", text="Mã SV")
        self.table_sv.heading("hoten", text="Họ tên")
        self.table_sv.heading("ngaysinh", text="Ngày sinh")
        self.table_sv.heading("gioitinh", text="Giới tính")
        self.table_sv.heading("lop", text="Lớp")
        self.table_sv.heading("diem", text="Điểm TB")
        self.table_sv['show'] = 'headings'

        self.table_sv.column("masv", width=80)
        self.table_sv.column("hoten", width=150)
        self.table_sv.column("ngaysinh", width=100)
        self.table_sv.column("gioitinh", width=80)
        self.table_sv.column("lop", width=80)
        self.table_sv.column("diem", width=80)

        self.table_sv.pack(fill=BOTH, expand=1)
        self.table_sv.bind("<ButtonRelease-1>", self.chon_sv)

    def load_data(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT MaSV, HoTen, NgaySinh, GioiTinh, Lop, DiemTB FROM SINH_VIEN ORDER BY MaSV")
        rows = cursor.fetchall()
        self.table_sv.delete(*self.table_sv.get_children())
        for row in rows:
            self.table_sv.insert("", END, values=row)
        conn.close()

    def chon_sv(self, event):
        selected = self.table_sv.focus()
        values = self.table_sv.item(selected, "values")
        if values:
            self.ma_var.set(values[0])
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT MatKhau FROM SINH_VIEN WHERE MaSV=?", (values[0],))
            row = cursor.fetchone()
            if row:
                self.matkhau_var.set(row[0])
            conn.close()
            self.hoten_var.set(values[1])
            self.ngaysinh_var.set(values[2])
            self.gioitinh_var.set(values[3])
            self.lop_var.set(values[4])
            self.diem_var.set(str(values[5]) if values[5] else "")

    def lam_moi(self):
        self.ma_var.set("")
        self.matkhau_var.set("")
        self.hoten_var.set("")
        self.ngaysinh_var.set("")
        self.gioitinh_var.set("")
        self.lop_var.set("")
        self.diem_var.set("")
        self.load_data()

    def them_sv(self):
        if not self.ma_var.get() or not self.matkhau_var.get() or not self.hoten_var.get():
            messagebox.showerror("Lỗi", "Mã SV, mật khẩu và họ tên không được để trống!")
            return

        try:
            diem = float(self.diem_var.get()) if self.diem_var.get() else None
        except:
            messagebox.showerror("Lỗi", "Điểm TB phải là số!")
            return

        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO SINH_VIEN (MaSV, MatKhau, HoTen, NgaySinh, GioiTinh, Lop, DiemTB)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (self.ma_var.get(), self.matkhau_var.get(), self.hoten_var.get(),
                  self.ngaysinh_var.get(), self.gioitinh_var.get(), self.lop_var.get(), diem))
            conn.commit()
            self.load_data()
            self.lam_moi()
            messagebox.showinfo("Thành công", "Đã thêm sinh viên mới!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Lỗi", "Mã SV đã tồn tại!")
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra:\n{ex}")
        conn.close()

    def capnhat_sv(self):
        if not self.ma_var.get():
            messagebox.showerror("Lỗi", "Vui lòng chọn sinh viên cần cập nhật!")
            return

        try:
            diem = float(self.diem_var.get()) if self.diem_var.get() else None
        except:
            messagebox.showerror("Lỗi", "Điểm TB phải là số!")
            return

        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                UPDATE SINH_VIEN 
                SET MatKhau=?, HoTen=?, NgaySinh=?, GioiTinh=?, Lop=?, DiemTB=?
                WHERE MaSV=?
            ''', (self.matkhau_var.get(), self.hoten_var.get(), self.ngaysinh_var.get(),
                  self.gioitinh_var.get(), self.lop_var.get(), diem, self.ma_var.get()))
            conn.commit()
            self.load_data()
            self.lam_moi()
            messagebox.showinfo("Thành công", "Cập nhật thông tin thành công!")
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra:\n{ex}")
        conn.close()

    def xoa_sv(self):
        if not self.ma_var.get():
            return
        if messagebox.askyesno("Xác nhận", f"Xóa sinh viên {self.hoten_var.get()} (Mã {self.ma_var.get()})?"):
            conn = self.connect_db()
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM SINH_VIEN WHERE MaSV=?", (self.ma_var.get(),))
                conn.commit()
                self.load_data()
                self.lam_moi()
                messagebox.showinfo("Thành công", "Đã xóa sinh viên!")
            except Exception as ex:
                messagebox.showerror("Lỗi", f"Không thể xóa:\n{ex}")
            conn.close()

    def tim_kiem(self):
        tu_khoa = messagebox.askstring("Tìm kiếm", "Nhập mã SV hoặc một phần họ tên:")
        if tu_khoa is None:
            return
        tu_khoa = tu_khoa.strip()
        if not tu_khoa:
            self.load_data()
            return

        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT MaSV, HoTen, NgaySinh, GioiTinh, Lop, DiemTB 
            FROM SINH_VIEN 
            WHERE MaSV LIKE ? OR HoTen LIKE ?
        ''', (f'%{tu_khoa}%', f'%{tu_khoa}%'))
        rows = cursor.fetchall()
        self.table_sv.delete(*self.table_sv.get_children())
        for row in rows:
            self.table_sv.insert("", END, values=row)
        conn.close()

    def thong_ke(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*), AVG(DiemTB), MAX(DiemTB), MIN(DiemTB) FROM SINH_VIEN")
        stats = cursor.fetchone()
        tong = stats[0] or 0
        avg = stats[1] or 0
        max_d = stats[2] or 0
        min_d = stats[3] or 0

        cursor.execute('''
            SELECT 
                SUM(CASE WHEN DiemTB >= 8 THEN 1 ELSE 0 END) as gioi,
                SUM(CASE WHEN DiemTB >= 6.5 AND DiemTB < 8 THEN 1 ELSE 0 END) as kha,
                SUM(CASE WHEN DiemTB >= 5 AND DiemTB < 6.5 THEN 1 ELSE 0 END) as tb,
                SUM(CASE WHEN DiemTB < 5 THEN 1 ELSE 0 END) as yeu 
            FROM SINH_VIEN
        ''')
        phan_loai = cursor.fetchone()
        conn.close()

        msg = (f"📊 THỐNG KÊ SINH VIÊN\n"
               f"Tổng số: {tong}\n"
               f"Điểm TB trung bình: {avg:.2f}\n"
               f"Điểm cao nhất: {max_d:.2f}\n"
               f"Điểm thấp nhất: {min_d:.2f}\n\n"
               f"Phân loại học lực:\n"
               f"Giỏi (>=8.0): {phan_loai[0] or 0}\n"
               f"Khá (6.5-7.9): {phan_loai[1] or 0}\n"
               f"Trung bình (5.0-6.4): {phan_loai[2] or 0}\n"
               f"Yếu (<5.0): {phan_loai[3] or 0}")
        messagebox.showinfo("Thống kê", msg)

    def sap_xep_diem(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT MaSV, HoTen, NgaySinh, GioiTinh, Lop, DiemTB FROM SINH_VIEN ORDER BY DiemTB DESC")
        rows = cursor.fetchall()
        self.table_sv.delete(*self.table_sv.get_children())
        for row in rows:
            self.table_sv.insert("", END, values=row)
        conn.close()
        messagebox.showinfo("Sắp xếp", "Đã sắp xếp theo điểm TB giảm dần.")

    def sap_xep_ten(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT MaSV, HoTen, NgaySinh, GioiTinh, Lop, DiemTB FROM SINH_VIEN ORDER BY HoTen")
        rows = cursor.fetchall()
        self.table_sv.delete(*self.table_sv.get_children())
        for row in rows:
            self.table_sv.insert("", END, values=row)
        conn.close()
        messagebox.showinfo("Sắp xếp", "Đã sắp xếp theo họ tên A-Z.")


if __name__ == "__main__":
    root = Tk()
    app = QuanLySinhVienClass(root)
    root.mainloop()