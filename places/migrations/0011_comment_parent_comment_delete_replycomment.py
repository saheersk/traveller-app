# Generated by Django 4.0.4 on 2023-01-22 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_replycomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_comment', to='places.comment'),
        ),
        migrations.DeleteModel(
            name='ReplyComment',
        ),
    ]
