FROM maguowei/python-app:onbuild

ENV APP_NAME douyin-sign
ENV APP_ENV dev

EXPOSE 5000
CMD ["gunicorn", "-w 1 -b 0.0.0.0:5000 app:app"]
