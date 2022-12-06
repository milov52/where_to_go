Проект представляет сайт афишу, на котором представлены интересные места с их подробным описанием.
В данном проекте реализован следующий функционал:
* Получение информации об интересном месте на карте, с возможностью зуммирования и просмотра детальной информации
* Добавление через панель администратора новых локаций с изображениями, координатами и дополнительной информации

## Используемые технологии
* Python 3.7
* Django 2.2
## Установка проекта
Клонируйте данный репозиторий на свой компьютер и перейдите в папку проекта.
<pre><code>git clone https://github.com/milov52/where_to-go.git</code>
<code>cd where_to-go</code></pre>
Создайте и активируйте виртуальное окружение:
<pre><code>python -m venv venv</code>
<code>source venv/Scripts/activate  #для Windows</code>
<code>source env/bin/activate       #для Linux и macOS</code></pre>
Установите требуемые зависимости:
<pre><code>pip install -r requirements.txt</code></pre>
Примените миграции:
<pre><code>python manage.py migrate</code></pre>
Запустите django-сервер:
<pre><code>python manage.py runserver</code></pre>
