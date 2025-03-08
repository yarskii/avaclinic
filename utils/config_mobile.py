import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

load_dotenv()

remote_url = os.getenv('LOCAL_URL')
relative_path_app = os.getenv('APP_PATH')


def to_driver_options_local():
    app = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path_app))
    options = UiAutomator2Options()
    options.set_capability('app', app)

    return options
