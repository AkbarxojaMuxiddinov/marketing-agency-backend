from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agency", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Yaratilgan vaqti",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        verbose_name="O'zgartirilgan vaqti",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Mijoz nomi"),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="clients/",
                        verbose_name="Mijoz logotipi",
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True,
                        null=True,
                        verbose_name="Sayt havolasi",
                    ),
                ),
                (
                    "sort_order",
                    models.PositiveIntegerField(
                        default=0,
                        verbose_name="Ko'rsatish tartibi",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        verbose_name="Saytda ko'rsatilsin",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mijoz",
                "verbose_name_plural": "Mijozlar",
                "ordering": ("sort_order", "name"),
            },
        ),
    ]
