## Pre-requisites
1. Having installed python3 and pip3
2. Install virtualenv
   1. Follow this guide [Install virtualenv](https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3)
   2. Inside this repository, if you're in a linux environment, please execute:
   ```
        pip3 install virtualenv
        mkdir venv
        virtualenv venv
    ```

## Prepare the environment
1. Activate the virtualenv environment with the next steps:
   1. source venv/bin/activate
   2. pip3 install -r requirements.txt
   3. set up a couple of environment variables, if you're in a linux environment please execute:
    ```
        export EMAIL=`replace_with_your_email`
        export ROOT_URL=https://rooftop-career-switch.herokuapp.com
    ```

## Run the script
1. Please execute the command shown below:<br>
   ```./main.py or python3 main.py```
2. If everything was right, the message `The blocks were sorted properly.` will shown.
3. If there was an error the message `The blocks weren't sorted properly.` will shown.

## Execute the tests
1. Please, before to begin with this section if you not execute the step `Pre-requisites` and `Prepare the environment`, please do it. This won't work without previous steps.
2. In the root path, please execute the command.
   ```
   python3 -m unittest discover -s tests
   ```