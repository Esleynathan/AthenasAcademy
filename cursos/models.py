from django.db import models

class Cursos(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    thumb = models.ImageField(upload_to = "thumb_cursos")

    def __str__(self) -> str:
        return self.nome

class Aulas(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    aula = models.FileField(upload_to = "aulas")
    curso = models.ForeignKey(Cursos, on_delete = models.DO_NOTHING)


    def __str__(self) -> str:
        return self.nome

class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)
    comentario = models.TextField()
    data = models.DateTimeField(default = datetime.now)
    aula = models.ForeignKey(Aulas, on_delete = models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.usuario.nome