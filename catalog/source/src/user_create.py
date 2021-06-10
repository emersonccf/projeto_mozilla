from django.contrib.auth.models import User

# cria superusuario (username, email, password)
user = User.objects.create_superuser('admin2', '', 'admin2')

# cria usuario (username, email, password)
user = User.objects.create_user('ana', '', 'ana')
