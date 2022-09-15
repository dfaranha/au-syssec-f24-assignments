# RSA Signatures

## Your Task

### Task 2: Exploiting Textbook RSA Signatures

You are given the source code of a simple website that a professor has created
to automate annoying tasks such as grading. It also distributes quotes to
particularly good students. To prevent students from coming up with their own
grade, the website authenticates them with RSA signatures.  Since the professor
is quite lazy and does not want to be bothered by students, he/she provides
another API to sign any paperwork except grades.

Your task is to obtain a signed message stating you got a 12, so that you can
receive a quote.  To this end, you can use the given API and the malleability
properties of plain, textbook RSA.

We plan to host a version of the website later on.  To get started with the
task, you can host a local version on your own machine (see below).


### Task 3: Implementing RSA-PSS

Textbook RSA signatures are not secure. An attacker is able to obtain
signatures for messages that were never signed as such.
To prevent such attacks, padding schemes can be used.  One of such is PSS
(Probabilistic Signature Scheme).

The part of the assignment requires the implementation of the RSA-PSS according
to [RFC8017](https://datatracker.ietf.org/doc/html/rfc8017#section-8.1) using
SHA-256 as hash and mask generation function, and a salt length of 32 bytes.

The objective of this assignment is to implement support for the key generation,
signing and signature verification operations, such that the resulting
cryptosystem is consistent and able to verify its own signatures.

In your implementation, you should target a security level of 128 bits, i.e.,
use RSA moduli of size 3072 bits.  You are allowed to use library functions
such as random number generators and mathematical subroutines (of course you
cannot just wrap an existing library for RSA), but you need to document and
justify you decisions with respect to security.  Especially, be careful when
selecting the random number generator for key generation, as to avoid the
pitfalls discussed in class. If encoding/decoding presents a challenge, you
can reuse existing code as well, or read the [IEEE P1363 specification](https://web.archive.org/web/20170810025803/http://grouper.ieee.org/groups/1363/P1363a/contributions/pss-submission.pdf) for reference.
For reference, the German Wikipedia has some [good pictures](https://de.wikipedia.org/wiki/Probabilistic_Signature_Scheme) of the RSA-PSS encoding/decoding functions.

Any high-level programming language will suffice. Immediate suggestions are
Python, for its native support for arbitrary-precision integers, byte strings,
and its extensive standard library; Java, due to its library support for
multi-precision integers; or the combination of the C programming language with
the GMP library.



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
# docker build -t rsa-signatures .
# docker run -p 5000:80 rsa-signatures
```

In both cases, the application is reachable at <http://localhost:5000/>.
