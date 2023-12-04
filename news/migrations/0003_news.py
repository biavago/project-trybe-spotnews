# Generated by Django 4.2.3 on 2023-12-04 15:52

from django.db import migrations, models
import django.db.models.deletion
import news.validation


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                    "title",
                    models.CharField(
                        max_length=200,
                        validators=[news.validation.title_validator],
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateField()),
                ("image", models.ImageField(upload_to="img/")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.user",
                    ),
                ),
                ("categories", models.ManyToManyField(to="news.category")),
            ],
        ),
    ]
