## Resume-matcher

### Setup

- Install Dependencies
  - pdfminer
    ```
    git clone https://github.com/euske/pdfminer.git
    cd pdfminer
    python setup.py install
    ```
- Install the app
  - Setting up the app inside a [virtualenv](https://virtualenv.pypa.io/en/stable/) 
  	```
    sudo apt-get install python-virtualenv
    cd resume-matcher
    virtualenv venv
    . venv/bin/activate
    ```
  - Installing the dependencies
  	```
    pip install -r requirements.txt
    ```
  - Add a config file for the app
  	```
    touch resume-matcher/app/config.py
    ```

##### Run the server
```
python manage.py runserver
```

##### Needs a config.py with STATIC_PATH variable pointing to the static folder

