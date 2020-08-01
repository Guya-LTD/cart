[![Build Status](https://travis-ci.org/Guya-LTD/cart.svg?branch=master)](https://travis-ci.org/Guya-LTD/cart)


# Cart service for Guya microservices

Cart service for Guya microservices is a Python based Microservice API


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- python 3.7

### Installation

To make sure about the *[dependency isolation](https://12factor.net/dependencies "dependency isolation")* is recommended to use the *[venv](http://https://docs.python.org/3/library/venv.html "venv")* to create a virtual environment.

After downloading or cloned this repository, open the project directory and install the dependencies with the below *pip* command:

```
pip install -r requirements.txt
```

For development purposes, you can install the package in editable mode with the dev requirements.

```
pip install -e . -r requirements-dev.txt
```

For testing purpose, you can install the package in tesing mode with the test requirements.

```
pip install -e . -r requirements-test.txt
```

For generating documentation, you can install sphinx and other requiremtns using doc requiremtns.

```
pip install -e . -r requirements-doc.txt
```

### Usage

**Development**

In development, you can use the built-in development server with the `flask run` command. Remember to set the environment and the database URI:

```
export FLASK_ENV=development (optional)

export FLASK_APP=cart (optional)

flask run
```

For a smoother work-flow on development, you can use a .env file to load the database URI. The *local.env* file, in the *app* folder, is an example of use to .env file.

**Production**

In the production environment, you just need to set the DATABASE_URL environment variable. Then you can use the command:

`waitress-serve --call 'cart:create_app'`

[Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/ "Waitress") is the production WSGI server used for this project.

**Tests**

To run the test, you need to set the DATABASE_URL environment variable too. Like in development, you can use a test/.env to set the DATABASE_URL variable.

Run the test with the following command:

`tox`

### Usage with Docker

### Hooks

```
pre-commit install
```

## Commiting code

```
git add .
cz commit
git commit -v -a
```

### Testing

#### Syntax

You can check the syntax using flake8 (you must have flake8 package installed first) :

```
flake8 c1
```

You can also use tox (you must have tox package installed first) :

```
tox -e lint
```

#### Test coverage

To execute the test coverage, you must install the package with the dev requirements (see installation section).

Then, you can run the coverage with the following command :

```
coverage run --source c1 -m py.test
```

You can also use tox (you must have tox package installed first) :

```
tox -e test
```

#### Running Unit Test

#### Running Functional Test

#### Running Integration Test

#### Running Load Test

### Deployment

### Built With

## API Reference

## Change log

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Contributing

Whether reporting bugs, discussing improvements and new ideas or writing extensions: Contributions are welcome! Here's how to get started:

1. Fork the repository on Github, create a new branch off the master branch and start making your changes (known as[ GitHub Flow](https://guides.github.com/introduction/flow/index.html " GitHub Flow"))
2. Write a test which shows that the bug was fixed or that the feature works as expected
3. Send a pull request and bug the maintainer until it gets merged and published

Please see [CONTRIBUTING](CONTRIBUTING.md)

## Authors

Please see [AUTHORS](AUTHORS.md)

## License
