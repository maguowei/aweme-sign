from subprocess import Popen
import frida


def on_message(message, data):
    print(f'[{message}] => {data}')


def start_hook(remote_device=''):
    if remote_device:
        frida.get_device_manager().add_remote_device(remote_device)
        device = frida.get_remote_device()
    else:
        device = frida.get_usb_device()
    Popen("adb forward tcp:27042 tcp:27042", shell=True).wait()
    Popen("adb forward tcp:27043 tcp:27043", shell=True).wait()
    app_package_name = 'com.ss.android.ugc.aweme'
    try:
        pid = device.spawn([app_package_name])
        device.resume(pid)
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
