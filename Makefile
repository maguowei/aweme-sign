build:
	docker build -t maguowei/douyin-sign .

run:
	docker run -it --rm -e "REMOTE_DEVICE=192.168.56.103:27042" -p 5000:5000 -v ${PWD}:/app maguowei/douyin-sign
