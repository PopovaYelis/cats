# ИНСТРУКЦИИ ПО ЗАПУСКУ FASTAPI cats

1. У вас должен быть установлен docker compose
    - Вводим команду docker compose up (если для docker нет прав перед командой введите sudo)
2. Можно работать через POSTMAN либо через документацию SWAGGER (далее буду рассказывать про swagger)
    - Для запуска документации и проверки роутов перейдите по [ссылкe](http://0.0.0.0:5000/docs)

### Описание выполненной работы
1. Реальзованно FASTAPI cats для просмотра, изменения, удаления информации про котят
2. Взаимодействие с БД реализовано через orm SQLAlchemy
3. База данных postgresql
4. Приложение обернуто в Dockerfile
5. Для быстрого запуска командлй {docker compose up} приложение обернуто в Docker-compose.yaml, 


### Описание роутов и взаимодействие с ними через SWAGGER
#### Для проверки выбираем соответсвующие роуты и нажимаем TRY

1. GET /cats - список всех котят
   - execute (если не добавили котов, то ожидаемые ответ 404, Cat not found)
3. GET /breeds - список всех пород
   - execute (если не добавили породы, то ожидаемые ответ 404, Breed not found)
5. GET /cats/one/{cat_id} - информация об одном котенке по id
   - вводим обязательный параметр {cat_id}, далее execute (если не добавили котов, то ожидаемые ответ 404, Cat not found)
7. GET /cats/{breed_name} - список котят с породо {breed_name}
   - вводим обязательный параметр {breed_name} далее execute (если не добавили котов, то ожидаемые ответ 404, Cat not found)
9. POST /cats - добавление котенка
    -вводим обязательные параметры {cat_name: str, age: int, color: str, description: str, breed_id: int} далее execute (если не породы с {breed_id}, то ожидаемые ответ 404, Breed not found)
11. POST /breed - добавление породы
   -вводим обязательные параметры {name: str} далее execute
13. PATCH /cats - частичное/полное изменение информации о котенке
    - вводим обязательный параметр {cat_id}, вводим необязательные параметры в формате json, которые хотим изменить, далее execute (если кота с таким id нет, то ожидаемые ответ 404, Cat not found)
15. DELETE /cats - удаление котенка
    - вводим обязательный параметр {cat_id} которые хотим изменить, далее execute (если кота с таким id нет, то ожидаемые ответ 404, Cat not found)


![image](https://github.com/user-attachments/assets/0646840c-6d09-45f1-97d8-18b2deb849f2)
