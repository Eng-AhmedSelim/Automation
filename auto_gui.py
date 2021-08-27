import pyautogui as pgui
from time import sleep

print(pgui.size())  #
print(pgui.position())  # location mouse

print(pgui.moveTo(650, 1056))  # move to mk


pgui.click(646, 1058)
sleep(3)
pgui.click(199, 69)
sleep(3)
pgui.click(831, 471)
sleep(3)
pgui.write('facebook', .3)
pgui.hotkey('enter')


pgui.alert(text='', title='', button='OK')
pgui.confirm(text='How are you', title='hello', buttons=['Im fine', 'Cancel'])

user = pgui.prompt(text='inter name', title='config', default='')
print(user)

pgui.password(text='', title='', default='', mask='*')

# ------------------------------------
# loop view location mouse
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pgui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')