# Task 1: CBC Padding Oracle

## Your Task

You are given the source code of a simple website that distributed quotes.
However, you only receive a quote if you can present a cookie containing a
valid authentication token.  Such a token is an AES-CBC encryption of a certain
message.

You first need to recover the secret part of the message, and then create a valid
ciphertext containing the right plaintext without having access to the
encryption key.

This requires you to exploit the properties of the CBC mode of encryption,
together with the fact that the service outputs helpful error messages in case
something goes wrong. A very helpful tutorial to CBC padding oracle attacks can be found [here](https://research.nccgroup.com/2021/02/17/cryptopals-exploiting-cbc-padding-oracles).

We plan to host a version of the website later on.  To get started with the
task, you can host a local version on your own machine (see below).

NB: This is of course not a good authentication method, but rather a somewhat
artificial example demonstrating the problems of unauthenticated symmetric
encryption.

## Running the Service Locally

With the given files, you can play around with the service and test your code
locally on your own computer.  Note that all secret data has been redacted from
the code and replaced with dummy values.

If you have installed Python 3, you can install the required packages in an
isolated virtual environment:
```
$ python -m venv venv               # (1) create a virtual environment in the directory `venv`
$ . ./venv/bin/activate             # (2) activate the virtual environment
$ pip install -r requirements.txt   # (3) install the required packages into the virtual environment
```
To run the service you then simply execute the following:
```
$ FLASK_APP=main flask run          # (4) run the application
```
The next time you want to run the service, you only need to repeat step (4)
(possibly after activating the virtual environment again Step (4)).

Alternatively, we also prepared a Docker container that you can use:
```
# docker build -t cbc-padding-oracle .
# docker run -p 5000:80 cbc-padding-oracle
```

In both cases, the application is reachable at <http://localhost:5000/>.
