# Python 3.8 - LocalLibrary - Estudo do Django 3 - do site mozilla.org

LocalLibrary

Para configurar o projeto, clone este repositório 

>> git clone https://github.com/emersonccf/projeto_mozilla

e faça a criação de um ambiente virtual, 

>> python -m venv ve
ou
>> pyton3 -m venv ve

ative-o 

>> ve\Scripts\activate 
ou 
>> source ve/bin/activate

e depois instale a relação de dependências que constam na pasta e arquivo -> requirements.txt com o comando: 

>> pip install -r requirements.txt

Assim todas as dependencias serão instaladas.

Realize as migrações (cria o banco de dados e suas tabelas):

>> python manage.py migrate

Crie o um super usuário para administra o sistema:

>> python manage.py createsuperuser

---


