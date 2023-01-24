from selenium import webdriver
import webbrowser

driver = webdriver.Firefox()
driver.get("https://hadithsearch.herokuapp.com/")
button = driver.find_element_by_class_name("css-1rs6os edgvbvh3")
button.click()