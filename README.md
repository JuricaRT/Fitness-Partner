# Fitness-Partner

* STEMI chatbot code repository
* Live chatbot: https://chatbot.stemi.education/chat?projectId=ckomscmu32507gt1i6v1okwqr&runId=ckp6rs6w2514958u9uqr7x69u7d

Rasa Commands
-------------

* `rasa train` -  Trains a model using your NLU data and stories, saves trained model in `./models`
* `rasa run` -  Starts a server with your trained model.
* `rasa test` -  Tests a trained Rasa model on any files starting with `test_.`
* `rasa data split nlu` -  Performs a 80/20 split of your NLU training data.
* `rasa shell` - Loads your trained model and lets you talk to your assistant on the command line.
* `rasa run actions` - Starts an action server using the Rasa SDK.

Directory Structure
-------------

    .
    ├── actions                   # Contains custom action code
    ├── config.yml                # Configuration for Rasa NLU and Rasa Core
    ├── credentials.yml (ignored) # Credentials for voice and chat platforms the bot is using
    ├── domain.yml                # The domain file, including bot responses templates
    ├── endpoints.yml             # Endpoints that bot can use
    ├── models (ignored)          # Contains trained model
    ├── results (ignored)         # Contains training results
    ├── tests                     # Contains tests for bot evaluation
    ├── data                      # Contains training and other data
        ├── nlu                   # Contains NLU training data
        ├── rules                 # Contains rules
        ├── stories               # Contains stories
