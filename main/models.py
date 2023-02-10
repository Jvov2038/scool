from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

import users.models


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


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name="Текст")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True, null=True)
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото№2", blank=True, null=True)
    photo3 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото№3", blank=True, null=True)
    photo4 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото№4", blank=True, null=True)
    photo5 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото№5", blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    prog =models.ForeignKey("Prog", on_delete=models.PROTECT, verbose_name="Программа", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Публикации'
        verbose_name_plural = 'Публикации'
        ordering = ['time_create', 'title']


class HomeWork(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name="Содержание")
    pdffile = models.FileField(upload_to="pdf/%Y/%m/%d/", verbose_name="PDF")
    executor = models.ForeignKey(users.models.User, on_delete=models.PROTECT, null=True, verbose_name="Исполнитель")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('homework', kwargs={'title': self.pk})

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'
        ordering = ['time_create']


class CategoryLecture(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории", db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_lecture', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория лекции'
        verbose_name_plural = 'Категории лекций'
        ordering = ['id']


class Lecture(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    URL = models.URLField(blank=True, verbose_name="Ссылка на видео")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey(CategoryLecture, on_delete=models.PROTECT, verbose_name="Категория", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lecture', kwargs={'lecture_slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Лекции'
        verbose_name_plural = 'Лекции'
        ordering = ['time_create', 'title']


class CategoryProg(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории", db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию програмы'
        verbose_name_plural = 'Категории программ'
        ordering = ['id']


class Prog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", null=True, blank=True)
    content = models.TextField(blank=True, verbose_name="Содержание")
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото2", null=True, blank=True)
    selection_procedure = models.TextField(blank=True, null=True, verbose_name="Порядок отбора")
    photo3 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото3", null=True, blank=True)
    selection_procedure2 = models.TextField(blank=True, null=True, verbose_name="Порядок отбора 2 абзац")
    photo4 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото4", null=True, blank=True)
    prog_statement = models.TextField(blank=True, verbose_name="Положение о программе")
    photo5 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото5", null=True, blank=True)
    prog_statement2 = models.TextField(blank=True, verbose_name="Положение о программе 2 абзац")
    pdffile = models.FileField(upload_to="pdf/%Y/%m/%d/", verbose_name="PDF", null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    time_start = models.DateTimeField(verbose_name="Дата и время начала программы", null=True, blank=True)
    time_ending = models.DateTimeField(verbose_name="Дата и время окончания программы", null=True, blank=True)
    is_published = models.BooleanField(verbose_name="Публикация")
    supervisor = models.ForeignKey(users.models.User, on_delete=models.PROTECT, related_name='supervisor', verbose_name="Руководитель",
                                   null=True, blank=True)
    registration = models.ManyToManyField(users.models.User, verbose_name="Участники программы")
    cat = models.ForeignKey(CategoryProg, on_delete=models.PROTECT, verbose_name="Категория", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('program', kwargs={'program_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'
        ordering = ['time_create', 'title']
