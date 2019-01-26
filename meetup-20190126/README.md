## Iniciar Admin local ##

```
sudo docker-compose up

```

## Crear base de datos vacia ##

```
sh ./reset_db.sh
sudo docker exec -it app-admin bash

# en el bash del container

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
```
