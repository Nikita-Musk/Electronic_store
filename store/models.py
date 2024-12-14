from django.db import models


class Network(models.Model):
    LEVEL_CHOICES = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=200, verbose_name="Название")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.PositiveIntegerField(verbose_name="Номер дома")
    level = models.IntegerField(choices=LEVEL_CHOICES)
    supplier = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Поставщик",
        blank=True,
        null=True,
    )
    debt = models.DecimalField(
        max_digits=20, verbose_name="Задолженность", default=0.00, decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сеть"
        verbose_name_plural = "Сети"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    model = models.CharField(max_length=200, verbose_name="Модель продукта")
    launch_date = models.DateField(verbose_name="Дата выхода продукта на рынок")
    supplier = models.ForeignKey(
        Network, on_delete=models.CASCADE, verbose_name="Поставщик"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
