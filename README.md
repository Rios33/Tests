Проект с тестами для сайта saucedemo.com

Запуск:

1) cd C:\Users\Имя пользователя\...\Папка с проектом
2) docker build -t test .
3) docker run --rm test

Должно показать что все 5 тестов прошли.

Тесты:

- вход с правильным логином и паролем (standard_user, secret_sauce)
  
- вход с неправильным паролем
  
- вход заблокированного пользователя (locked_out_user)
  
- вход с пустыми полями
  
- вход пользователя performance_glitch_user (там есть задержки, но должен войти)

результаты тестов:

все 5 тестов проходят, время выполнения ~20 секунд

- tests/test_login.py::TestLogin::test_success_login PASSED

- tests/test_login.py::TestLogin::test_wrong_password PASSED  

- tests/test_login.py::TestLogin::test_locked_user PASSED

- tests/test_login.py::TestLogin::test_empty_fields PASSED

- tests/test_login.py::TestLogin::test_performance_user PASSED

============================== 5 passed in 19.52s ==============================

Файлы:

- login_page.py - тут методы для страницы логина
  
- inventory_page.py - тут проверки для страницы после логина
  
- test_login.py - сами тесты (их 5)
  
- conftest.py - настройка для запуска тестов (фикстура)
  
- Dockerfile - чтоб в контейнере запускать
  
- requirements.txt - библиотеки (playwright, pytest и т.д.)

Всё, тесты работают.
