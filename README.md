# Twitter Sentiment Analyser
A python application which will fetch tweets for a particular region and perfom sentimental analysis on those tweets to determine the degree of positive and negative tweets.

We are using `jupyter notebooks` for this project.
### Installation
1. To install python and its dependencies I would suggest to use `virtualenv`. Install `virtualenv` via `pip`:
    ```sh
    $ pip install virtualenv
    ```
2. Clone the current project 
     ```sh
    $ git clone https://github.com/aarushigupta/TwitterProject
    ```
3. Create a virtual environment for a project:
    ```sh
    $ cd TwitterProject
    $ virtualenv venv
    ```
4. To begin using the virtual environment, it needs to be activated:
    ```sh
    $ source venv/bin/activate
    ```
5. To install all required dependencies, execute the following command
     ```sh
    $ pip install -r requirements.txt
    ```
6.  Execute the following command and copy the twitter api-keys to keys.py file
     ```sh
    $ cp keys.py.sample keys.py
    ``` 
7. To open the jupyter notebooks run the following command.
    ```sh
    $ jupyter notebooks
    ```
8. If you are done working in the virtual environment for the moment, you can deactivate it:
    ```sh
    $ deactivate
    ```
   [giturl]: <https://github.com/aarushigupta/TwitterProject>
