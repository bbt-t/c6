<p align="right">
  <img alt="" src="https://i.ibb.co/Lpk3tgK/c3-removebg-preview.png" width="300">
</p>

## Курсовая работа по Django

[> ТЗ тут <](https://skyengpublic.notion.site/Django-49b5a442e97a4e3a98b416d6cf3ed9a7)

<details>
<summary>API</summary>

- авторизация по токену и логин-паролю :heavy_check_mark:
- получение токена по логин-паролю :heavy_check_mark:
- получение всех записей клиентов :heavy_check_mark:
- получение всех записей рассылок :heavy_check_mark:

</details>

### Главная согласно ТЗ


<details>
<summary>Blog</summary>

- все статьи :heavy_check_mark:
- конкретная статья :heavy_check_mark:

</details>

<details>
<summary>Переопределена модель пользователя</summary>

- добавлены поля согласно ТЗ :heavy_check_mark:
- регистрация и авторизация :heavy_check_mark:
- подтверждение почты :heavy_check_mark:

</details>

<details>
<summary>Рассылка писем</summary>

- создание клиента :heavy_check_mark:
- просмотр клиентов :heavy_check_mark:

- создание сообщения :heavy_check_mark:
- просмотр сообщений :heavy_check_mark:

- создание рассылки :heavy_check_mark:
- просмотр рассылок :heavy_check_mark:

- просмотр результатов попыток рассылок :heavy_check_mark:

</details>

Функционал менеджера :heavy_check_mark:


> для работы необходимо прописать переменные окружения:

`POSTGRES_PASSWORD`
`POSTGRES_DB`
`POSTGRES_USER`
`REDIS_PASS`
`REDIS_HOST`
`REDIS_PORT`

`SECRET_KEY`

`EMAIL_HOST_USER`
`EMAIL_HOST_PASSWORD`
`EMAIL_HOST`

> и иметь подключение к БД (Postgres && Redis)
