sudo docker restart app-admin
sudo docker exec app-db psql -U postgres -c "drop database python_ni_app"
sudo docker exec app-db psql -U postgres -c "create database python_ni_app"
sudo docker exec app-admin python manage.py migrate
