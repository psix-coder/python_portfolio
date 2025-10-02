# 🎮 Interactive Terminal Portfolio

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![CLI](https://img.shields.io/badge/interface-CLI-orange.svg)

> Terminal/konsolda ishlaydigan interaktiv va rangdor Python portfolio dasturi

## 📖 Loyiha haqida

Interactive Terminal Portfolio - bu Python da yaratilgan to'liq interaktiv konsol ilovasi. Loyiha terminal'da ishlaydigan zamonaviy portfolio ko'rinishini taqdim etadi va foydalanuvchi bilan o'zaro aloqada bo'ladi. Matrix animatsiyalar, typewriter effektlari va mini o'yinlar bilan jihozlangan.

## ✨ Asosiy xususiyatlar

### 🎨 Visual Effects
- ✅ **Matrix Animation** - Dastur boshlanishida Matrix effekti
- ✅ **Typewriter Effect** - Matnlarni harfma-harf chiqarish
- ✅ **Colored Output** - ANSI ranglar yordamida rangli matn
- ✅ **Progress Bars** - Ko'nikmalar darajasini ko'rsatish
- ✅ **ASCII Art** - Portfolio banner
- ✅ **Box Drawing** - Ramkalar va chiziqlar

### 📋 Portfolio Sections
- 👤 **Men haqimda** - Shaxsiy ma'lumotlar
- 💼 **Loyihalar** - Loyihalar ro'yxati va tavsif
- 🛠️ **Ko'nikmalar** - Progress bar bilan ko'nikmalar
- 📊 **Statistika** - GitHub statistikalari
- 🎮 **Mini O'yin** - Son topish o'yini
- 📞 **Kontakt** - Aloqa ma'lumotlari

### 🎯 Interaktiv Xususiyatlar
- ✅ **Menu Navigation** - Oson navigatsiya
- ✅ **User Input** - Foydalanuvchi kiritishi
- ✅ **Game Logic** - O'yin mexanikasi
- ✅ **Dynamic Content** - Dinamik kontent
- ✅ **Cross-platform** - Barcha OS'larda ishlaydi

## 🛠️ Texnologiyalar

<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</div>

**Pure Python:**
- Python 3.6+ (standard library)
- `sys` - System operatsiyalari
- `os` - OS interface
- `time` - Vaqt bilan ishlash
- `random` - Tasodifiy sonlar

**Hech qanday tashqi kutubxona kerak emas!** ✨

## 🚀 O'rnatish va ishlatish

### Talablar

```
Python 3.6 yoki yuqori versiya
```

### Qadamlar

1. **Repository'ni clone qiling:**
```bash
git clone https://github.com/psix-coder/python-portfolio.git
cd python-portfolio
```

2. **Dasturni ishga tushiring:**
```bash
# Python 3 bilan
python3 main.py

# Yoki Windows'da
python main.py

# Yoki executable sifatida (Linux/Mac)
chmod +x main.py
./main.py
```

**Bu hammasi!** Hech qanday qo'shimcha paket o'rnatish kerak emas! 🎉

## 📁 Loyiha strukturasi

```
python-portfolio/
├── python/
│   └── main.py           # Asosiy dastur
└── README.md             # Dokumentatsiya
```

## 💻 Interfeys va funksiyalar

### Asosiy menyu

```
┌─────────────────────────────────┐
│     ASOSIY MENYU                │
├─────────────────────────────────┤
│  1. 👤 Men haqimda              │
│  2. 💼 Loyihalar                │
│  3. 🛠️  Ko'nikmalar              │
│  4. 📊 Statistika               │
│  5. 🎮 Mini O'yin               │
│  6. 📞 Kontakt                  │
│  0. 🚪 Chiqish                  │
└─────────────────────────────────┘
```

### Xususiyatlar

#### 1. Matrix Effect
Dastur boshlanganida Matrix filmidagi kabi animatsiya:
```python
01010101001010101010101
10101010101010010101010
01010101001010101010101
```

#### 2. Typewriter Effect
Matnlar harfma-harf ekranga chiqadi, inson yozayotgandek:
```
👨‍💻 Ism: Aziz Programmer
📍 Joylashuv: Toshkent, O'zbekiston
```

#### 3. Progress Bars
Ko'nikmalar vizual progress bar bilan:
```
Python              : [████████████████████████░░░░] 95%
Django/FastAPI      : [███████████████████████░░░░░] 90%
```

#### 4. Mini O'yin
Son topish o'yini - 7 urinishda 1-100 oralig'idagi sonni topish:
```
Men 1 dan 100 gacha son o'yladim. Topishga harakat qiling!

Taxminingiz (7 urinish qoldi): 50
⬆️  Kattaroq son kiriting
```

## 🎨 ANSI Ranglar

Dastur quyidagi ranglardan foydalanadi:

| Rang | Kod | Ishlatilishi |
|------|-----|-------------|
| 🟢 Green | `\033[92m` | Matrix, muvaffaqiyat |
| 🔵 Cyan | `\033[96m` | Asosiy matn |
| 🟡 Yellow | `\033[93m` | Menyu, ogohlantirishlar |
| 🟣 Magenta | `\033[95m` | Sarlavhalar |
| 🔴 Red | `\033[91m` | Xatolar |
| 🔷 Blue | `\033[94m` | Progress bars |

## 📋 Kod strukturasi

### Portfolio Class

```python
class Portfolio:
    def __init__(self):
        # ANSI ranglarni saqlash
        
    def clear(self):
        # Konsolni tozalash
        
    def typewriter(self, text, delay=0.03, color='green'):
        # Typewriter effekti
        
    def matrix_effect(self, duration=2):
        # Matrix animatsiyasi
        
    def draw_box(self, text, color='cyan'):
        # Ramka chizish
        
    def progress_bar(self, title, percentage, color='blue'):
        # Progress bar ko'rsatish
        
    def show_banner(self):
        # ASCII art banner
        
    def show_menu(self):
        # Asosiy menyu
        
    def about_me(self):
        # Men haqimda
        
    def projects(self):
        # Loyihalar ro'yxati
        
    def skills(self):
        # Ko'nikmalar bilan progress bars
        
    def statistics(self):
        # GitHub statistika
        
    def mini_game(self):
        # Son topish o'yini
        
    def contact(self):
        # Kontakt ma'lumotlari
        
    def run(self):
        # Asosiy loop
```

## 🎯 Foydalanish misoli

```bash
$ python3 main.py

# Matrix animatsiyasi ko'rsatiladi...

╔═══════════════════════════════════════════════╗
║                                               ║
║     ██████╗  ██████╗ ██████╗ ████████╗       ║
║     ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝       ║
║     ██████╔╝██║   ██║██████╔╝   ██║          ║
║     ██╔═══╝ ██║   ██║██╔══██╗   ██║          ║
║     ██║     ╚██████╔╝██║  ██║   ██║          ║
║     ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝          ║
║                                               ║
║          PYTHON DASTURCHI PORTFOLIOSI         ║
║                                               ║
╚═══════════════════════════════════════════════╝

# Menyu ko'rsatiladi...
Tanlang (0-6): 3

# Ko'nikmalar ko'rsatiladi...
Python              : [█████████████████████████░░] 95%
Django/FastAPI      : [████████████████████████░░░] 90%
```

## ⚙️ Moslashtirish

### O'z ma'lumotlaringizni qo'shish:

1. **`about_me()` funksiyasini tahrirlang:**
```python
info = [
    "👨‍💻 Ism: Sizning Ismingiz",
    "📍 Joylashuv: Sizning shahringiz",
    # ...
]
```

2. **`projects()` funksiyasini yangilang:**
```python
projects = [
    {
        "name": "🌐 Sizning loyihangiz",
        "desc": "Tavsif",
        "tech": "Texnologiyalar",
        "stars": 10
    }
]
```

3. **`contact()` ma'lumotlarini o'zgartiring:**
```python
contacts = [
    "📧 Email: sizning@email.com",
    "🐙 GitHub: github.com/username",
    # ...
]
```

## 🌍 Cross-platform Qo'llab-quvvatlash

Dastur Windows, Linux va macOS'da ishlaydi:

- ✅ **Windows** - PowerShell, CMD
- ✅ **Linux** - Bash, Zsh, Fish
- ✅ **macOS** - Terminal

**Eslatma:** Ba'zi terminal'lar ANSI ranglarni qo'llab-quvvatlamaydi. Windows CMD'da ranglar to'g'ri ishlamasligi mumkin (PowerShell yaxshiroq).

## 🎮 Mini O'yin Qoidalari

**Son topish o'yini:**
1. Kompyuter 1 dan 100 gacha son o'ylaydi
2. Sizda 7 ta urinish bor
3. Har urinishdan keyin "kattaroq" yoki "kichikroq" yordam beriladi
4. Topasiz - yutdingiz! 🎉
5. 7 urinishda topa olmasangiz - yutqazdingiz 😢

## 📈 Kelajakdagi yangilanishlar

- [ ] Boshqa o'yinlar qo'shish (Guess the word, Calculator)
- [ ] File'dan ma'lumotlarni o'qish (JSON/YAML config)
- [ ] Multilanguage support (EN/UZ/RU)
- [ ] Export to HTML/PDF
- [ ] GitHub API integration (real statistics)
- [ ] More animations va effects
- [ ] Sound effects (opsional)
- [ ] Configuration file
- [ ] Plugin system
- [ ] Web version (Flask/Django)

## 🤝 Hissa qo'shish

1. Fork qiling
2. Feature branch yarating
3. Commit qiling
4. Push qiling
5. Pull Request oching

**O'zingizning effektlaringizni qo'shing!** 🎨

## 📝 Litsenziya

MIT License - erkin foydalanishingiz mumkin!

## 👤 Muallif

**Psix Coder**

- GitHub: [@psix-coder](https://github.com/psix-coder)
- Repository: [Python Portfolio](https://github.com/psix-coder/python-portfolio)

## 🌟 Ilhom

Bu loyiha quyidagilardan ilhomlangan:
- Matrix film
- Retro terminal interfaces
- CLI application best practices

## 📚 O'rganish materiallari

Bu loyihadan nima o'rganish mumkin:
- Python OOP (Classes)
- ANSI escape codes
- Terminal manipulation
- User input handling
- Game logic
- Animation techniques

## 🎓 O'quv maqsadlari uchun

Bu dastur Python o'rganayotgan talabalar uchun ajoyib misol:
- ✅ Clean code
- ✅ Object-oriented programming
- ✅ User interaction
- ✅ Visual effects
- ✅ Cross-platform development

---

<div align="center">

**⭐ Agar yoqsa, star qo'ying! ⭐**

Made with ❤️ and Pure Python by [Psix Coder](https://github.com/psix-coder)

🎮 **Interactive Terminal Portfolio - Code with Style!**

</div>
