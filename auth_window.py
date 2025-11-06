import tkinter as tk
from tkinter import ttk, messagebox
import sys


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Blue Frost - Вход")
        # width = root.winfo_screenwidth()
        # height = root.winfo_screenheight()
        # self.root.geometry(f"{width}x{height}")
        # self.root.attributes('-fullscreen', True)
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg='#121212')
        
        # Центрирование окна
        self.center_window()
        
        self.setup_ui()
        
    def center_window(self):
        """Центрирует окно на экране"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_ui(self):
        """Создает интерфейс входа"""
        # Основной фрейм
        main_frame = tk.Frame(self.root, bg='#121212')
        main_frame.pack(fill='both', expand=True, padx=50, pady=40)
        
        # Логотип Spotify
        logo_label = tk.Label(
            main_frame,
            text="Blue Frost",
            font=('Arial', 32, 'bold'),
            fg='#1DB954',
            bg='#121212'
        )
        logo_label.pack(pady=(0, 40))
        
        # Заголовок
        title_label = tk.Label(
            main_frame,
            text="Войдите в свой аккаунт",
            font=('Arial', 18, 'bold'),
            fg='#FFFFFF',
            bg='#121212'
        )
        title_label.pack(pady=(0, 30))
        
        # Поле для email/username
        self.create_input_field(main_frame, "Электронная почта или имя пользователя", "email")
        
        # Поле для пароля
        self.create_input_field(main_frame, "Пароль", "password", show="•")
        
        
        # Кнопка входа
        login_button = tk.Button(
            main_frame,
            text="ВОЙТИ",
            font=('Arial', 12, 'bold'),
            fg='#121212',
            bg='#1DB954',
            activebackground='#1ED760',
            activeforeground='#121212',
            border=0,
            cursor='hand2',
            width=20,
            height=2,
            command=self.Login
        )
        login_button.pack(pady=30)
        
        # Разделитель
        separator_frame = tk.Frame(main_frame, bg='#121212')
        separator_frame.pack(fill='x', pady=20)
        
        separator_label = tk.Label(
            separator_frame,
            text="или",
            font=('Arial', 10),
            fg='#B3B3B3',
            bg='#121212',
            padx=10
        )
        separator_label.pack()
        
        # Линия перед текстом
        line1 = tk.Frame(separator_frame, height=1, bg='#535353')
        line1.pack(fill='x', side='left', expand=True)
        line2 = tk.Frame(separator_frame, height=1, bg='#535353')
        line2.pack(fill='x', side='right', expand=True)
        
        # Ссылка "Забыли пароль?"
        forgot_link = tk.Label(
            main_frame,text="Забыли пароль?",
            font=('Arial', 10, 'underline'),
            fg='#B3B3B3',
            bg='#121212',
            cursor='hand2'
        )
        forgot_link.pack(pady=(0, 0))
        forgot_link.bind("<Button-1>", lambda e: self.forgot_password())
        
        
        # Ссылка на регистрацию
        register_label = tk.Label(
            main_frame,
            text="Ещё нет аккаунта? Зарегистрироваться в Blue Frost",
            font=('Arial', 10, 'underline'),
            fg='#B3B3B3',
            bg='#121212',
            cursor='hand2'
        )
        register_label.pack()
        register_label.bind("<Button-1>", lambda e: self.register())
    
    def create_input_field(self, parent, placeholder, field_type, show=None):
        """Создает поле ввода с placeholder"""
        frame = tk.Frame(parent, bg='#121212')
        frame.pack(fill='x', pady=(0, 15))
        
        entry = tk.Entry(
            frame,
            font=('Arial', 12),
            fg='#FFFFFF',
            bg='#121212',
            insertbackground='#FFFFFF',
            relief='flat',
            show=show
        )
        entry.pack(fill='x', ipady=8)
        
        # Подчеркивание
        underline = tk.Frame(frame, height=1, bg='#535353')
        underline.pack(fill='x')
        
        # Placeholder functionality
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg='#FFFFFF')
        
        def on_focus_out(event):
            if entry.get() == '':
                entry.insert(0, placeholder)
                entry.config(fg='#B3B3B3')
        
        entry.insert(0, placeholder)
        entry.config(fg='#B3B3B3')
        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)
        
        # Сохраняем ссылку на поле ввода
        if field_type == "email":
            self.email_entry = entry
        elif field_type == "password":
            self.password_entry = entry
    
    def create_social_button(self, parent, text, bg_color, fg_color="#FFFFFF"):
        """Создает кнопку для входа через социальные сети"""
        button = tk.Button(
            parent,
            text=text,
            font=('Arial', 10, 'bold'),
            fg=fg_color,
            bg=bg_color,
            activebackground=bg_color,
            border=0,
            cursor='hand2',
            width=30,
            height=2,
            command=lambda: self.social_login(text)
        )
        button.pack(pady=5)
    
    def Login(self):
        """Обрабатывает попытку входа"""
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        # Проверка на placeholder значения
        if email == "Электронная почта или имя пользователя" or password == "Пароль":
            messagebox.showerror("Ошибка", "Пожалуйста, введите email и пароль")
            return
        
        if not email or not password:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля")
            return
        
        # Здесь должна быть логика аутентификации
        print(f"Логин: {email}, Пароль: {'*' * len(password)}")
        
        # Временное сообщение об успехе
        messagebox.showinfo("Успех", "Вход выполнен успешно!")
    
    def social_login(self, provider):
        """Обрабатывает вход через социальные сети"""
        print(f"Вход через: {provider}")
        messagebox.showinfo("Социальный вход", f"Перенаправление на {provider}")
    def forgot_password(self):
        """Обрабатывает восстановление пароля"""
        messagebox.showinfo("Восстановление пароля", "Функция восстановления пароля")
    
    def register(self):
        """Обрабатывает переход к регистрации"""
        messagebox.showinfo("Регистрация", "Переход к регистрации")


class Reg():
    def __init__(self, root):
        self.root = root
        self.root.title("Blue Frost - Регистрация")
        self.root.geometry(f"600x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#121212')
        


class App():
    def __init__(self, root):
        self.root = root
        self.root.title("Blue Frost")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.root.configure(bg='#121212')

        self.login_window = Login(root)
        self.reg_window = Reg(root)

        self.show_login()

    def show_login(self):
        self.login_window.setup_ui()


        

        
        

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()