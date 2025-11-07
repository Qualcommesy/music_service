import tkinter as tk
from tkinter import messagebox
from DBCommands import add_user, pass_user


class BetaLogin:  # Экран входа
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(self.root, bg='#121212')

        self.setup_ui()

    def setup_ui(self):
        # Интерфейс экрана входа
        # Основной контейнер
        main_container = tk.Frame(self.frame, bg='#121212')
        main_container.pack(expand=True)

        # Логотип
        tk.Label(main_container, text="Beta", font=('Arial', 32, 'bold'),
                 fg='#1DB954', bg='#121212').pack(pady=(0, 40))

        # Заголовок
        tk.Label(main_container, text="Войдите в свой аккаунт",
                 font=('Arial', 18, 'bold'), fg='white', bg='#121212').pack(pady=(0, 30))

        # Поля ввода
        input_frame = tk.Frame(main_container, bg='#121212')
        input_frame.pack(pady=(0, 20))

        # Email
        email_frame = tk.Frame(input_frame, bg='#121212')
        email_frame.pack(fill='x', pady=(0, 15))

        self.email_entry = self.create_entry_with_placeholder(
            email_frame, "Электронная почта или имя пользователя")

        # Пароль
        password_frame = tk.Frame(input_frame, bg='#121212')
        password_frame.pack(fill='x', pady=(0, 15))

        self.password_entry = self.create_entry_with_placeholder(
            password_frame, "Пароль", show="•")

        # Кнопка входа
        login_button = tk.Button(main_container, text="ВОЙТИ", bg='#1DB954', fg='black',
                                 font=('Arial', 12, 'bold'), width=20, height=2,
                                 command=self.login)
        login_button.pack(pady=20)

        # Разделитель
        self.create_separator(main_container, "или")


        # Ссылка "Забыли пароль?"
        forgot_link = tk.Label(main_container, text="Забыли пароль?",
                               font=('Arial', 10, 'underline'), fg='#B3B3B3', bg='#121212',
                               cursor='hand2')
        forgot_link.pack(pady=(20, 0))
        forgot_link.bind("<Button-1>", lambda e: self.forgot_password())

        # Разделительная линия
        tk.Frame(main_container, height=1, bg='#535353').pack(fill='x', pady=(30, 20))

        # Ссылка на регистрацию
        register_label = tk.Label(main_container,
                                  text="Ещё нет аккаунта? Зарегистрироваться в Beta",
                                  font=('Arial', 10, 'underline'), fg='#B3B3B3', bg='#121212',
                                  cursor='hand2')
        register_label.pack()
        register_label.bind("<Button-1>", lambda e: self.app.show_register_screen())

    def create_entry_with_placeholder(self, parent, placeholder, show=None):
        # Поле ввода с placeholder
        # Поле ввода
        entry = tk.Entry(parent, font=('Arial', 12), width=30,
                         fg='#FFFFFF', bg='#121212', insertbackground='#FFFFFF',
                         show=show)
        entry.pack(fill='x', ipady=8)

        # Подчеркивание
        tk.Frame(parent, height=1, bg='#535353').pack(fill='x')

        # Фокус
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

        return entry

    def create_separator(self, parent, text):
        # Разделитель с текстом
        separator_frame = tk.Frame(parent, bg='#121212')
        separator_frame.pack(fill='x', pady=10)

        separator_label = tk.Label(separator_frame, text=text, font=('Arial', 10),
                                   fg='#B3B3B3', bg='#121212', padx=10)
        separator_label.pack()

        # Линии по бокам
        line1 = tk.Frame(separator_frame, height=1, bg='#535353')
        line1.pack(fill='x', side='left', expand=True)
        line2 = tk.Frame(separator_frame, height=1, bg='#535353')
        line2.pack(fill='x', side='right', expand=True)


    def login(self):
        # Обработка входа (в процессе)
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Проверка на placeholder
        if (email == "Электронная почта или имя пользователя" or
                password == "Пароль"):
            messagebox.showerror("Ошибка", "Пожалуйста, введите email и пароль")
            return

        if not email or not password:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля")
            return

        # Авторизация пользователя.
        if pass_user(email, password) == True:
            messagebox.showinfo('Успешно вошел.')
        elif pass_user(email, password) == False:
            messagebox.showinfo('Произошла ошибка.')





        print(f"Логин: {email}, Пароль: {'*' * len(password)}")
        messagebox.showinfo("Успех", "Вход выполнен успешно!")
        self.app.show_main_screen()

    def forgot_password(self):
        # Восстановление пароля
        messagebox.showinfo("Восстановление пароля",
                            "Функция восстановления пароля будет реализована позже")

    def show(self):
        # Показ экрана
        self.frame.pack(fill='both', expand=True)

    def hide(self):
        # Закрытие экрана
        self.frame.pack_forget()


