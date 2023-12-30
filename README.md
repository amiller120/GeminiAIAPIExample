to run in docker add a .env file to the root of the project and add GOOGLE_AIP_KEY={yourkey}, after that start with docker compose up command. 

To run via vs code without docker, go to the debug tab and start the project with vs code. If you are running outside docker you will also need to install the dependencies that the dockerfile takes care of via pip install. 

The app is configured to run on port 8000.
