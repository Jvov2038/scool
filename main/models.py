from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name="Текст")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['time_create', 'title']


class Category(models.Model):
     name = models.CharField(max_length=100, verbose_name="Название категории", db_index=True)
     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

     def __str__(self):
         return self.name


     def get_absolute_url(self):
         return reverse('category', kwargs={'cat_slug': self.slug})


     class Meta:
         verbose_name = 'Категория'
         verbose_name_plural = 'Категории'
         ordering = ['id']


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    content = models.TextField(blank=True, verbose_name="Характеристика")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    position_at_work = models.CharField(max_length=255, verbose_name="Должность")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('man', kwargs={'name': self.pk})

    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учителя'
        ordering = ['name']


class HomeWork(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Содержание")
    pdffile = models.FileField(upload_to="pdf/%Y/%m/%d/", verbose_name="PDF")
    executor = models.CharField(max_length=255, verbose_name="Исполнитель")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('homework', kwargs={'title': self.pk})

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'
        ordering = ['time_create']

