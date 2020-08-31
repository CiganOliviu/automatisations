import os

project_name = input("What's the name of the project: ")

os.system("composer create-project --prefer-dist laravel/laravel " + project_name)

os.system("php artisan serve")