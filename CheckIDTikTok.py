import os, sys, time, math, random, colorsys
from colorama import init

init(autoreset=True)

# ─────────── CLEAR MÀN HÌNH ───────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ─────────── HỆ MÀU CẦU VỒNG ───────────
def hsv2rgb(h, s, v):
    return colorsys.hsv_to_rgb(h, s, v)

def rgb_to_ansi(r, g, b):
    return 16 + (36 * round(r * 5)) + (6 * round(g * 5)) + round(b * 5)

def smooth_rainbow(length, offset=0, brightness=1.0, saturation=0.9, phase_offset=0):
    return [rgb_to_ansi(*hsv2rgb(((i + offset) / (length * 1.2) + phase_offset) % 1.0, saturation, brightness)) for i in range(length)]

# ─────────── ÁNH SÁNG QUÉT DÒNG LOGO ───────────
def gradient_line(text, colors, light_sweep_pos=None, glow_strength=1.0):
    result = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        distance = abs(i - light_sweep_pos) if light_sweep_pos is not None else 1000
        if distance < 3:
            result += f"\033[1m\033[38;5;{color}m{char}\033[0m"
        else:
            result += f"\033[38;5;{color}m{char}"
    return result + "\033[0m"

# ─────────── HIỆU ỨNG NHỊP THỞ ───────────
def render_logo_wave(frame, intensity=1):
    output = ""
    pulse = 0.5 + 0.5 * math.sin(frame * 0.06)
    brightness = 0.85 + 0.15 * pulse
    saturation = 0.88 + 0.1 * pulse
    sweep_pos = int((math.sin(frame * 0.1) + 1) * (max_logo_length // 2))
    phase_offset = math.sin(frame * 0.03) * 0.2
    for i, line in enumerate(logo_lines):
        shift = frame + i * intensity
        colors = smooth_rainbow(len(line), shift, brightness, saturation, phase_offset)
        output += gradient_line(line, colors, light_sweep_pos=sweep_pos, glow_strength=1.2) + "\n"
    return output

# ─────────── HIỆN BANNER ANIMATION ───────────
def animated_banner(frames=40, delay=0.045):
    start_offset = random.randint(0, 100)
    for f in range(frames):
        clear()
        print(render_logo_wave(f + start_offset))
        time.sleep(delay)

# ─────────── LOGO TOOL ───────────
logo_lines = [
   "████████╗███╗░░░███╗  ██╗  ███╗░░██╗██████╗░██╗░░██╗  ██╗",
   "╚══██╔══╝████╗░████║  ╚═╝  ████╗░██║██╔══██╗██║░██╔╝  ██║",
   "░░░██║░░░██╔████╔██║  ░░░  ██╔██╗██║██║░░██║█████═╝░  ██║",
   "░░░██║░░░██║╚██╔╝██║  ░░░  ██║╚████║██║░░██║██╔═██╗░  ╚═╝",
   "░░░██║░░░██║░╚═╝░██║  ██╗  ██║░╚███║██████╔╝██║░╚██╗  ██╗",
   "░░░╚═╝░░░╚═╝░░░░░╚═╝  ╚═╝  ╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝  ╚═╝"
]

# ─────────── KHỞI CHẠY ───────────
max_logo_length = max(len(line) for line in logo_lines)
animated_banner()



import os
from colorama import Fore, Style, init

init(autoreset=True)

try:
    import ms4
except ImportError:
    os.system('pip install ms4==2.10.0')
    os.system("clear")

from ms4 import InfoTik

nguoi_dung = input(Fore.CYAN + Style.BRIGHT + '⚡ ID TikTok: ').strip()

thong_tin = InfoTik.TikTok_Info(nguoi_dung)

if 'bad' in thong_tin['status']:
    print(Fore.RED + Style.BRIGHT + ' ❌ Tên người dùng không hợp lệ!')
elif 'ok' in thong_tin['status']:
    def get_info(key, default="⚠️ Không có dữ liệu!"):
        return str(thong_tin.get(key, default)).strip()

    ten = get_info('name')
    nguoi_theo_doi = get_info('followers')
    dang_theo_doi = get_info('following')
    luot_thich = get_info('like')
    so_video = get_info('video')
    co = get_info('flag')
    quoc_gia = get_info('country')
    ngay_tao = get_info('Date')
    ma_so = get_info('id')
    tieu_su = get_info('bio')

    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f'''
          
\033[32m══════════════════════════════════════════════════════════      
{Fore.YELLOW}[>_<] THÔNG TIN TÀI KHOẢN{Fore.LIGHTWHITE_EX}        
\033[32m══════════════════════════════════════════════════════════                                 
{Fore.GREEN}[>_<] 👤 Tên người dùng:{Fore.WHITE} {nguoi_dung}   
\033[32m══════════════════════════════════════════════════════════                 
{Fore.GREEN}[>_<] ☃️  Tên hiển thị:{Fore.WHITE} {ten}                                 
\033[32m══════════════════════════════════════════════════════════                                                   
{Fore.GREEN}[>_<] 👥  Người theo dõi:{Fore.WHITE} {nguoi_theo_doi}                               
{Fore.GREEN}[>_<] 🔄  Đang theo dõi:{Fore.WHITE} {dang_theo_doi}                              
\033[32m══════════════════════════════════════════════════════════                                         
{Fore.GREEN}[>_<] ❤️ Lượt thích:{Fore.WHITE} {luot_thich}                                                  
{Fore.GREEN}[>_<] 🎞️  Số video:{Fore.WHITE} {so_video}                                            
\033[32m══════════════════════════════════════════════════════════                                             
{Fore.GREEN}[>_<] 🚩  Cờ:{Fore.WHITE} {co}                                  
{Fore.GREEN}[>_<] 🌍  Quốc gia:{Fore.WHITE} {quoc_gia}                         
{Fore.GREEN}[>_<] 📅  Ngày tạo:{Fore.WHITE} {ngay_tao}      
{Fore.GREEN}[>_<] 🆔  ID:{Fore.WHITE} {ma_so}               
\033[32m═══════════════════════════════════════════════════════════
{Fore.GREEN}[>_<] 📜  Tiểu sử:{Fore.WHITE} {tieu_su}                 
\033[32m═══════════════════════════════════════════════════════════  

Người Tạo ⚙ : DangKhoa_Dev
''')
