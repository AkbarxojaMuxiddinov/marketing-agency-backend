from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")

    class Meta:
        abstract = True


class Service(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Xizmat nomi")
    description = models.TextField(verbose_name="Xizmat tavsifi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Xizmat narxi")

    def __str__(self):
        return self.title


class Portfolio(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Loyiha nomi")
    image = models.ImageField(upload_to="portfolio/", verbose_name="Loyiha rasmi")
    project_url = models.URLField(blank=True, null=True, verbose_name="Loyiha havolasi")

    def __str__(self):
        return self.title


class Client(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="Mijoz nomi")
    logo = models.ImageField(
        upload_to="clients/",
        blank=True,
        null=True,
        verbose_name="Mijoz logotipi",
    )
    website = models.URLField(blank=True, null=True, verbose_name="Sayt havolasi")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Ko'rsatish tartibi")
    is_active = models.BooleanField(default=True, verbose_name="Saytda ko'rsatilsin")

    class Meta:
        ordering = ("sort_order", "name")
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"

    def __str__(self):
        return self.name


class SocialLink(TimeStampedModel):
    PLATFORM_CHOICES = [
        ("instagram", "Instagram"),
        ("telegram", "Telegram"),
    ]

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES,
        unique=True,
        verbose_name="Ijtimoiy tarmoq",
    )
    url = models.URLField(verbose_name="Profil havolasi")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Ko'rsatish tartibi")
    is_active = models.BooleanField(default=True, verbose_name="Saytda ko'rsatilsin")

    class Meta:
        ordering = ("sort_order", "platform")
        verbose_name = "Ijtimoiy tarmoq havolasi"
        verbose_name_plural = "Ijtimoiy tarmoq havolalari"

    def __str__(self):
        return self.get_platform_display()


class Lead(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Mijoz ismi")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami")
    message = models.TextField(verbose_name="Xabari")
    is_processed = models.BooleanField(default=False, verbose_name="Ko'rib chiqilganmi?")

    def __str__(self):
        return f"{self.name} - {self.phone}"
