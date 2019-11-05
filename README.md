# flask-app

# API Testing Instructions:

Using browser : http://localhost:5000/api/search?species=homo_sapiens&name=brc 

Using CURL: curl - get 'http://localhost:5000/api/search?species=homo_sapiens&name=brc'


API accepted parameter:

a) species

b) name


This API only accept GET queries. For other type of queries(POST, PATCH, DELETE etc.) it return error(405 HTTP Code)

This API must receive species and name query otherwise it would return HTTP 400 error.


# Installation Instruction:

a) git clone https://github.com/mhossain39/flask-app

b) cd flask-app

c) pip install -r requirements.txt

d) python flask-app.py



# Docker Instruction:

a) git clone https://github.com/mhossain39/flask-app

b) cd flask-app

c) docker build -t flask-app .

d) docker run -d -p 80:5000 --name flaskapp flask-app


# API Documentation:

info:
  description: Restful API which allow users to search gene in Ensembl database
  version: "1.0.0"
  title: Gene Search API

consumes:
  - "application/json"
produces:
  - "application/json"

basePath: "/api"


paths:
  /search:
    get:
       parameters:
        - in: query
          name: species
          schema:
            type: string
          required: true
          name: name
          schema:
            type: string
          required: true

      tags:
        - "Genes"
      summary: "The Gene data structure supported by  application"
      description: "Read the list of gene"
      responses:
        200:
          description: "Successful read gene autocompletion list operation"
          schema:
            type: "array"
            items:
              properties:
                id:
                  type: "string"
                name:
                  type: "string"
                species:
                  type: "string"
