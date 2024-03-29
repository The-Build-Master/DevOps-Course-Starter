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

The test is performed using the content of the test_view_model.py file which is split into two
sections. The first section tests for items with a status of 'Done' and the second test for items
with a status of 'To Do'

For the integration test an new file '.env.test' needs to be created in the same directory as 
the existing '.env' file. This new file will be a copy of the existing file but as it is to be 
added to source control and 'secret' information such as API Keys, API Tokens must be removed 
first.

The content of the app.py file needs to be modified so that anything from the 'app = Flask(__name__)
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

Module-4

1. Check that it is possible to connect from the Local Host to the Control Node using 'ssh USERNAME@Control-IP-Address'
2. On the local host use 'ssh-keygen' to create a SSH key pair if required.
3. Then use 'ssh-copy-id USERNAME@Control-IP-Address' to allow ssh communication between the Local Host and the Control Node without the need of a password.
4. Connect the Local Host to the Control Node using 'ssh' and confirm that Ansible is install using 'Ansible --version'.
5. Install Ansible if necessary using 'sudo pip install ansible'.
6. Check that it is possible to connect from the Control Node to the Managed Node using 'ssh USERNAME@Managed-IP-Address'.
7. 'Exit' from the Managed Node to the Control Node.
8. On the Control Node use 'ssh-keygen' to create a SSH key pair.
9. Then use 'ssh-copy-id USERNAME@Managed-IP-Address' to allow ssh connection to the Control Node to the Managed Node without the need of a password.
10. Get copies of the 'my-ansible-inventory' and 'my-ansible-playbook.yml' files from the GIT repository to the Local Host.
11. Check that the IP Address in the 'my-ansible-inventory' matches the Managed Node and modify if necessary.
12. Using a suitable utility such as 'scp' copy these files to the Control Node where the destination path will be '/home/USERNAME'
13. Connect to the Control Node if necessary
14. On the Control Node run the following command 'ansible-playbook my-ansible-playbook.yml -i my-ansible-inventory'
15. Upon request enter the Trello API Key to be used.
16. Upon request enter the Trello API Token to be used
17. This should install and configure all the items needed to complete the deployment to the Managed Node
18. Check for and resolve any errors reported
19. On the Local Host confirm that the application is running by browsing to 'http://Managed-IP-Address:5000/'

Module-5 

The Docker file contains all of the Docker information to create a production build using Gunicorn and a development build using
Flask.

To create a production build the following command line needs to be executed.
$ docker build --target production --tag todo_app:prod .

And to create a development build the following following command line needs to be executed.
$ docker build --target development --tag todo_app:dev .

In both cases the '.' at the end of the comment line is required.

To run the Docker images created the following command lines are are required.
For production
$ docker run -p 5000:5000 --env-file ./.env -it todo_app:prod

For development
$ docker run -p 5000:5000 --env-file ./.env -it todo_app:dev

If required it is possible to make changes to the Python files while a development build is running which will automatically be
applied to the Docker container. To do this the following command line can be used.
$ docker run -p 5000:5000 --env-file ./.env -it --mount type=bind,source="$(pwd)"/todo_app,target=/myapp/todo_app todo_app:dev

As no secrets are to be copied in the build images a list of files not to be copied to the container has been added to a 
.dockerignore files

Module-7

The Dockerfile has been modified to allow for automated testing when using the GIT 'push' and 'pull_request' process by adding a 
'test' target to the file.
For this to function a test image is required and can be built using the following command
$ docker build --target test --tag my-test-image .

To confirm that the tests run correctly use the following command
$ docker run --env-file .env.test my-test-image

Changes to some file and folders will not trigger the automated testing.

Results of the GIT processes the result should appear in the GitHub actions section
 

Module-8

Docker Hub container = 'thebuildmaster/todo_app_prod:latest'

To create and run the Web App follow the instructions below.

Login to the Azure Portal.
Select the create a ‘Web App’ option in the ‘Create Resource’ blade.
On the new screen select the appropriate ‘subscription’ and ‘Resource Group‘. This information should have been provided.
Select a unique name for the Web App. A green tick will indicate if the one entered is acceptable.
Select the ‘Docker container’ radio button for the publish option.
The select the ‘Linux’ radio button for the ‘Operating system’
Set the ‘Region’ to ‘UK West’.
A new Linux Plan will automatically be created but make sure that the Pricing Plan is set to ‘Basic B1’

On the next screen Set the Option drop down to ‘Single Container’ and the Image soured to ‘Docker Hub’
If the access type is Private suitable credentials will need to be provided.
Enter the ‘Image and Tag‘ details which will be ‘thebuildmaster/todo_app_prod:latest’ in this case.
Enter the start up command to ‘run -p 5000:5000 --env-file ./.env -it todo_app_prod’

Select the ‘Review + create’ option.

Once the resource has been created go to the ‘Deployment Centre’ screen in the resource and make note of the ‘Webhook URL’ as this will be needed later.

Before starting the Web App go to the ‘Configuration’ screen. In here enter name / value pairs which are defined in the .env file.
For example ‘FLASK_ENV=development’ would be entered as Name = FLASK_ENV and Value = development.

Save these changes and then start the Web App. This may take some time to complete. There are a number of that will indicate the deployment status.

Then the browse to the Web App. The URL can be located on the Web App Overview page.
If the Web App errors it may be necessary to add an entry to the Configuration list with the Name of WEBSITE_PORT and the Value of the Port number being used by the application which is 5000 in this case.

