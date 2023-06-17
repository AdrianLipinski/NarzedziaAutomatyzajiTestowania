from selenium import webdriver

# Inicjalizacja przeglądarki
driver = webdriver.Chrome()

# Otwarcie strony WP
driver.get("https://www.wp.pl")

# Znalezienie elementu z nazwą strony
page_name_element = driver.find_element_by_css_selector("span[data-id='title']")

# Pobranie tekstowej zawartości elementu
page_name = page_name_element.text

# Oczekiwana nazwa strony
expected_page_name = "WP"

# Sprawdzenie, czy nazwa strony jest zgodna z oczekiwaną
if page_name == expected_page_name:
    print("Nazwa strony WP jest prawidłowa.")
else:
    print("Nazwa strony WP jest nieprawidłowa.")

# Zamknięcie przeglądarki
driver.quit()