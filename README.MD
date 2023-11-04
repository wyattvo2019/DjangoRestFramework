```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
python -m pip install Django
python -m django --version
pip install djangorestframework
pip show djangorestframework

django-admin startproject src .
django-admin startapp car
python manage.py migrate
python manage.py runserver
```
# Create API in this step
## Step 1: Create car model
## Step 2: Create Car Serializer
## Step 3: Create view for create/update/delete
## Step 4: Add url to use view
## Step 5: Add url to main app
## Step 6: Add car app to main app
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

