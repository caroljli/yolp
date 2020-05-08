# yolp
Yelp for students.

  Note that I'm aware that this isn't the exact project outlined in my proposal, but hopefully this didn't cause any trouble.

## Overview
Yolp is Yelp, but for students on college campuses. Restaurants are organized by their location on campuses and students can easily navigate, review, and follow restaurants they care about.

**Presentation video:** can be viewed here: https://drive.google.com/file/d/1_e1OGSvGDWY9_bWsCo295A8Hhx2bc1Ge/view?usp=sharing

## Packages and Project Requirements
**First Party Packages:** this projects uses `datetime`, `sqlite3`, `string`, `json`, and built-in standard types.

* Note: packages are referenced from https://docs.python.org/3/library/

**Third Party Packages:** this project uses `django` and `geopy`.

**Classes:** contains many Django classes, including but not limited to `Student`, `Restaurant`, and `RestaurantAdmin`. Each contains own magic methods.

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
