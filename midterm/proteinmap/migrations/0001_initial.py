# Generated by Django 3.0.3 on 2023-07-14 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('taxa_id', models.IntegerField(primary_key=True, serialize=False)),
                ('clade', models.CharField(max_length=2)),
                ('genus', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pfam',
            fields=[
                ('pfam_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('protein_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('length', models.IntegerField()),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proteinmap.Organism')),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('protein', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='proteinmap.Protein')),
                ('sequence', models.CharField(blank=True, max_length=40000)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('start', models.IntegerField()),
                ('stop', models.IntegerField()),
                ('pfam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proteinmap.Pfam')),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proteinmap.Protein')),
            ],
        ),
    ]