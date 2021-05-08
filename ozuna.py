# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:36:40 2020

@author: juan-
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# Definimos la URL-principal y la ruta al driver de chrome
main_url = 'https://www.instagram.com/?hl=es-la' # URL principal
driver = 'C:\\Users\\juan-\\OneDrive\\Documentos\\Ozuna\\chromedriver.exe'
# Abrimos una ventana con la URL-principal
browser= webdriver.Chrome(driver)
browser.get(main_url)



time.sleep(50)
k = 0
for i in range(100000):
    try:
        comentario = WebDriverWait(browser,10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')))
        
        comentario.send_keys("ps5")
        
        comentar = WebDriverWait(browser,10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button')))
        
        comentar.click()
        
        time.sleep(61)
        
    except:
        print(k)
        


