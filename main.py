"""A intenção do código é criar uma rotina automatizada para abrir o tinder e dar switch right (likes)
para os 100 primeiros perfis que encontrar. Primeiro, importam-se as bibliotecas necessárias, webdriver,
para lidar com o navegador, Keys, para usar as funções de teclado (keys), exceptions para lidar com as exceções,
quando o código não encontrar o elemento, e sleep, para o tempo de espera em cada carregamento"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
"""aqui as variáveis para o login, segundo a Angela, o login com menos passos é o do facebook. Lembrando
que para ocultar o e-mail e senha pode-se usar o console.log"""
FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
FB_PASSWORD = YOUR FACEBOOK PASSWORD
"""aqui o caminho do chrome_driver_path no computador """
chrome_driver_path = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
"""o endereço do site para acesso"""
driver.get("http://www.tinder.com")
"""aqui o tempo de espera para carregamento, depois, o botão de login, aqui passado pelo xpath, que é o endereço
único de cada elemento"""
sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()
"""nova espera e é passado o botão de login do facebook"""
sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
"""In Selenium, each window has a identification handle, we can get all the window handles with:
driver.window_handles
The above line of code returns a list of all the window handles. The first window is at position 0 e.g.
Traduzindo, o selenium pode lidar com mais de uma janela ou tab aberta ao mesmo tempo, para isso ele
vai sequenciar as janelas pela ordem em que elas foram abrindo, por isso, a primeira é [0]. Depois é
dado o comando do switch, para ir para a janela de login e dado um print (creio que para testar se o código
está funcionando)"""
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
"""aqui vai localizar o elemento de e-mail e senha pelo x-path e depois o comando .send_keys vai preencher
os campos e dar clique. Pelo que entendi, o padrão é localizar o elemento, guardar em uma variável e depois
usar o send_keys para preencher ou clicar"""
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
""". Using Selenium and Python:

- Click ALLOW for location.

- Click NOT INTERESTED for notifications.

- Click I ACCEPT for cookies

"""
sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
"""como só são permitido 100 likes por vez, o for loop irá iterar tentando localizar o botão de like
(como o aplicativo funciona no site, não há a opção de deslizar) através do xpath dele e irá clicar, a exceção
é para quando aparece um pop up que é um possível match."""
for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()