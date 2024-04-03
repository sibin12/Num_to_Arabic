# Number to Arabic Converter

This project provides a RESTful API endpoint to convert numeric numbers to Arabic words using Python and Django Rest Framework.

## Installation

1. Clone the repository:
git clone https://github.com/sibin12/Num_to_Arabic.git
cd Num_to_Arabic

2. Install the required Python libraries:
pip install django djangorestframework num2words

## Usage

1. Run the Django server:
python manage.py runserver

2. Make a POST request to the API endpoint:
- URL: http://127.0.0.1:8000/api/convert/
- Request Body:
  ```
  {
    "number": 1234567
  }
  ```

Replace `1234567` with the number you want to convert.

3. Receive the response with the Arabic words equivalent to the number.

## API Endpoint

- POST `/api/convert/`
- Request Body:
 ```
 {
   "number": <numeric_value>
 }
 ```
- Response:
 ```
 {
   "arabic_words": <arabic_equivalent>
 }
 ```

## Libraries Used

- Django: Web framework for building web applications in Python.
- Django Rest Framework: Toolkit for building Web APIs in Django.
- num2words: Python library to convert numbers to words.

