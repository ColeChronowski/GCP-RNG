# Random Number Generator Compute Engine for Java™

## Before you begin

Make sure you install jetty9.

In Ubuntu, you can do this with the command

`sudo apt install jetty9`

## Deploying to App Engine

To run the application locally, use the [Maven App Engine
plugin](https://cloud.google.com/appengine/docs/java/tools/using-maven).

    mvn clean appengine:run

View the app at [localhost:8080](http://localhost:8080).

To deploy the app to App Engine, run

    mvn clean appengine:deploy

After the deploy finishes, you can view your application at
`https://YOUR_PROJECT.appspot.com`, where `YOUR_PROJECT` is your Google Cloud
project ID. You can see the new version deployed on the [App Engine section of
the Google Cloud Console](https://console.cloud.google.com/appengine/versions).
