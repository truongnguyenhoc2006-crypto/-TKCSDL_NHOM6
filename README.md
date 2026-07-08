# HỆ THỐNG QUẢN LÝ SINH VIÊN

## 1. Giới thiệu

Đây là chương trình **Quản lý sinh viên** được xây dựng bằng ngôn ngữ **Python**, sử dụng thư viện **Tkinter** để thiết kế giao diện và **SQLite** để lưu trữ dữ liệu.

Chương trình hỗ trợ đăng nhập vào hệ thống và quản lý thông tin sinh viên như: mã sinh viên, mật khẩu, họ tên, ngày sinh, giới tính, lớp và điểm trung bình.

## 2. Chức năng chính

### 2.1. Đăng nhập hệ thống

Người dùng đăng nhập bằng mã sinh viên và mật khẩu đã có trong cơ sở dữ liệu. Nếu đăng nhập thành công, chương trình sẽ mở giao diện quản lý sinh viên.

Tài khoản mẫu:

| Tên đăng nhập | Mật khẩu |
| ------------- | -------- |
| SV001         | 123456   |
| SV002         | 123456   |
| admin         | admin123 |

### 2.2. Quản lý sinh viên

Chương trình hỗ trợ các chức năng:

* Thêm sinh viên mới
* Cập nhật thông tin sinh viên
* Xóa sinh viên
* Làm mới form nhập liệu
* Hiển thị danh sách sinh viên
* Chọn sinh viên từ bảng để xem và chỉnh sửa thông tin

### 2.3. Tìm kiếm sinh viên

Người dùng có thể tìm kiếm sinh viên theo:

* Mã sinh viên
* Một phần họ tên sinh viên

### 2.4. Thống kê sinh viên

Chương trình có chức năng thống kê:

* Tổng số sinh viên
* Điểm trung bình chung
* Điểm cao nhất
* Điểm thấp nhất
* Phân loại học lực: Giỏi, Khá, Trung bình, Yếu

### 2.5. Sắp xếp dữ liệu

Chương trình hỗ trợ sắp xếp danh sách sinh viên theo:

* Điểm trung bình giảm dần
* Họ tên theo thứ tự A-Z

## 3. Công nghệ sử dụng

* Ngôn ngữ lập trình: Python
* Giao diện: Tkinter
* Cơ sở dữ liệu: SQLite
* Công cụ quản lý source code: GitHub

## 4. Cấu trúc thư mục

```text
QuanLySinhVien/
│
├── dangnhap.py
├── QuanLySinhVien.py
├── sinhvien.db
└── README.md
```

Trong đó:

* `dangnhap.py`: File chạy đầu tiên, dùng để đăng nhập vào hệ thống.
* `QuanLySinhVien.py`: File chứa giao diện và các chức năng quản lý sinh viên.
* `sinhvien.db`: File cơ sở dữ liệu SQLite lưu thông tin sinh viên.
* `README.md`: File hướng dẫn cài đặt và sử dụng chương trình.

## 5. Yêu cầu cài đặt

Máy tính cần cài đặt:

* Python 3.x
* Các thư viện có sẵn của Python:

  * tkinter
  * sqlite3
  * os

Thông thường, `tkinter` và `sqlite3` đã có sẵn khi cài Python.

## 6. Cách chạy chương trình

### Bước 1: Tải source code về máy

Có thể tải source code từ GitHub hoặc clone bằng lệnh:

```bash
git clone <link-repository>
```

Sau đó mở thư mục dự án:

```bash
cd QuanLySinhVien
```

### Bước 2: Kiểm tra tên file

Đảm bảo các file có tên đúng như sau:

```text
dangnhap.py
QuanLySinhVien.py
sinhvien.db
```

Nếu file tải về có dạng `dangnhap(1).py` hoặc `QuanLySinhVien(1).py`, cần đổi tên lại thành:

```text
dangnhap.py
QuanLySinhVien.py
```

### Bước 3: Chạy chương trình

Mở terminal hoặc command prompt tại thư mục chứa source code, sau đó chạy lệnh:

```bash
python dangnhap.py
```

Nếu máy dùng lệnh `python3`, chạy:

```bash
python3 dangnhap.py
```

## 7. Cách sử dụng

### Đăng nhập

Nhập tài khoản mẫu:

```text
Mã sinh viên: admin
Mật khẩu: admin123
```

Sau khi đăng nhập thành công, chương trình sẽ chuyển sang giao diện quản lý sinh viên.

### Thêm sinh viên

Nhập đầy đủ thông tin sinh viên, sau đó nhấn nút **Thêm**.

Các thông tin bắt buộc gồm:

* Mã sinh viên
* Mật khẩu
* Họ tên

### Cập nhật sinh viên

Chọn một sinh viên trong bảng, sửa thông tin cần thay đổi, sau đó nhấn **Cập nhật**.

### Xóa sinh viên

Chọn sinh viên cần xóa, sau đó nhấn **Xóa** và xác nhận thao tác.

### Tìm kiếm sinh viên

Nhấn nút **Tìm kiếm**, nhập mã sinh viên hoặc họ tên cần tìm.

### Thống kê sinh viên

Nhấn nút **Thống kê** để xem thông tin tổng hợp về số lượng sinh viên và điểm trung bình.

### Sắp xếp sinh viên

Có thể sắp xếp danh sách sinh viên theo:

* Điểm trung bình
* Họ tên

## 8. Cơ sở dữ liệu

Chương trình sử dụng database SQLite với file:

```text
sinhvien.db
```

Bảng dữ liệu chính là `SINH_VIEN`, gồm các trường:

| Tên trường | Kiểu dữ liệu | Ghi chú            |
| ---------- | ------------ | ------------------ |
| MaSV       | TEXT         | Khóa chính         |
| MatKhau    | TEXT         | Mật khẩu đăng nhập |
| HoTen      | TEXT         | Họ tên sinh viên   |
| NgaySinh   | TEXT         | Ngày sinh          |
| GioiTinh   | TEXT         | Giới tính          |
| Lop        | TEXT         | Lớp                |
| DiemTB     | REAL         | Điểm trung bình    |

Nếu chưa có dữ liệu, chương trình sẽ tự tạo bảng và thêm một số tài khoản mẫu để đăng nhập.

## 9. Một số lỗi thường gặp

### Lỗi không mở được file quản lý

Nguyên nhân có thể do tên file chưa đúng. Cần đảm bảo file quản lý có tên:

```text
QuanLySinhVien.py
```

### Lỗi không tìm thấy database

Cần đảm bảo file `sinhvien.db` nằm cùng thư mục với `dangnhap.py` và `QuanLySinhVien.py`.

### Lỗi không chạy được lệnh python

Kiểm tra xem máy đã cài Python chưa bằng lệnh:

```bash
python --version
```

hoặc:

```bash
python3 --version
```

## 10. Thành viên thực hiện

Nhóm thực hiện: Nhóm 6

Đề tài: Xây dựng hệ thống quản lý sinh viên bằng Python và SQLite.

## 11. Ghi chú

Chương trình được xây dựng phục vụ cho mục đích học tập, thực hành môn học và quản lý dữ liệu sinh viên ở mức cơ bản.
