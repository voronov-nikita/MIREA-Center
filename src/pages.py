from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel, QFormLayout, QLineEdit
from PyQt5.QtCore import Qt
from styles import STYLES


class ContentPage(QWidget):
    """Базовый класс для всех страниц контента"""
    def __init__(self, title):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.setStyleSheet(STYLES["content"])
        
        self.title = QLabel(title)
        self.title.setStyleSheet(STYLES["title"])
        self.layout.addWidget(self.title)
        
        self.setup_ui()
        self.layout.addStretch()
    
    def setup_ui(self):
        """Метод для настройки UI, должен быть переопределен в дочерних классах"""
        pass


class ServicesPage(ContentPage):
    def __init__(self):
        super().__init__("Сервисы")
    
    def setup_ui(self):
        buttons = [
            ("Расписания", self.show_schedule),
            ("Дисциплины", self.show_disciplines),
            ("Цифровой университет", self.show_digital_university),
            ("ЛКС", self.show_lks),
            ("Сервис инициативных идей студентов", self.show_student_ideas),
            ("Воинская обязанность", self.show_military_duty)
        ]
        
        for text, handler in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(STYLES["content_button"])
            btn.clicked.connect(handler)
            self.layout.addWidget(btn)
    
    def show_schedule(self):
        self.parent().set_content("Расписания", "Здесь будет содержимое раздела Расписания")
    
    def show_disciplines(self):
        self.parent().set_content("Дисциплины", "Здесь будет содержимое раздела Дисциплины")
    
    def show_digital_university(self):
        self.parent().set_content("Цифровой университет", "Здесь будет содержимое раздела Цифровой университет")
    
    def show_lks(self):
        self.parent().set_content("ЛКС", "Здесь будет содержимое раздела ЛКС")
    
    def show_student_ideas(self):
        self.parent().set_content("Сервис инициативных идей студентов", "Здесь будет содержимое раздела Сервис инициативных идей студентов")
    
    def show_military_duty(self):
        self.parent().set_content("Воинская обязанность", "Здесь будет содержимое раздела Воинская обязанность")


class MyClassesPage(ContentPage):
    def __init__(self):
        super().__init__("Мои занятия")
    
    def setup_ui(self):
        buttons = [
            ("Сервисы", self.show_services),
            ("Настройки", self.show_settings),
            ("Таланов М. А.", self.show_teacher)
        ]
        
        for text, handler in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(STYLES["content_button"])
            btn.clicked.connect(handler)
            self.layout.addWidget(btn)
    
    def show_services(self):
        self.parent().set_content("Сервисы", "Здесь будет содержимое раздела Сервисы (из Мои занятия)")
    
    def show_settings(self):
        self.parent().show_settings_page()
    
    def show_teacher(self):
        self.parent().set_content("Таланов М. А.", "Здесь будет информация о преподавателе Таланов М. А.")


class InstructionsPage(ContentPage):
    def __init__(self):
        super().__init__("Инструкция")
    
    def setup_ui(self):
        buttons = [
            ("БРС", self.show_brs),
            ("Судебный портал дист. обучения", self.show_court_portal),
            ("Справочник студента", self.show_student_guide),
            ("Студенческий офис", self.show_student_office),
            ("Преподаватель", self.show_teacher),
            ("Информационный библиотечный центр", self.show_library),
            ("Студенческий офис", self.show_student_office_2)
        ]
        
        for text, handler in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(STYLES["content_button"])
            btn.clicked.connect(handler)
            self.layout.addWidget(btn)
    
    def show_brs(self):
        self.parent().set_content("БРС", "Здесь будет инструкция по БРС")
    
    def show_court_portal(self):
        self.parent().set_content("Судебный портал дист. обучения", "Здесь будет инструкция по Судебному порталу дистанционного обучения")
    
    def show_student_guide(self):
        self.parent().set_content("Справочник студента", "Здесь будет Справочник студента")
    
    def show_student_office(self):
        self.parent().set_content("Студенческий офис", "Здесь будет информация о Студенческом офисе")
    
    def show_teacher(self):
        self.parent().set_content("Преподаватель", "Здесь будет инструкция для преподавателей")
    
    def show_library(self):
        self.parent().set_content("Информационный библиотечный центр", "Здесь будет информация о библиотечном центре")
    
    def show_student_office_2(self):
        self.parent().set_content("Студенческий офис 2", "Здесь будет дополнительная информация о Студенческом офисе")


