import frida
import time


def on_message(message, data):
    print(f'[{message}] => {data}')


def start_hook():
    device = frida.get_usb_device(timeout=5)

    app_package_name = 'com.ss.android.ugc.aweme'
    try:
        pid = device.spawn([app_package_name])
        device.resume(pid)
        time.sleep(1)
        session = device.attach(pid)
        print('[*] start hook')
        print(session)

        with open('script/douyin-sign.js') as file:
            js_code = file.read()
        api = session.create_script(js_code)
        api.on('message', on_message)
        api.load()
        return api
    except frida.NotSupportedError:
        print(f'app not found!')


if __name__ == '__main__':
    start_hook()
