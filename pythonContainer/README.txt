Para construir la imagen:
docker build --tag pythoni .

Para ejecutar:

Opción 1:
docker run  --name tweet5 -it -d -v C:\desarrollo\python\tweetSplit:/app pythoni /bin/bash
docker exec tweet5 python3 /app/generador.py

Opción 2:
docker run --rm -v C:\desarrollo\python\tweetSplit:/app pythoni python3 /app/generador.py

Opción 3:
docker run --rm -v C:\desarrollo\python\tweetSplit:/app augustosalazar/pyhoni:1 python3 /app/generador.py