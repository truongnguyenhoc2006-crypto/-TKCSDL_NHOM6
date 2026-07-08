# HỆ THỐNG QUẢN LÝ SINH VIÊN

## 1. Giới thiệu

Đây là chương trình **Quản lý sinh viên** được xây dựng bằng **Python**. Chương trình sử dụng **Tkinter** để tạo giao diện và **SQLite** để lưu trữ dữ liệu sinh viên.

Hệ thống hỗ trợ đăng nhập và quản lý thông tin sinh viên cơ bản như: thêm, sửa, xóa, tìm kiếm, thống kê và sắp xếp sinh viên.

## 2. Chức năng chính

* Đăng nhập hệ thống.
* Hiển thị danh sách sinh viên.
* Thêm sinh viên mới.
* Cập nhật thông tin sinh viên.
* Xóa sinh viên.
* Tìm kiếm sinh viên theo mã sinh viên hoặc họ tên.
* Thống kê số lượng sinh viên và điểm trung bình.
* Sắp xếp sinh viên theo điểm trung bình hoặc họ tên.

## 3. Công nghệ sử dụng

* Python
* Tkinter
* SQLite

## 4. Cấu trúc thư mục

```text id="zufcqr"
QuanLySinhVien/
│
├── dangnhap.py
├── QuanLySinhVien.py
├── sinhvien.db
└── README.md
```

## 5. Tài khoản đăng nhập mẫu

| Tên đăng nhập | Mật khẩu | Vai trò       |
| ------------- | -------- | ------------- |
| admin         | admin123 | Quản trị viên |
| SV001         | 123456   | Sinh viên     |
| SV002         | 123456   | Sinh viên     |

## 6. Cách chạy chương trình

Mở terminal hoặc command prompt tại thư mục chứa source code, sau đó chạy lệnh:

```bash id="ae3hk6"
python dangnhap.py
```

Nếu máy dùng lệnh `python3`, chạy:

```bash id="m4ufm6"
python3 dangnhap.py
```

## 7. Hướng dẫn sử dụng

Sau khi chạy chương trình, nhập tài khoản mẫu để đăng nhập.

Ví dụ:

```text id="4fgxbk"
Tên đăng nhập: admin
Mật khẩu: admin123
```

Sau khi đăng nhập thành công, chương trình sẽ mở giao diện quản lý sinh viên.

Trong giao diện quản lý, người dùng có thể:

* Nhập thông tin rồi nhấn **Thêm** để thêm sinh viên.
* Chọn sinh viên trong bảng rồi nhấn **Cập nhật** để sửa thông tin.
* Chọn sinh viên rồi nhấn **Xóa** để xóa.
* Nhấn **Tìm kiếm** để tìm sinh viên.
* Nhấn **Thống kê** để xem thống kê.
* Nhấn nút sắp xếp để sắp xếp theo điểm hoặc họ tên.

## 8. Lưu ý

* Các file `dangnhap.py`, `QuanLySinhVien.py` và `sinhvien.db` cần nằm cùng một thư mục.
* Nếu file có tên như `dangnhap(1).py` hoặc `QuanLySinhVien(1).py`, cần đổi tên lại thành `dangnhap.py` và `QuanLySinhVien.py`.

## 9. Kết luận

Chương trình Quản lý sinh viên giúp quản lý thông tin sinh viên ở mức cơ bản, phù hợp cho bài tập môn học và thực hành Python với cơ sở dữ liệu SQLite.
::: 
