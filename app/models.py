from django.db import models


class Ramais(models.Model):
    SETORES = [
        ('Tecnologia da Informação', 'Tecnologia da Informação'),
        ('Recursos Humanos', 'Recursos Humanos'),
        ('Financeiro', 'Financeiro'),
        ('Administrativo', 'Administrativo'),
    ]

    nome = models.CharField(max_length=100, blank=True)
    ramal = models.CharField(max_length=4, blank=True)
    setor = models.CharField(max_length=100, blank=True, choices=SETORES)
    maquina = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.ramal}'

    class Meta:
        ordering = ['nome']
        verbose_name = 'Ramal'
        verbose_name_plural = 'Ramais'
