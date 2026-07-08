from selenium.webdriver.common.by import By

# === СТРАНИЦА РЕГИСТРАЦИИ ===
REG_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле ввода Имени
REG_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода Email
REG_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода Пароля
REG_REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
REG_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" на странице регистрации

# === ГЛАВНАЯ СТРАНИЦА ===
LOGIN_MAIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет" на главной
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ" на главной

# === ФОРМА ВХОДА ===
LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email на форме входа
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле Пароль на форме входа
LOGIN_SIGNIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" на форме входа
LOGIN_REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка "Зарегистрироваться" на форме входа
LOGIN_FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка "Восстановить пароль"

# === ЛИЧНЫЙ КАБИНЕТ ===
PROFILE_CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор" в личном кабинете
PROFILE_LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers
PROFILE_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход" в личном кабинете

# === КОНСТРУКТОР (РАЗДЕЛЫ) ===
CONSTRUCTOR_BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка "Булки"
CONSTRUCTOR_SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка "Соусы"
CONSTRUCTOR_FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка "Начинки"