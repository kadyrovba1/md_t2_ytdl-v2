Welcom to youtube mp3-converter!

Installation:
1.Install Python 3.6 and newer
2.Clone the repository:https://github.com/kadyrovba1/md_t2_ytdl-v2
3.Install virtualenv
4.Create a new environment: virtualenv env
5.Activate env: source env/bin/aactivate
6.Install required packages: pip install -r requirements.txt
7.Migration: pyhon manage.py migrate
8.Run redis server: redis-server
9.Run celery: celery -A converter worker -l info
10.Run server: python3 manage.py runserver
