# Simple Catalog App
This simple site uses [Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder) and implements simple OAuth with google for user authentication, auto CRUD generation and custom widgets for faster and better UI.
It uses BootStrap CSS and JS, BootsWatch Themes and Font-Awesome CSS and Fonts.


## Installation
This project requires python3.6 or latter. In order to facilitate creating many python projects with different requirements, virtualenv was used. [Installation guide](https://virtualenv.pypa.io/en/stable/installation/). To install using virtualenv on Linux:


    git clone https://github.com/albertodepaola/catalog-project.git;
    cd catalog-project;
    pip install virtualenv;
    virtualenv -p python3.6 envname;
    source envname/bin/activate;
    pip install -r requirements.txt;
    fabmanager run --host 127.0.0.1 --port 8080;
    
To install using virtualenv on Windows 10 with python 3.7 already installed using PowerShell:
    
    git clone https://github.com/albertodepaola/catalog-project.git;
    cd catalog-project;
    pip install virtualenv;
    virtualenv envname; # on windows I've noticed that you have to hit enter to see when it finishes
    .\envname\Scripts\activate.bat;
    pip install -r requirements.txt;
    fabmanager run --host 127.0.0.1 --port 8080;

    
On the first run, the database is empty. Login using google and you will be granted full admin rights (ginormous security flaw...), then it's possible to create categories from the top menu 'Catalog' -> 'List Categories'. After the first category is created, new items can be added to it from the main page.
As the app is built using Flask AppBuilder, the navigation is almost completely standard to the framework, the exception being the main page, that conforms with the project requirements.

# License
The content of this repository is licensed under a [Creative Commons Attribution License](https://creativecommons.org/licenses/by/3.0/us/)

