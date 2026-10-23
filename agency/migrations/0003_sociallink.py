from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agency", "0002_client"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialLink",
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
                    "platform",
                    models.CharField(
                        choices=[("instagram", "Instagram"), ("telegram", "Telegram")],
                        max_length=20,
                        unique=True,
                        verbose_name="Ijtimoiy tarmoq",
                    ),
                ),
                (
                    "url",
                    models.URLField(verbose_name="Profil havolasi"),
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
                "verbose_name": "Ijtimoiy tarmoq havolasi",
                "verbose_name_plural": "Ijtimoiy tarmoq havolalari",
                "ordering": ("sort_order", "platform"),
            },
        ),
    ]
