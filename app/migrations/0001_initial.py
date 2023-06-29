# Generated by Django 4.2.2 on 2023-06-29 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id_proyecto', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
                ('fecha_de_publicacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuariocliente',
            fields=[
                ('id_cliente', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='subir_proyecto',
            fields=[
                ('id_subidaProyecto', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo_proyecto', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='directorio/')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuariocliente')),
            ],
        ),
        migrations.CreateModel(
            name='proyecto_categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
                ('id_proyecto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='id_vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuariocliente'),
        ),
    ]
