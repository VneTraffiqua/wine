# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Подготовьте Exel файл с продукцией (*Файлы с изображениями размещайте в папке `images`*). Пример таблицы:

![Пример Exel-файла](https://i.ibb.co/Cm9jXJm/Example.png")

#### [EXEL ФАЙЛ С ПРИМЕРА](https://github.com/VneTraffiqua/wine/blob/master/wine.xlsx?raw=true)
- Установите зависимости командой:
``` bash
pip install -r requirements.txt
```
- Создайте файл конфигурации `.env` с параметрами:
  - `FILE_PATH=`<*Путь к xls-файлу или название xls-файла (Если он находится в дирректории с исполняемым файлом `main.py`)*>
  - `SHEET_NAME=`<*Имя листа таблицы*>
  - `WORKING_SINCE=`<*Дата создания винодельни*>


- Запустите сайт командой:

Указав путь к файлу конфигурации `.env`
``` bash 
python3 main.py -e <путь к файлу конфигурации>
``` 
Если файл конфигурации находится в папке с исполняемым файлом `main.py` путь к файлу указывать необязательно. Достаточно выполнить команду:
``` bash 
python3 main.py
```




- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
