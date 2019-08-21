# API token configuration file for Heroku deployments

# This file is for configuring the environment variable for your Discord API token when deployed to a Heroku application.
# You can set this environment variable through your Heroku dashboard on the application settings page.
# Create a new config var on Heroku named API_KEY with your Discord API token as the value.
# This file should not be modified, but you may need to modify the variable name within the [] brackets to match your config var naming scheme.

import os

API_KEY = os.environ['API_KEY']
