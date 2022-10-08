# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

Module 2
Using a suitable Internet Browser create a Trello account by going to:-
https://trello.com/signup

Once the account has been created obtain the API key and token by following the instructions given at:-
https://trello.com/api-key

The API key and token must be kept securely as this provides access to your account.
They can be places in the project .env file which is not one of the files monitored by GIT.
As they will be used in the project it is wise to provide suitable names which can then be retrieved by using the os.getenv() function

To make request to the Trello APIs the Python 'Request' library will need to be installed and added to the poetry dependencies

### Install the requests library (PowerShell)

```powershell
pip install requests
```


### Add the requests library to pyproject.toml dependencies (PowerShell)

```powershell
poetry add requests
```

Module 3

We need to add 'pytest' to our project so that we can perform unit tests.
To do this use the following command 

```powershell
poetry add pytest --dev
```

This should download it and also update pyproject.toml.

The test is performed using the content of the test_view_model.py file which is split into two
sections. The first section tests for items with a status of 'Done' and the second test for items
with a status of 'To Do'
In each section the same list of items is used, the first item has the status of 'To Do' and the
second has the status of 'Done'
Each test used an Action which is based upon a list of returned items as processed in the 
view_model.py file which splits the items into one of two lists (one for each status being tested).
The tests in each section confirms that there is only one item in the returned list, that it has
the correct item id and then correct status.
Other test can be performed by adding additional assert lines to the #Assert section.

Test are run by selecting the 'Test explorer' icon in Visual Studio code (the beaker symbol),
highlighting the required test either at the root level or further down the tree list 
and then pressing the 'Run Test' icon (right pointing triangle)

Successful test will be indicated by a green tick icon. Failures can be reviewed by high lighting
any red lines and looking at the test response.

For the integration test an new file '.env.test' needs to be created in the same directory as 
the existing '.env' file. This new file will be a copy of the existing file but as it is to be 
added to source control and 'secret' information such as API Keys, API Tokens must be removed 
first.

The content of the app.py file needs to be modified so that anything from the 'app = Flask(__name--)
line to the end of all '@app.route' sections are encapsulated within a new 'def create_app():' 
block.

e.g. 
# imports here

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    
    # All the routes and setup code etc
    # e.g.
    # @app.route('/')
    # def index():
    #     ...
    
    return app

The integration test file 'int_test.py' is located in a new 'tests' folder and it important that 
this folder also contains a '__init__.py' file. This can be copied from on of the other existing
folders

The new 'int_test.py' file will contain the test client and will be defined as a 'fixture'.
It will be necessary to import a number of other items into this test file such as the 'app.py',
'dotenv' module to reference the '.env.temp' file as well as others related to 'os', 'pytest' 
and 'requests' 

A 'stub' is used instead of a direct call to Trello which returns a know package of data and it 
is this data that asserts are made to ensure that the correct response is received.

The test can be initiated from within Visual Studio Code using the 'Testing Explorer' option 
which should return successful responses. 
It should also be possible to start 'Git bash' in the root folder of the workspace and running 
poetry run pytest or poetry run pytest path/to/test_file. In the latter case only a subset of all the tests maybe performed rather than a 'full' set.

