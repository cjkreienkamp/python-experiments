import pyautogui as pag
import webbrowser

# ask for unconfigured lidar IP
lidarIP = input("Hesai Lidar IP: ")

# open browser to currentSourceIP
chromeIconPos = (537, 849)
chromeSearchBarPos = (288, 82)

pag.doubleClick(chromeIconPos, duration=15)
pag.click(chromeSearchBarPos, duration=5)
pag.write(lidarIP)
pag.press('enter')
