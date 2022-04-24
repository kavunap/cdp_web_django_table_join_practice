`books` テーブルで、タイトルが "PythonBook" であるユーザーを抽出する方法は以下の通りです。この場合、 [`prefetch_related`](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#prefetch-related "doc")` を使用します。

```
>>> users=User.objects.prefetch_related('books').filter(books__title="PythonBook")
>>> users
<QuerySet [<User: Alice>]>
>>> print(users.query)
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" INNER JOIN "book_book" ON ("auth_user"."id" = "book_book"."user_id") WHERE "book_book"."title" = PythonBook
```

- [`prefetch_related`](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#prefetch-related "doc")