class BetaReg:
    # Экран регистрации
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(self.root, bg='#121212')

        self.setup_ui()

    def setup_ui(self):
        # Интерфейс экрана регистрации
        # Основной контейнер
        main_container = tk.Frame(self.frame, bg='#121212')
        main_container.pack(expand=True)

        # Логотип
        tk.Label(main_container, text="Beta", font=('Arial', 32, 'bold'),
                 fg='#1DB954', bg='#121212').pack(pady=(0, 30))

        # Заголовок
        tk.Label(main_container, text="Зарегистрируйтесь в Beta",
                 font=('Arial', 18, 'bold'), fg='white', bg='#121212').pack(pady=(0, 25))

        # Поля ввода
        input_frame = tk.Frame(main_container, bg='#121212')
        input_frame.pack(pady=(0, 20))

        # Email
        email_frame = tk.Frame(input_frame, bg='#121212')
        email_frame.pack(fill='x', pady=(0, 12))

        tk.Label(email_frame, text="Электронная почта", font=('Arial', 10),
                 fg='#B3B3B3', bg='#121212').pack(anchor='w')

        self.email_entry = tk.Entry(email_frame, font=('Arial', 12), width=30,
                                    fg='#FFFFFF', bg='#121212', insertbackground='#FFFFFF')
        self.email_entry.pack(fill='x', ipady=6)
        tk.Frame(email_frame, height=1, bg='#535353').pack(fill='x')

        # Пароль
        password_frame = tk.Frame(input_frame, bg='#121212')
        password_frame.pack(fill='x', pady=(0, 12))

        tk.Label(password_frame, text="Пароль", font=('Arial', 10),
                 fg='#B3B3B3', bg='#121212').pack(anchor='w')

        self.password_entry = tk.Entry(password_frame, font=('Arial', 12), width=30,
                                       show="•", fg='#FFFFFF', bg='#121212',
                                       insertbackground='#FFFFFF')
        self.password_entry.pack(fill='x', ipady=6)
        tk.Frame(password_frame, height=1, bg='#535353').pack(fill='x')

        # Подтверждение пароля
        confirm_frame = tk.Frame(input_frame, bg='#121212')
        confirm_frame.pack(fill='x', pady=(0, 12))

        tk.Label(confirm_frame, text="Подтвердите пароль", font=('Arial', 10),
                 fg='#B3B3B3', bg='#121212').pack(anchor='w')

        self.confirm_password_entry = tk.Entry(confirm_frame, font=('Arial', 12), width=30,
                                               show="•", fg='#FFFFFF', bg='#121212',
                                               insertbackground='#FFFFFF')
        self.confirm_password_entry.pack(fill='x', ipady=6)
        tk.Frame(confirm_frame, height=1, bg='#535353').pack(fill='x')

        # Имя пользователя
        username_frame = tk.Frame(input_frame, bg='#121212')
        username_frame.pack(fill='x', pady=(0, 12))

        tk.Label(username_frame, text="Имя пользователя", font=('Arial', 10),
                 fg='#B3B3B3', bg='#121212').pack(anchor='w')

        self.username_entry = tk.Entry(username_frame, font=('Arial', 12), width=30,
                                       fg='#FFFFFF', bg='#121212', insertbackground='#FFFFFF')
        self.username_entry.pack(fill='x', ipady=6)
        tk.Frame(username_frame, height=1, bg='#535353').pack(fill='x')

        # Кнопка регистрации
        register_button = tk.Button(main_container, text="ЗАРЕГИСТРИРОВАТЬСЯ",
                                    bg='#1DB954', fg='black', font=('Arial', 12, 'bold'),
                                    width=25, height=2, command=self.register)
        register_button.pack(pady=20)

        # Ссылка на вход
        login_label = tk.Label(main_container,
                               text="Уже есть аккаунт? Войти в Beta",
                               font=('Arial', 10, 'underline'), fg='#B3B3B3', bg='#121212',
                               cursor='hand2')
        login_label.pack(pady=10)
        login_label.bind("<Button-1>", lambda e: self.app.show_login_screen())

    def register(self):
        # Обработка регистрации
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        username = self.username_entry.get()

        # Проверка
        if not all([email, password, confirm_password, username]):
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все обязательные поля")
            return

        if password != confirm_password:
            messagebox.showerror("Ошибка", "Пароли не совпадают")
            return

        if len(password) < 8:
            messagebox.showerror("Ошибка", "Пароль должен содержать минимум 8 символов")
            return
        
        # Проверка при регистрации пользователя.
        if add_user(email, password) == True:
            messagebox.showinfo("Успех", "Регистрация завершена успешно!")
            self.app.show_main_screen()
        elif add_user(email, password) == 3:
            messagebox.showinfo('На этой почте зарегистрирован аккаунт.')
        elif add_user(email, password) == False:
            messagebox.showinfo('Произошла ошибка.')

    def show(self):
        # Показ экрана
        self.frame.pack(fill='both', expand=True)

    def hide(self):
        # Закрытие экрана
        self.frame.pack_forget()

