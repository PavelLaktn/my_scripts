powershell -file logoff_for_users.ps1 && net stop W3SVC && cd D:\ && python backup.py >> D:\Backups\CLOUD\1C\log_file.%date%.txt && net start W3SVC
