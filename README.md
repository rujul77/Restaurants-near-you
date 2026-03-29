# Restaurants near you - JET

## 1. The goal of the task
-
The main goal of the task is to access the API end point given, and then access the first 10 restaurants corresponding to the given postcode by user and display each restaurants attributes. For e.g. name, cuisine, address, rating

## 2. Assumptions made for the task
-
Not a lot of assumptions were made as the task was quite clear. 

However one assumption that was made is that the API always contains the name, cuisine, rating, address and the logo value. For e.g. I can assume that if there is a restaurant in the postcode, it will definitely include all 4 of these values. If one of these is missing, there could be problems in displaying restaurants properly as detailes for each restaurant is given as one python dictionary.


## 3. Design choices
-
1. First was choosing which stack to work with and which type of interface to build. Since There was a few days to do it, i chose to build a very simple web interface to make interacting with it more intuitive. Python was chosen as the main language as this is what I am most comfortable with. Subsequently, I wanted to try and learn something new so I chose flask for the backend. Flask is lightweight and simple for the backend

2. For the interface, Plain HTML and bootstrap CSS were used. All i did with the html was make a form and search button which would send postcode to the backend and return a list of restaurants. Boostrap css made it very easy to make this list into visual cards. My main inspiration was literally the JET website where you enter a postcode and you get nearby restaurants shown in cards.

3. After completing the main functions of the task i chose pytest with appropriate python libraries for unit testing.


## 4. How to run the program
- Ensure you have Python 3.12+ installed (earlier versions may also work)
- Install dependencies: `pip install -r requirements.txt`
- Navigate to the project root directory
- Run the application: `python backend.py`  
  (if this does not work, try `python3 backend.py`)
- Open your browser and go to: `http://127.0.0.1:5000/`
- Enter a postcode to test the program

## 5. How to run the unit tests
- Navigate to the project root directory
- Run: `pytest tests/test_backend.py`
- If `pytest` is not recognised, run: `python -m pytest tests/test_backend.py`

## 6. How AI was used
- ai use was kept to a minimum in this project as it was quite simple. the main hurdle was to learn something new with flask, bootstrap and pytest. AI was mainly used as a learning resource for e.g. asking about syntax, debugging parts of code and explaining the why behind new things I was learning for flask/pytest.

- AI was used a little more to help with the creation of html boilerplate/ guiding the very basic design of the webpage using bootstrap (for e.g. the card design). However, every architectural decision was of my own.

- Finally AI was also used to help with formatting the readme.

- Main AI tools used were Claude ai and chatGPT (basic web versions).