class BetaMain:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(self.root, bg='#121212')

        self.setup_ui()

    def setup_ui(self):
        # Интерфейс главного экрана"""
        # Верхняя панель
        top_frame = tk.Frame(self.frame, bg='#121212')
        top_frame.pack(fill='x', padx=20, pady=10)

        tk.Label(top_frame, text="Beta", font=('Arial', 24, 'bold'),
                 fg='#1DB954', bg='#121212').pack(side='left')

        # Кнопка выхода
        logout_button = tk.Button(top_frame, text="Выйти", font=('Arial', 10),
                                  fg='white', bg='#535353', border=0,
                                  command=self.app.show_login_screen)
        logout_button.pack(side='right')

        # Основной контент
        content_frame = tk.Frame(self.frame, bg='#121212')
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Приветствие
        tk.Label(content_frame, text="Добро пожаловать!", font=('Arial', 20, 'bold'),
                 fg='white', bg='#121212').pack(pady=(0, 30))

        # Рекомендуемые плейлисты(макет)
        tk.Label(content_frame, text="Рекомендуемые плейлисты", font=('Arial', 16, 'bold'),
                 fg='white', bg='#121212').pack(anchor='w', pady=(0, 15))

        playlists = [
            "Мой плейлист #1", "Любимые треки", "Для работы",
            "Расслабление", "Тренировка", "Зарубежные хиты"
        ]

        for playlist in playlists:
            playlist_frame = tk.Frame(content_frame, bg='#181818')
            playlist_frame.pack(fill='x', pady=5, padx=10)

            tk.Label(playlist_frame, text=playlist, font=('Arial', 12),
                     fg='white', bg='#181818').pack(side='left', padx=10, pady=8)

            play_button = tk.Button(playlist_frame, text="▶", font=('Arial', 10),
                                    fg='black', bg='#1DB954', width=3,
                                    command=lambda p=playlist: self.play_music(p))
            play_button.pack(side='right', padx=10, pady=5)

    def play_music(self, playlist):
        # Запуск воспроизведения плейлиста
        print(f"Воспроизведение: {playlist}")
        self.app.show_player_screen()

    def show(self):
        # Показ экрана
        self.frame.pack(fill='both', expand=True)

    def hide(self):
        # Закрытие экрана
        self.frame.pack_forget()

