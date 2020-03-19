build:
	docker build -t maguowei/douyin-sign .

run:
	docker run -it --rm -p 5000:5000 -v "${PWD}":/app maguowei/douyin-sign
