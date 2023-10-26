docker build -t flask-image:v1 .
docker run -d -p 5000:5000 -v C:\desarrollo\docker\DockerClassRepository\flaskWebServer:/app flask-image:v1

http://localhost:5000
http://localhost:5000/success/augusto

curl -d "adamlistek=augusto"  -X POST http://localhost:5000/login