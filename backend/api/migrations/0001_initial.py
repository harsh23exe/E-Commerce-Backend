from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor): 
        user = CustomUser(name="Harsh", 
                          email="harsh23exe@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="7506149022",
                          gender="Male")
        user.set_password("harsh23exe")
        user.save()

    dependencies=[

    ]
    operations=[migrations.RunPython(seed_data)]