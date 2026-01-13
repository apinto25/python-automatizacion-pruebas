import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://localhost:8080"


class TestUserRegister:
    @pytest.fixture(autouse=True)
    def setup(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 5)

        yield

        self.driver.quit()

    def test_page_title(self):
        assert "Registro" in self.driver.title

    def test_create_user(self):
        username = self.driver.find_element(By.ID, "username")
        email = self.driver.find_element(By.CSS_SELECTOR, "#email")
        button = self.driver.find_element(By.XPATH, "//*[@id='btn-save']")

        username.send_keys("ana")
        email.send_keys("ana@test.com")
        button.click()

        response = self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "message")))

        assert response.text == "¡Usuario creado exitosamente!"
