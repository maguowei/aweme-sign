FROM maguowei/python-app:onbuild

ENV APP_NAME douyin-sign
ENV APP_ENV dev
ENV REMOTE_DEVICE ''
ENV PATH ${APP_SOURCE_CODE_PATH}/bin:$PATH

EXPOSE 5000
CMD [ "sh", "-c", "adb connect ${REMOTE_DEVICE}; gunicorn -w 1 -b 0.0.0.0:5000 app:app" ]
