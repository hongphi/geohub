# geohub

Geo's Hub

## Step by step to run this project:
- At root project run this command to build project:
    
        $ docker-compose -f local.yml build
- Then run this command to run all services:

        $ docker-compose -f local.yml up -d
- Run this command to restore database:

        $ docker-compose -f local.yml exec postgres restore backup_2022_06_13T01_59_33.sql.gz

- Open browser with [this link](http://localhost:8080/)
- Add more services go to http://localhost:8000/admin/services/product/ (username: hongphi, pass: admin)
### Running tests with pytest

    $ docker-compose -f local.yml exec django pytest

### Curl command to test api:
    List api services
    $ curl -X GET http://localhost:8000/api/services/
    Services details
    $ curl -X GET http://localhost:8000/api/services/<slug>/


### Geo hub diagram and solution diagram:
- Please check these file: geohub_diagram.png, solution diagram.png

