from django.db import models


class Heroes(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=150)
    image = models.ImageField(verbose_name="Фото", upload_to="photos/%Y/%m/%d", blank=True)
    description = models.TextField(verbose_name="История", blank=True)
    category = models.ManyToManyField("Category", verbose_name="Категория")
    gender = models.ForeignKey("Gender", verbose_name="Пол", on_delete=models.SET_NULL, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True)
    death_date = models.DateField(verbose_name="Дата смерти", blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обнавления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Герой Ислама"
        verbose_name_plural = "Герои Ислама"


class Category(models.Model):
    title = models.CharField(verbose_name="Категория", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Gender(models.Model):
    title = models.CharField(verbose_name="Пол", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"