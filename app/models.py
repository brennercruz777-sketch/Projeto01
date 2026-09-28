from django.db import models

class Vaga(models.Model):
    MODALIDADE_CHOICES = [
        ('Remoto', 'Remoto'),
        ('Híbrido', 'Híbrido'),
        ('Presencial', 'Presencial'),
    ]

    titulo_vaga = models.CharField(max_length=200)
    empresa = models.CharField(max_length=150)
    modalidade = models.CharField(max_length=20, choices=MODALIDADE_CHOICES, default='Remoto')
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    requisitos = models.TextField()
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo_vaga} - {self.empresa}"