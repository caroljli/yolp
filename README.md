# yolp
Yelp for students.

## Overview
Yolp is Yelp, but for students on college campuses. Restaurants are organized by their location on campuses and students can easily navigate, review, and follow restaurants they care about.

## Deployment
To run,

```
cd yolp
pip install requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Modularity

The project is divided into three apps: `restaurant`, `restaurant_admin`, and `student`.
* The `restaurant` app handles Restaurant object creation and actions.
* The `restaurant_admin` app handles RestaurantAdmin object creation and actions.
* The `student` app handles Student object creation and actions, in addition to writing reviews.

## Admin

The admin credentials are (not necessary):
* Username: `admin`
* Password: `password`
