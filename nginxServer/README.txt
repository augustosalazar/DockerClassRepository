
Start the flask container with:
cd simpleFlaskServer
docker build --tag imagef .
docker run -p 5000:5000 --name simplef -d imagef

Start NGINX with:
docker run -d --name nginx-base -p 80:80 nginx:latest

When updating NGINX config
docker cp default.conf nginx-base:/etc/nginx/conf.d/
docker exec nginx-base nginx -t
docker exec nginx-base nginx -s reload

