# wapp_task_manager_flask

Демо приложение. Служит шаблоном для остальных приложений.

## Перед использованием

- Переименовать файл CFILE в build.sh
- Переименовать файл CFILE в release-code.sh
- Переименовать файл SQLALCHEMY_DATABASE_URI в config.py
- Запустить `pyupdater init`

## Вырианты запуска приложения

### flask

```bash
build.sh flask
```

### zipapp

```bash
build.sh zipapp run
```

### pyinstaller

```bash
build.sh pyinst_docker run
```

