<h1 align="center">Welcome to Ajackus Python Blog Implementation 👋</h1>
<p>
  <a href="https://opensource.org/licenses/MIT" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Django Blog Implementation for python. Extra web views for ease of use

## Setup

```sh
git clone 
cd 
python -m virtualenv env
```
Unix
```sh
source env/bin/activate
```
Windows
```sh
.\env\Scripts\activate
```
## Install

```sh
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata admin_seed
```

## Usage

```sh
python manage.py runserver
```

## Author

👤 **Rohan Krishna**

Github: [@rohan-uxdev](https://github.com/rohan-uxdev)

## Running APIs on Postman

In order to run these APIs on Postman, you will have to run any get method, and retrieve the csrf token from the cookies on the response and add them to the header
X-CSRFToken - 

## 📝 License

Copyright © 2020 [Rohan Krishna](https://github.com/rohan-uxdev).<br />
This project is [MIT](https://opensource.org/licenses/MIT) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_