# Flask-Restful-Example
the repository is example for restful api by using flask
## Pull image
```
docker pull mysql
```
## Run mysql container
```
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password mysql
```
## Run a command in a running container
```
docker exec -it mysql  mysql -uroot -ppassword
```
## Run app for Local
1.  Clone repo
    ```
    git clone https://github.com/sean830314/flask-restful-example.git
    ```
2.  Setup python virtual environment
    ```
    cd 'your_repo'
    python3 -m venv flask_venv
    source flask_venv/bin/activate
    ```
3.  Installing packages
    ```
    pip install -r requirements.txt
    ```
4.  Create database
    ```
    docker exec -i mysql  mysql -uroot -ppassword <<< "CREATE DATABASE flask_demo;"
    ```
5.  Run app
    ```
    python3 app.py
    ```
6.  Generate data
    ```
    python3 generate.py
    ```
## References

- [mysql dockerhub](https://hub.docker.com/_/mysql)
- [Learn REST: A RESTful Tutorial](https://www.restapitutorial.com/)