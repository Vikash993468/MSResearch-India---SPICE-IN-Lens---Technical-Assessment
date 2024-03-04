from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os


def get_default_download_directory():
    return os.path.join(os.path.expanduser("~"), "Downloads")

download_path = get_default_download_directory()
# print("Default download directory:", default_download_directory)


options = Options()
options.add_experimental_option("prefs", {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  # This option opens PDFs in a new tab instead of downloading
})

options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



driver.get("https://dspace.mit.edu/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "By Issue Date").click()
dropdown = driver.find_element(By.ID, "aspect_artifactbrowser_ConfigurableBrowse_field_year")
dropdown.find_element(By.XPATH, "//option[. = '2024']").click()
driver.find_element(By.CSS_SELECTOR, "#aspect_artifactbrowser_ConfigurableBrowse_field_year > option:nth-child(2)").click()
driver.find_element(By.LINK_TEXT, "Energy-Stable Global Radial Basis Function Methods on Summation-By-Parts Form").click()
driver.find_element(By.LINK_TEXT, "Download").click()


wait = WebDriverWait(driver, 5)  # Adjust the timeout as needed

downloaded_file = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '{download_path}')]")))

driver.close()


