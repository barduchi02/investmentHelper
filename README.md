# Investment Helper
A Django project that helps investors to monitor B3 actives, and let them know when to buy or sell monitored actives.

# Requirements
1. **Numpy** package (pip install numpy)
2. **APScheduler** package (pip install APScheduler)
3. A PostgreSQL database. The "scripts.sql" file needs to be used to populate this db (after the python manage.py migrate command is run)

# Observation
The **settings.py** file was omitted from GitHub because it contains the author's personal information. The **settings_mock.py** file contains an exemple settings file with the information necessary to create the settings.py that the project needs. In this file, please complete the fields with the "<FIELD_DESCRIPTION>" (Ex.: <DATABASE_NAME>) notation and rename it to **settings.py** before runnig the project.
