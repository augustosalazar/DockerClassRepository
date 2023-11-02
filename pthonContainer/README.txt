docker build --tag ptest
docker run --rm -v /root/:/app ptest python3 /app/hello.py