The front end for Hyperloop Visison System.

## Download instructions
Download the directory, this can be mainly done in two ways, one is by [cloning the directory](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository/), the other is by [downloading it directly](https://sites.northwestern.edu/researchcomputing/resources/downloading-from-github/).
Open up terminal/shell in the downloaded directory
## Set up instructions
Install all the dependencies
`pip -i requrements.txt`

Run the flask app by using:
`flask run`
## Integration with ML model
To integrate this server with the machine learning model, the functions from the machine learning model could be imported into the flask server and the output would be shown on the server.

See Sample Integration directory for an example ml.py file and a modified app.py file.