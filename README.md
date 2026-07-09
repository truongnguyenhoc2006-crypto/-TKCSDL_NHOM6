# HỆ THỐNG QUẢN LÝ SINH VIÊN

## 1. Giới thiệu

Đây là chương trình **Quản lý sinh viên** được xây dựng bằng ngôn ngữ **Python**.  
Chương trình sử dụng **Tkinter** để thiết kế giao diện và **SQLite** để lưu trữ dữ liệu sinh viên.

Hệ thống hỗ trợ đăng nhập và quản lý thông tin sinh viên cơ bản như: thêm, cập nhật, xóa, tìm kiếm, thống kê và sắp xếp danh sách sinh viên.

## 2. Chức năng chính

- Đăng nhập hệ thống bằng mã sinh viên và mật khẩu.
- Hiển thị danh sách sinh viên.
- Thêm sinh viên mới.
- Cập nhật thông tin sinh viên.
- Xóa sinh viên.
- Tìm kiếm sinh viên theo mã sinh viên hoặc họ tên.
- Thống kê số lượng sinh viên, điểm trung bình, điểm cao nhất và điểm thấp nhất.
- Phân loại học lực: Giỏi, Khá, Trung bình, Yếu.
- Sắp xếp sinh viên theo điểm trung bình hoặc họ tên.

## 3. Công nghệ sử dụng

- **Python**
- **Tkinter**
- **SQLite**
- **Jupyter Notebook**

## 4. Cấu trúc thư mục

```text
-TKCSDL_NHOM6/
│
├── dangnhap.py
├── QuanLySinhVien.py
├── QuanLySinhVien.ipynb
├── sinhvien.db
└── README.md
```

Trong đó:

- `dangnhap.py`: file chạy đầu tiên, dùng để đăng nhập vào hệ thống.
- `QuanLySinhVien.py`: file chứa giao diện và các chức năng quản lý sinh viên.
- `QuanLySinhVien.ipynb`: notebook trình bày và chạy thử code.
- `sinhvien.db`: file cơ sở dữ liệu SQLite lưu thông tin sinh viên.
- `README.md`: file giới thiệu và hướng dẫn sử dụng chương trình.

## 5. Tài khoản đăng nhập mẫu

| Tên đăng nhập | Mật khẩu | Vai trò |
|---|---|---|
| admin | admin123 | Quản trị viên |
| SV001 | 123456 | Sinh viên |
| SV002 | 123456 | Sinh viên |

## 6. Cách chạy chương trình

### Bước 1: Tải source code

Tải project về máy hoặc clone repository:

```bash
git clone https://github.com/truongnguyenhoc2006-crypto/-TKCSDL_NHOM6.git
```

Sau đó mở thư mục project:

```bash
cd -TKCSDL_NHOM6
```

### Bước 2: Kiểm tra file

Đảm bảo các file sau nằm cùng một thư mục:

```text
dangnhap.py
QuanLySinhVien.py
sinhvien.db
```

### Bước 3: Chạy chương trình

Mở terminal hoặc command prompt tại thư mục chứa source code, sau đó chạy:

```bash
python dangnhap.py
```

Nếu máy dùng lệnh `python3`, chạy:

```bash
python3 dangnhap.py
```

## 7. Hướng dẫn sử dụng

Sau khi chạy chương trình, nhập tài khoản mẫu để đăng nhập.

Ví dụ:

```text
Tên đăng nhập: admin
Mật khẩu: admin123
```

Sau khi đăng nhập thành công, chương trình sẽ mở giao diện quản lý sinh viên.

Trong giao diện quản lý, người dùng có thể:

- Nhập thông tin rồi nhấn **Thêm** để thêm sinh viên.
- Chọn sinh viên trong bảng rồi nhấn **Cập nhật** để sửa thông tin.
- Chọn sinh viên rồi nhấn **Xóa** để xóa sinh viên.
- Nhấn **Tìm kiếm** để tìm sinh viên theo mã hoặc họ tên.
- Nhấn **Thống kê** để xem thống kê sinh viên.
- Nhấn nút sắp xếp để sắp xếp theo điểm trung bình hoặc họ tên.

## 8. Cơ sở dữ liệu

Chương trình sử dụng database SQLite với file:

```text
sinhvien.db
```

Bảng dữ liệu chính là `SINH_VIEN`, gồm các trường:

| Tên trường | Kiểu dữ liệu | Ghi chú |
|---|---|---|
| MaSV | TEXT | Khóa chính |
| MatKhau | TEXT | Mật khẩu đăng nhập |
| HoTen | TEXT | Họ tên sinh viên |
| NgaySinh | TEXT | Ngày sinh |
| GioiTinh | TEXT | Giới tính |
| Lop | TEXT | Lớp |
| DiemTB | REAL | Điểm trung bình |

Nếu chưa có dữ liệu, chương trình sẽ tự tạo bảng và thêm một số tài khoản mẫu để đăng nhập.

## 9. Một số lỗi thường gặp

### Không mở được giao diện quản lý

Nguyên nhân có thể do file quản lý chưa đúng tên. Cần đảm bảo file có tên:

```text
QuanLySinhVien.py
```

### Không tìm thấy database

Cần đảm bảo file `sinhvien.db` nằm cùng thư mục với `dangnhap.py` và `QuanLySinhVien.py`.

### Không chạy được lệnh Python

Kiểm tra Python bằng lệnh:

```bash
python --version
```

hoặc:

```bash
python3 --version
```

## 10. Thành viên thực hiện

- Nhóm thực hiện: **Nhóm 6**
- Đề tài: **Xây dựng hệ thống quản lý sinh viên bằng Python và SQLite**

## 11. Kết luận

Chương trình Quản lý sinh viên giúp quản lý thông tin sinh viên ở mức cơ bản, phù hợp cho bài tập môn học và thực hành Python với cơ sở dữ liệu SQLite.
