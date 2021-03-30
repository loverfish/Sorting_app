##### Данное web-приложение имеет следующие возможности:

1. Сортировать загруженный файл, одним из предложенных методов сортировки 
2. Генерировать файл с несортированными числами 
3. Показывать и хранить результаты последних вызовов
4. Считать время выполнения сортировки
5. В панели администратора добавлены следующие функции:
  * фильтрация по типу алгоритма
  * сортировка по любому полю модели
  * поиск

##### Установка:

1. клонировать проект (git clone...)
2. скачать и настроить postgresql:
  * скачать:    
    sudo apt install postgresql postgresql-contrib 
  * Открываем консоль PostgreSQL под стандартным пользователем postgres 
    sudo -u postgres psql postgres
  * Задаем пароль администратора БД  
    \password postgres
  * Создаем и настраиваем пользователя при помощи которого будем
    соединяться с базой данных из Django (ну очень плохая практика все
    делать через ... суперпользователя). Заодно указываем значения по 
    умолчанию для кодировки, уровня изоляции транзакций и временного пояса.  
    create user user_name with password 'password';  
    alter role user_name set client_encoding to 'utf8';  
    alter role user_name set default_transaction_isolation to 'read committed';  
    alter role user_name set timezone to 'UTC';
  * Создаем базу для нашего проекта  
    create database django_db owner user_name;
  * Выходим из консоли  
    \q
  * В окружении проекта устанавливаем бэкэнд для PostgreSQL  
    pip install psycopg2    (для mac pip install psycopg2-binary)
  * Последний наш шаг - настроить раздел DATABASES конфигурационного файла
    проекта settings.py 
    'ENGINE': 'django.db.backends.postgresql_psycopg2',  
    'NAME': 'django_db',  
    'USER' : 'user_name',  
    'PASSWORD' : 'password',  
    'HOST' : '127.0.0.1',  
    'PORT' : '5432',
 3. активируем виртуальную среду и устанавливаем пакеты из requirements.txt   
 4. создаем суперпользователя для доступа к панели администратора
 5. в settings.py указываем собственный SECRET_KEY

##### Приложение готово к использованию
  
