import requests
import os

# Màu
nen_tim = "\033[45m"  # Nền tím
trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
vang = "\033[1;33m\033[1m"
do = "\033[1;31m\033[1m"
hack = f"{nen_tim}     [NGUYENDANGKHOA]{trang} => "

# Banner
banner = f"""
     ╔═══════════════════════════════════════════════════════════════╗
     ║   ████████╗███╗   ███╗  ██╗  ███╗  ██╗██████╗ ██╗  ██╗  ██╗   ║
     ║   ╚══██╔══╝████╗ ████║  ╚═╝  ████╗ ██║██╔══██╗██║ ██╔╝  ██║   ║
     ║      ██║   ██╔████╔██║       ██╔██╗██║██║  ██║█████═╝   ██║   ║
     ║      ██║   ██║╚██╔╝██║       ██║╚████║██║  ██║██╔═██╗   ╚═╝   ║
     ║      ██║   ██║ ╚═╝ ██║  ██╗  ██║ ╚███║██████╔╝██║ ╚██╗  ██╗   ║
     ║      ╚═╝   ╚═╝     ╚═╝  ╚═╝  ╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝  ╚═╝   ║
     ╚═══════════════════════════════════════════════════════════════╝"""
os.system('cls' if os.name == 'nt' else 'clear')
print(banner)

# Nhập link
link = input(f"{hack}NHẬP LINK CẦN RÚT GỌN : {vang}")

# Gọi API của yeumoney
token = "e5ce8b377f21aa9ea4e38d6a55f44d8048189fee5ca75b4963b200b705622dbd"
api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={link}"

try:
    response = requests.get(api_url)
    if response.status_code == 200:
        if response.text.lower().startswith("http"):
            print(f"{hack}{xanh_la}LINK RÚT GỌN CỦA BẠN LÀ: {vang}{response.text}")
        else:
            print(f"{hack}Lỗi: {response.text}")
    else:
        print(f"{hack}Lỗi HTTP: {response.status_code} - {response.text}")
except Exception as e:
    print(f"{hack}Lỗi hệ thống: {e}")
