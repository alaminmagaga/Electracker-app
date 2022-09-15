# Generated by Django 4.1 on 2022-09-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsArticle",
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
                ("newspaper", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Business", "Business"),
                            ("Cars", "Cars"),
                            ("Entertainment", "Entertainment"),
                            ("Family", "Family"),
                            ("Health", "Health"),
                            ("Politics", "Politics"),
                            ("Religion", "Religion"),
                            ("Science", "Science"),
                            ("Sports", "Sports"),
                            ("Technology", "Technology"),
                            ("Travel", "Travel"),
                            ("Video", "Video"),
                            ("World", "World"),
                        ],
                        default="Politics",
                        max_length=100,
                    ),
                ),
                ("news_text", models.CharField(max_length=5000)),
                ("label", models.CharField(default="Fake", max_length=10)),
            ],
        ),
    ]
