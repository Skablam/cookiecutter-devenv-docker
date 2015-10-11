# cookiecutter-devenv-docker

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template for a development environment where each application is run in a [Docker](https://www.docker.com/) container.

To create a development environment clone this repository and then run:

```
  cookiecutter cookiecutter-devenv-docker
```

It will prompt you for the dev env name:

```
  devenv_name (default is "devenv-example")?
```

Enter the name for your dev environment and hit enter. This will create a folder with your devenv_name.

Change directory i.e. if your dev env is called devenv-webapps:

```
  cd devenv-webapps
```
In this folder there will be an apps.yml file, this is the file that will contain the details of your applications. By default it contains a sample application:

```
    flask-docker-example:
      repo: git@github.com:Skablam/Flask-Docker-Example.git
      branch: master
      port: 7676
```

Here the app name is flask-docker-example. Repo is the url of the application. Branch is the git branch you want to pull. Port is the port that your application will be listening on.

You can add as many apps as you want, and it is assumed that each app will have a Dockerfile from which a container will be built. Once you have added your applications to apps.yml you can then Vagrant up.

```
  vagrant up
```

During Vagrant provisioning each app will be cloned into /vagrant/apps. A config.yml will be generated from apps.yml. The config.yml is used in conjunction with [Docker-Compose](https://docs.docker.com/compose/) to create and run a container for each app in turn. The applications will be running in the background.

Docker-Compose [commands](https://docs.docker.com/compose/reference/) can then be used to manipulate and interrogate the containers. Several aliases have been created to make this easier (this are set out in local/add-commands.sh):

```
 status                   - View the status of the running the applications
 start *appname*          - Start an application
 stop *appname*           - Stop an application
 restart *appname*        - Restart an application
 logs *appname*           - View the logs for an application
 build *appname*          - Rebuild a container if you have changed the Dockerfile.
 up                       - Builds, (re)creates, starts all applications
 kill-containers          - Stops all containers
 run *appname* *command*  - Run commands inside an application container.
```

See the Docker-Compose [commands](https://docs.docker.com/compose/reference/) for further detail and more options. Note normally the file is called docker-compose.yml rather than config.yml. To specify a custom file you use -f i.e. sudo docker-compose -f /vagrant/config/.yml *command*.

## Working On and Debugging an Application

When working or debugging an application you will want to run the app in the foreground. To do this:

```
  stop flask-docker-example
  run flask-docker-example
```
You can interact with break points when it is running in the foreground.

To run the app in the background again run:

```
  start flask-docker-example
```

## Running Tests

To run unit tests for any application:

```
  run-without-port *appname* *unit test command*
```
For example if you are using pytest:

```
  run-without-port flask-docker-example py.test
```
The run-without-port command will temporarily create another instance of the container but not bind it to any port (just in case the app is already running when you run your unit tests).
