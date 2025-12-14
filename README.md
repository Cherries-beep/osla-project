OSLA Test Project

Небольшой Django + DRF сервис для трекинга объектов строительства. Репозиторий используется как база для тестового задания.

Быстрый старт

1. Создайте виртуальное окружение и активируйте его:
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

2. Установите зависимости:
pip install -r requirements.txt

3. Примените миграции:
python manage.py migrate

4. Запустите сервер:
python manage.py runserver 0.0.0.0:8000

5. Проверка работы API:

Перейдите в браузере: http://127.0.0.1:8000/building/ — список объектов строительства.
Создайте объект через POST с organization_ids: [1,2].
GET /building/buildings/{id}/organizations/ — убедитесь, что организации связаны с объектом.


Через Docker

1. Соберите и запустите проект одной командой:
docker compose up --build

2. Сервер будет доступен на http://localhost:8000/

3. Миграции выполняются автоматически при сборке контейнера

4. Для остановки и удаления контейнеров:
docker compose down



## Расширенная функциональность

### Новая модель Organization
**Поля:**
- `name` (CharField, max_length=255) - название организации, минимум 2 символа
- `employees_count` (PositiveIntegerField) - количество сотрудников, диапазон 1-100000
- `external_id` (CharField, max_length=255, unique=True) - уникальный идентификатор организации
- `created_at` (DateTimeField, auto_now_add=True) - дата создания
- `updated_at` (DateTimeField, auto_now=True) - дата последнего обновления

**Валидация:**
- Название должно содержать минимум 2 символа (после удаления пробелов)
- Количество сотрудников должно быть в диапазоне от 1 до 100000
- External ID не может быть пустым



## Связь Building-Organization
Один объект строительства может быть связан с несколькими организациями (Many-to-Many связь).  
Одна организация может работать на нескольких объектах строительства.

**Поле связи:** `organizations` (ManyToManyField в модели Building)



### API Endpoints

#### Организации
- `GET /building/organizations/` - список с фильтрацией по name, external_id, employees_count
- `POST /building/organizations/` - создание
- `GET/PUT/PATCH/DELETE /building/organizations/{id}/` - детали, обновление, удаление

#### Объекты строительства
- `GET /building/buildings/` - список с фильтрацией по name, entity, organizations
- `POST /building/buildings/` - создание (передать `organization_ids: [1, 2]`)
- `GET/PUT/PATCH/DELETE /building/buildings/{id}/` - детали, обновление, удаление

#### Управление связями (дополнительно)
- `GET /building/buildings/{id}/organizations/` - получить организации объекта
- `POST /building/buildings/{id}/organizations/{org_id}/` - добавить связь
- `DELETE /building/buildings/{id}/organizations/{org_id}/` - удалить связь