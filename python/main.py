#!/usr/bin/env python3
"""
Matritsa Animatsiyali Konsolda Portfolio
Terminal/Konsolda ishlaydigana interaktiv Python dastur
"""

import time
import random
import sys
import os


class Portfolio:
    def __init__(self):
        self.colors = {
            'reset': '\033[0m',
            'green': '\033[92m',
            'cyan': '\033[96m',
            'yellow': '\033[93m',
            'magenta': '\033[95m',
            'red': '\033[91m',
            'blue': '\033[94m',
            'bold': '\033[1m'
        }
        
    def clear(self):
        """Konsolni tozalash"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def typewriter(self, text, delay=0.03, color='green'):
        """Typewriter effekti"""
        for char in text:
            sys.stdout.write(self.colors[color] + char)
            sys.stdout.flush()
            time.sleep(delay)
        print(self.colors['reset'])
        
    def matrix_effect(self, duration=2):
        """Matrix kabi animatsiya"""
        chars = "01" * 50
        for _ in range(duration * 10):
            line = ''.join(random.choice(chars) for _ in range(80))
            print(self.colors['green'] + line + self.colors['reset'])
            time.sleep(0.1)
        self.clear()
        
    def draw_box(self, text, color='cyan'):
        """Matn atrofida ramka chizish"""
        width = len(text) + 4
        print(self.colors[color] + '╔' + '═' * width + '╗')
        print('║  ' + text + '  ║')
        print('╚' + '═' * width + '╝' + self.colors['reset'])
        
    def progress_bar(self, title, percentage, color='blue'):
        """Progress bar ko'rsatish"""
        bar_length = 30
        filled = int(bar_length * percentage / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        print(f"{self.colors[color]}{title}: [{bar}] {percentage}%{self.colors['reset']}")
        
    def show_banner(self):
        """ASCII art banner"""
        banner = """
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
        """
        print(self.colors['cyan'] + self.colors['bold'] + banner + self.colors['reset'])
        time.sleep(1)
        
    def show_menu(self):
        """Asosiy menyu"""
        menu = """
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
        """
        print(self.colors['yellow'] + menu + self.colors['reset'])
        
    def about_me(self):
        """Men haqimda bo'limi"""
        self.clear()
        self.draw_box("MEN HAQIMDA", "magenta")
        print()
        
        info = [
            "👨‍💻 Ism: Aziz Programmer",
            "📍 Joylashuv: Toshkent, O'zbekiston",
            "🎓 Mutaxassislik: Python Backend Developer",
            "💡 Tajriba: 3+ yil dasturlash",
            "🚀 Maqsad: AI va ML sohasida malaka oshirish"
        ]
        
        for item in info:
            self.typewriter(item, 0.02, 'cyan')
            time.sleep(0.3)
        
        print("\n" + self.colors['green'] + "Bio: " + self.colors['reset'])
        bio = "Python va Django yordamida veb-ilovalar yaratish bilan shug'ullanaman. Open-source loyihalarga qiziqaman va o'z bilimlarimni boshqalar bilan bo'lishni yaxshi ko'raman."
        self.typewriter(bio, 0.02, 'reset')
        
    def projects(self):
        """Loyihalar bo'limi"""
        self.clear()
        self.draw_box("MENING LOYIHALARIM", "blue")
        print()
        
        projects = [
            {
                "name": "🌐 Blog Platform",
                "desc": "Django asosida yaratilgan to'liq funksional blog",
                "tech": "Python, Django, PostgreSQL",
                "stars": 45
            },
            {
                "name": "📊 Data Analyzer",
                "desc": "CSV va Excel fayllarni tahlil qiluvchi dastur",
                "tech": "Python, Pandas, Matplotlib",
                "stars": 32
            },
            {
                "name": "🤖 Telegram Bot",
                "desc": "Automatlashtirish uchun Telegram bot",
                "tech": "Python, aiogram, SQLite",
                "stars": 58
            },
            {
                "name": "🎯 Task Manager API",
                "desc": "REST API orqali vazifalarni boshqarish",
                "tech": "FastAPI, MongoDB",
                "stars": 27
            }
        ]
        
        for i, proj in enumerate(projects, 1):
            print(f"{self.colors['yellow']}{'─' * 50}{self.colors['reset']}")
            print(f"{self.colors['bold']}{i}. {proj['name']}{self.colors['reset']}")
            print(f"   {proj['desc']}")
            print(f"   {self.colors['cyan']}Tech:{self.colors['reset']} {proj['tech']}")
            print(f"   {self.colors['yellow']}⭐ {proj['stars']} stars{self.colors['reset']}")
            time.sleep(0.5)
            
    def skills(self):
        """Ko'nikmalar bo'limi"""
        self.clear()
        self.draw_box("KO'NIKMALAR VA TEXNOLOGIYALAR", "green")
        print()
        
        skills = [
            ("Python", 95),
            ("Django/FastAPI", 90),
            ("Git & GitHub", 85),
            ("SQL/PostgreSQL", 80),
            ("Docker", 75),
            ("Linux", 70),
            ("Redis", 65),
            ("Machine Learning", 60)
        ]
        
        for skill, level in skills:
            self.progress_bar(skill.ljust(20), level, 'green')
            time.sleep(0.3)
            
    def statistics(self):
        """Statistika bo'limi"""
        self.clear()
        self.draw_box("GITHUB STATISTIKA", "cyan")
        print()
        
        stats = [
            ("📦 Repositories", "24"),
            ("⭐ Total Stars", "187"),
            ("🔱 Forks", "43"),
            ("👥 Followers", "156"),
            ("📝 Commits (2024)", "847"),
            ("🔥 Streak", "45 kun"),
            ("🏆 Contributions", "1,234")
        ]
        
        for label, value in stats:
            print(f"{self.colors['yellow']}{label.ljust(25)}{self.colors['reset']}: {self.colors['green']}{self.colors['bold']}{value}{self.colors['reset']}")
            time.sleep(0.3)
            
    def mini_game(self):
        """Mini o'yin - Son topish"""
        self.clear()
        self.draw_box("SON TOPISH O'YINI", "magenta")
        print(f"\n{self.colors['cyan']}Men 1 dan 100 gacha son o'yladim. Topishga harakat qiling!{self.colors['reset']}\n")
        
        secret = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"{self.colors['yellow']}Taxminingiz ({max_attempts - attempts} urinish qoldi): {self.colors['reset']}"))
                attempts += 1
                
                if guess == secret:
                    print(f"\n{self.colors['green']}🎉 Tabriklayman! {attempts} urinishda topdingiz!{self.colors['reset']}\n")
                    break
                elif guess < secret:
                    print(f"{self.colors['red']}⬆️  Kattaroq son kiriting{self.colors['reset']}")
                else:
                    print(f"{self.colors['red']}⬇️  Kichikroq son kiriting{self.colors['reset']}")
                    
                if attempts == max_attempts:
                    print(f"\n{self.colors['red']}😢 Urinishlar tugadi! Son {secret} edi.{self.colors['reset']}\n")
            except ValueError:
                print(f"{self.colors['red']}Iltimos, faqat son kiriting!{self.colors['reset']}")
                
    def contact(self):
        """Kontakt ma'lumotlari"""
        self.clear()
        self.draw_box("KONTAKT MA'LUMOTLARI", "yellow")
        print()
        
        contacts = [
            "📧 Email: aziz.dev@example.com",
            "🐙 GitHub: github.com/azizprogrammer",
            "💼 LinkedIn: linkedin.com/in/azizdev",
            "📱 Telegram: @aziz_developer",
            "🌐 Website: azizdev.uz"
        ]
        
        for contact in contacts:
            self.typewriter(contact, 0.02, 'cyan')
            time.sleep(0.3)
            
    def run(self):
        """Dasturni ishga tushirish"""
        self.clear()
        self.matrix_effect(2)
        self.show_banner()
        
        while True:
            self.show_menu()
            choice = input(f"\n{self.colors['green']}Tanlang (0-6): {self.colors['reset']}")
            
            if choice == '1':
                self.about_me()
            elif choice == '2':
                self.projects()
            elif choice == '3':
                self.skills()
            elif choice == '4':
                self.statistics()
            elif choice == '5':
                self.mini_game()
            elif choice == '6':
                self.contact()
            elif choice == '0':
                self.clear()
                self.typewriter("Xayr! Kelganingiz uchun rahmat! 👋", 0.05, 'cyan')
                break
            else:
                print(f"{self.colors['red']}Noto'g'ri tanlov! Qaytadan urinib ko'ring.{self.colors['reset']}")
                time.sleep(1)
                
            input(f"\n{self.colors['yellow']}Davom etish uchun Enter bosing...{self.colors['reset']}")
            self.clear()


if __name__ == "__main__":
    portfolio = Portfolio()
    try:
        portfolio.run()
    except KeyboardInterrupt:
        print("\n\nDastur to'xtatildi. Xayr! 👋")
        sys.exit(0)