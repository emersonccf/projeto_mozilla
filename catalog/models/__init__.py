from django.db import models
from django.utils import timezone # não utilizado
from django.contrib.auth.models import User
from django.urls import reverse # Usado para gerar URLs revertendo os padrões de URL em Book
import uuid # Utilizado em BookIstance

LOAN_STATUS = (
    ('m', 'Manutenção'),
    ('e', 'Emrestado'),
    ('d', 'Disponível'),
    ('r', 'Reservado'),
)

from .genre import Genre
from .book import Book
from .bookinstance import BookInstance
from .author import Author
from .language import Language