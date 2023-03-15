## About this project

[E-Health Care](https://ehealthcare.netlify.app/) is a web application where users can check their heart condition through this system. If the user's inserted symptoms match the symptoms of a disease, it will advise the associate physician for that disease.

[![image](https://raw.githubusercontent.com/shahriarshafin/e-health-care/main/assets/images/screenshot.png)](https://ehealthcare.netlify.app/)

## Features:

- Search doctor and hospital
- Suggest associate doctor for the disease
- Check heart condition
- Covid-19 live update
- Intelligent searching system

## Build Setup

### Clone

```bash
https://github.com/ingenuity-2-0/ehealthcare-backend.git
cd ehealthcare-backend
```

### Change the working directory

```bash
cd ubot-backend
```

### Install dependencies

```bash
pip insatll -r requirements.txt
```

### Run the app in development mode

```bash
python manage.py migrate
python manage.py runserver
```

That's All! Now open [localhost:8000](http://localhost:5000/) to see the app.

## Dependencies

```
it requires python version >=3.7
asgiref==3.4.1
beautifulsoup4==4.10.0
certifi==2021.5.30
charset-normalizer==2.0.6
Django==3.2.7
idna==3.2
joblib==1.0.1
mysqlclient==2.0.3
numpy==1.21.2
pandas==1.3.3
Pillow==8.3.1
python-dateutil==2.8.2
pytz==2021.1
requests==2.26.0
scikit-learn==1.0
scipy==1.7.1
six==1.16.0
soupsieve==2.2.1
sqlparse==0.4.1
threadpoolctl==2.2.0
urllib3==1.26.7

python-dotenv~=0.19.1
```


## Build Setup ( front-end )

[https://github.com/ingenuity-2-0/ehealthcare_frontend](https://github.com/ingenuity-2-0/ehealthcare-frontend)

## Author and Contributors

- [@SabbirHosen](https://github.com/SabbirHosen)
- [@ShahriarShafin](https://github.com/ShahriarShafin)
- [@Ashraf-Moin](https://github.com/ashraf-moin)

## License

This project is licensed under the MIT License - see the [`LICENSE`](LICENSE) file for details.
