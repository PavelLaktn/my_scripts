#-*- encoding: utf-8 -*-

from pathlib import Path
import zipfile
import datetime

def do_backup(directory_for_backup, backups_directory, directories = []):

    # Функция обходит необходимые директории и добавляет в список найденные файлы
    def find_files(directory_for_backup):
        for item in directory_for_backup.iterdir():
            if item.is_file():
                files.append(str(directory_for_backup) + "\\" + item.name)
                continue
            if item.name in directories:
                find_files(item)
                
    # Путь к директории, которую нужно заархивировать
    directory_for_backup = directory_for_backup
    # Путь к диретории, куда нужно положить архив (бэкап)
    backups_directory = backups_directory
    # Список вложенных директорий, которые нужно архивировать (добавить бэкап)
    directories = directories
    #Список файлов для архивирования (бэкапа)
    files = []
    # Найти все файлы для архивирования (бэкапа) и добавить в список
    find_files(directory_for_backup)
    # Записать все файлы из списка в архив (бэкап) с текущей датой и временем в имени
    date_time =  datetime.datetime.now()
    with zipfile.ZipFile(backups_directory + "\\" + date_time.strftime("%d-%m-%Y %H-%M") + ".zip", 'w') as backup_zip:
        for name in files:
            print(datetime.datetime.now().strftime("%d-%m-%Y %H-%M") + f" Start writing {name}...", end = '')
            backup_zip.write(name)
            print(" done", end='\n')
    # Сообщить о выполнении архивирования (бэкапа)
    print("done")
            
def main():
    # Путь к директории, которую нужно заархивировать
    directory_for_backup = Path("C:\\1C Base")
    # Путь к диретории, куда нужно положить архив (бэкап)
    backups_directory = "D:\\Backups\\CLOUD\\1C"
    # Список вложенных директорий, которые нужно архивировать (добавить в бэкапа)
    directories = ["BUH", "TP"]
    do_backup(directory_for_backup, backups_directory, directories)

if __name__ == "__main__":
    main()
