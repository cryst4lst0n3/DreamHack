import pycurl
from io import BytesIO
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.MD5())

# 2. Hàm callback để xử lý dữ liệu khi nó đổ về từ server
def write_and_hash(data):
    # Tương đương EVP_DigestUpdate: Cập nhật dữ liệu vào mã băm ngay lập tức
    digest.update(data)
    # Nếu bạn vẫn muốn lưu file thì ghi vào file tại đây, 
    # nhưng không nên ghi vào BytesIO nếu file là .mp4 lớn.
    with open("data.mp4","wb") as f:
        f.write(data)
    return len(data)

c = pycurl.Curl()
c.setopt(c.URL,"https://dn720307.ca.archive.org/0/items/kikTXNL6MvX6ZpRXM/kikTXNL6MvX6ZpRXM.mp4" )
c.setopt(c.FOLLOWLOCATION, 1)
c.setopt(c.USERAGENT, "M")

# THAY ĐỔI QUAN TRỌNG: Dùng WRITEFUNCTION thay vì WRITEDATA vào buffer
c.setopt(c.WRITEFUNCTION, write_and_hash)

c.setopt(c.CONNECTTIMEOUT, 300) 
c.setopt(c.TIMEOUT, 300)

# Thực hiện tải (Dữ liệu sẽ được băm ngay khi đang tải)
c.perform()
c.close()

# 3. Kết thúc băm (Tương đương EVP_DigestFinal)
res = digest.finalize()
