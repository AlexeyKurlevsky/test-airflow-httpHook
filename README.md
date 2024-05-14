В проекте используется Python 3.10. Запуск проекта:
```commandline
sh ./bin/start_project.sh
```

Генерация FERNET CODE
```python
from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()
print(fernet_key.decode())
```