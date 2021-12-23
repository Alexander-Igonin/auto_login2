import time
from pywinauto import Application

wow_dir = r'"D:\\Games\\Blizzard\\World of Warcraft\\_classic_\\WowClassic.exe"'

cpu = 12
login_wait = 12


def launch_game():
    while queue < 3:
        wow = Application(backend='uia')
        wow.start(wow_dir)
        wow.wait_cpu_usage_lower(threshold=cpu)
        wow.window().type_keys(d.get(queue)[0] + '{TAB}')
        wow.window().type_keys(d.get(queue)[1] + '{ENTER}')
        time.sleep(login_wait)
        wow.window().type_keys('{ENTER}')
        queue += 1