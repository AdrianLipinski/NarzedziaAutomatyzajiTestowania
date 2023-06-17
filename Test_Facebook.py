from selenium import webdriver

# Inicjalizacja przeglądarki
driver = webdriver.Chrome()

# Otwarcie strony Facebook
driver.get("https://www.facebook.com")

# Znalezienie elementu z logo Facebooka
logo_element = driver.find_element_by_css_selector("a[aria-label='Facebook']")

# Pobranie adresu URL obrazka logo
logo_url = logo_element.get_attribute("href")

# Sprawdzenie, czy adres URL zawiera oczekiwany fragment
if "facebook.com" in logo_url:
    print("Logo Facebooka jest prawidłowe.")
else:
    print("Logo Facebooka jest nieprawidłowe.")

# Zamknięcie przeglądarki
driver.quit()