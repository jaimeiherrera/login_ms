# login_ms
Microservice for login and JWT manage

# Deploy
## Dockerfile
```
docker build -t login_ms_image .
docker run -p 9001:9001 --name login_ms_container -d login_ms_image
```
Optionals
```
docker exec -it login_ms_container /bin/bash
docker logs -f login_ms_container
```