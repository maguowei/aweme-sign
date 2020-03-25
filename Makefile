include .env

build:
	docker build -t maguowei/${APP_NAME} .

run:
	docker run -it --rm -e REMOTE_DEVICE=${REMOTE_DEVICE} -p 5000:5000 -v ${PWD}:/app maguowei/${APP_NAME}
