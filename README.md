# Simple Catalog App
This simple site uses [Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder) and implements simple OAuth with google for user authentication, auto CRUD generation and custom widgets for faster and better UI.
It uses BootStrap CSS and JS, BootsWatch Themes and Font-Awesome CSS and Fonts.


## Installation

First, clone the project from github:

    ```
    git clone https://github.com/albertodepaola/catalog-project.git
    ```

Then, install the complete list of required packages found in requirements.txt:

    ```
    pip install -r requirements.txt
    ```
    
I recommend using virtualenv to separate different python environments. [Installation guide.](https://virtualenv.pypa.io/en/stable/installation/)
Finally, run the project with:

    ```
    fabmanager run
    ```
    
On the first run, the database is empty. Login using google and you will be granted full admin rights (ginormous security flaw...), then it's possible
to create categories from the top menu 'Catalog' -> 'List Categories'. After the first category is created, new items can be added to it from the main page.
As the app is built using Flask AppBuilder, the navigation is almost completely standard to the framework, the exception being the main page, that conforms
with the projects requirements.

# License
The content of this repository is licensed under a [Creative Commons Attribution License](https://creativecommons.org/licenses/by/3.0/us/)