class SettingsPage(ContentPage):
    def __init__(self):
        super().__init__("Настройки")
    
    def setup_ui(self):
        form = QFormLayout()
        form.setSpacing(10)
        
        self.name_edit = QLineEdit()
        self.group_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        
        form.addRow("ФИО:", self.name_edit)
        form.addRow("Группа:", self.group_edit)
        form.addRow("Email:", self.email_edit)
        form.addRow("Телефон:", self.phone_edit)
        
        save_btn = QPushButton("Сохранить")
        save_btn.setStyleSheet(STYLES["content_button"])
        save_btn.clicked.connect(self.save_settings)
        
        self.layout.addLayout(form)
        self.layout.addWidget(save_btn)
    
    def save_settings(self):
        print("Настройки сохранены:")
        print(f"ФИО: {self.name_edit.text()}")
        print(f"Группа: {self.group_edit.text()}")
        print(f"Email: {self.email_edit.text()}")
        print(f"Телефон: {self.phone_edit.text()}")


class ContentDisplay(QWidget):
    """Виджет для отображения контента"""
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.setStyleSheet(STYLES["content"])
        
        self.title = QLabel()
        self.title.setStyleSheet(STYLES["title"])
        self.layout.addWidget(self.title)
        
        self.content = QLabel()
        self.content.setWordWrap(True)
        self.layout.addWidget(self.content)
        self.layout.addStretch()
    
    def set_content(self, title, text):
        self.title.setText(title)
        self.content.setText(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Журнал PTY МИРЭА")
        self.setGeometry(100, 100, 900, 600)
        
        # Создаем центральный виджет и основной макет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Создаем боковую панель
        self.sidebar = QWidget()
        self.sidebar.setStyleSheet(STYLES["sidebar"])
        self.sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setAlignment(Qt.AlignTop)
        sidebar_layout.setSpacing(5)
        sidebar_layout.setContentsMargins(5, 10, 5, 10)
        
        # Создаем кнопки для верхних вкладок
        self.btn_services = QPushButton("Сервисы")
        self.btn_my_classes = QPushButton("Мои занятия")
        self.btn_instructions = QPushButton("Инструкция")
        
        # Настраиваем кнопки
        for btn in [self.btn_services, self.btn_my_classes, self.btn_instructions]:
            btn.setStyleSheet(STYLES["sidebar_button"])
            btn.setFixedHeight(40)
            sidebar_layout.addWidget(btn)
        
        # Добавляем разделитель
        sidebar_layout.addWidget(QLabel())
        sidebar_layout.addWidget(QLabel("Меню"))
        sidebar_layout.addWidget(QLabel())
        
        # Создаем StackedWidget для переключения между разделами
        self.stacked_widget = QStackedWidget()
        
        # Создаем страницы для каждого раздела
        self.services_page = ServicesPage()
        self.my_classes_page = MyClassesPage()
        self.instructions_page = InstructionsPage()
        self.settings_page = SettingsPage()
        self.content_display = ContentDisplay()
        
        # Добавляем страницы в StackedWidget
        self.stacked_widget.addWidget(self.services_page)
        self.stacked_widget.addWidget(self.my_classes_page)
        self.stacked_widget.addWidget(self.instructions_page)
        self.stacked_widget.addWidget(self.settings_page)
        self.stacked_widget.addWidget(self.content_display)
        
        # Устанавливаем начальную страницу
        self.stacked_widget.setCurrentWidget(self.services_page)
        
        # Добавляем боковую панель и StackedWidget в основной макет
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stacked_widget)
        
        # Подключаем кнопки к переключению страниц
        self.btn_services.clicked.connect(self.show_services)
        self.btn_my_classes.clicked.connect(self.show_my_classes)
        self.btn_instructions.clicked.connect(self.show_instructions)
    
    def show_services(self):
        self.stacked_widget.setCurrentWidget(self.services_page)
    
    def show_my_classes(self):
        self.stacked_widget.setCurrentWidget(self.my_classes_page)
    
    def show_instructions(self):
        self.stacked_widget.setCurrentWidget(self.instructions_page)
    
    def show_settings_page(self):
        self.stacked_widget.setCurrentWidget(self.settings_page)
    
    def set_content(self, title, text):
        self.content_display.set_content(title, text)
        self.stacked_widget.setCurrentWidget(self.content_display)