class BetaPlayer:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(self.root, bg='#121212')

        self.setup_ui()

    def setup_ui(self):
        # Интерфейс экрана плеера
        # Верхняя панель
        top_frame = tk.Frame(self.frame, bg='#121212')
        top_frame.pack(fill='x', padx=20, pady=10)

        # Кнопка назад
        back_button = tk.Button(top_frame, text="← Назад", font=('Arial', 10),
                                fg='white', bg='#535353', border=0,
                                command=self.app.show_main_screen)
        back_button.pack(side='left')

        tk.Label(top_frame, text="Сейчас играет", font=('Arial', 16, 'bold'),
                 fg='white', bg='#121212').pack(side='left', padx=20)

        # Основной контент
        content_frame = tk.Frame(self.frame, bg='#121212')
        content_frame.pack(fill='both', expand=True)

        # Обложка альбома
        album_frame = tk.Frame(content_frame, bg='#121212')
        album_frame.pack(pady=50)

        # Заглушка для обложки
        album_cover = tk.Frame(album_frame, width=200, height=200, bg='#333333')
        album_cover.pack()
        album_cover.pack_propagate(False)

        tk.Label(album_cover, text="🎵", font=('Arial', 40),
                 bg='#333333', fg='white').pack(expand=True)

        # Информация о треке
        track_info_frame = tk.Frame(content_frame, bg='#121212')
        track_info_frame.pack(pady=20)

        tk.Label(track_info_frame, text="Название трека", font=('Arial', 18, 'bold'),
                 fg='white', bg='#121212').pack()
        tk.Label(track_info_frame, text="Исполнитель", font=('Arial', 14),
                 fg='#B3B3B3', bg='#121212').pack(pady=5)

        # Прогресс трека
        progress_frame = tk.Frame(content_frame, bg='#121212')
        progress_frame.pack(fill='x', padx=50, pady=20)

        tk.Label(progress_frame, text="0:00", fg='#B3B3B3', bg='#121212').pack(side='left')

        progress_bar = tk.Frame(progress_frame, height=4, bg='#535353')
        progress_bar.pack(fill='x', expand=True, padx=10)

        # Прогресс (заполненная часть)
        progress_fill = tk.Frame(progress_bar, height=4, bg='#1DB954', width=100)
        progress_fill.pack(side='left')

        tk.Label(progress_frame, text="3:45", fg='#B3B3B3', bg='#121212').pack(side='right')

        # Элементы управления
        controls_frame = tk.Frame(content_frame, bg='#121212')
        controls_frame.pack(pady=30)

        # Кнопки управления
        buttons = [
            ("🔀", "#1DB954"),  # Shuffle
            ("⏮", "#1DB954"),  # Previous
            ("⏸", "#1DB954"),  # Play/Pause
            ("⏭", "#1DB954"),  # Next
            ("🔁", "#1DB954")  # Repeat
        ]

        for text, color in buttons:
            button = tk.Button(controls_frame, text=text, font=('Arial', 16),
                               fg='black', bg=color, border=0, width=3, height=1)
            button.pack(side='left', padx=10)

    def show(self):
        # Показ экрана
        self.frame.pack(fill='both', expand=True)

    def hide(self):
        # Закрытие экрана
        self.frame.pack_forget()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Beta")
        self.root.geometry("800x600")
        self.root.configure(bg='#121212')

        # Создаем экземпляры всех окон
        self.login_screen = BetaLogin(self.root, self)
        self.register_screen = BetaReg(self.root, self)
        self.main_screen = BetaMain(self.root, self)
        self.player_screen = BetaPlayer(self.root, self)

        # Показываем начальный экран
        self.show_login_screen()

    def show_login_screen(self):
        # Показ экрана входа
        self.hide_all_screens()
        self.login_screen.show()

    def show_register_screen(self):
        # Показ экрана регистрации
        self.hide_all_screens()
        self.register_screen.show()

    def show_main_screen(self):
        # Показ основного экрана
        self.hide_all_screens()
        self.main_screen.show()

    def show_player_screen(self):
        # Показ экрана проигрывателя
        self.hide_all_screens()
        self.player_screen.show()

    def hide_all_screens(self):
        # Закрытие всех экранов
        self.login_screen.hide()
        self.register_screen.hide()
        self.main_screen.hide()
        self.player_screen.hide()


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()