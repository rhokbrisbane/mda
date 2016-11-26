# mda
AWS Ubuntu instance
- download the rhok.pem file
- run ssh -i your_path/rhok.pem ubuntu@ec2-54-206-36-167.ap-southeast-2.compute.amazonaws.com

DB instance Details (postgreSQL)
- host: mda-mentoring.c74u77we23gg.ap-southeast-2.rds.amazonaws.com:5432
- username: mda
- password: mda12345678

Running the Django project from the AWS instance
- ~/mda/mda_mentoring: python manage.py runserver ec2-54-206-36-167.ap-southeast-2.compute.amazonaws.com:8000

Slack API
- client ID: 108594367905.110075204087
- client secret: 13b31acef597d94e5d50f78cdb81563b
