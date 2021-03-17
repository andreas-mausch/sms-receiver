docker run --restart=always --name mongo -d -p 27017:27017 -v $(pwd)/mongo:/data sumglobal/rpi-mongodb
