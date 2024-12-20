import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from .base_page import BasePage
from selenium.webdriver.support.ui import Select

# Lớp Search kế thừa từ lớp BasePage chứa các chức năng của thanh tìm kiếm
class Navigation(BasePage):

    def click_random_product(self, product_sale=False):
        # Tìm tất cả sản phẩm
        products = self.driver.find_elements(By.CSS_SELECTOR,
                                             ".isotope-item .block2-txt-child1 a")  # CSS selector của sản phẩm
        if product_sale:
            products_with_sale = self.driver.find_elements(By.CSS_SELECTOR, '.stext-105 span[style="color: green;"]')
            selected_product_sale = random.choice(products_with_sale)
            if selected_product_sale:
                product_element = selected_product_sale.find_element(By.XPATH, './ancestor::div[@class="block2"]')

                quick_view_button = product_element.find_element(By.XPATH, './/a[contains(text(), "Quick View")]')

                quick_view_button.click()

                time.sleep(2)
                if self.driver.find_element(By.XPATH,
                                            "/html/body/section/div[1]/div[1]/div[2]/div/h4").text.strip() not in self.added_products:
                    self.added_products.append(self.driver.find_element(By.XPATH,
                                                                        "/html/body/section/div[1]/div[1]/div[2]/div/h4").text.strip())  # Lưu tên sản phẩm vào danh sách​19:40/-strong/-heart:>:o:-((:-h Tiến Hentai đang soạn tin trên máy tínhXem trước khi gửiThả Files vào đây để xem lại trước khi gửi

        else:
            # Kiểm tra nếu danh sách sản phẩm không rỗng
            if products:
                # Random chọn 1 sản phẩm
                selected_product = random.choice(products)
                if selected_product.text.strip() not in self.added_products:
                    self.scroll_to_element(selected_product)
                    product_name = selected_product.text.strip()
                    self.added_products.append(product_name)  # Lưu tên sản phẩm vào danh sách
                time.sleep(2)
                # Click vào sản phẩm được chọn
                selected_product.click()
                time.sleep(3)  # Chờ sau khi click
                if self.driver.find_element(By.XPATH,
                                            "/html/body/section/div[1]/div[1]/div[2]/div/h4").text.strip() not in self.added_products:
                    self.added_products.append(self.driver.find_element(By.XPATH,
                                                                        "/html/body/section/div[1]/div[1]/div[2]/div/h4").text.strip())  # Lưu tên sản phẩm vào danh sách​19:40/-strong/-heart:>:o:-((:-h Tiến Hentai đang soạn tin trên máy tínhXem trước khi gửiThả Files vào đây để xem lại trước khi gửi
            else:
                print("No products found to select.")

    def get_added_products(self):
        return self.added_products

    def click_gundam(self):
        # click vào nút tìm kiếm trong danh mục con
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/a").click()
        time.sleep(2)

    def get_text_h1(self):
        name = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/h1").text
        return name

    def hover_and_click_gundam_PG(self):
        menu_element = self.driver.find_element(By.XPATH, "//a[text()=' Gundam']")

        # Di chuột vào menu cha
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_element).perform()

        # Đợi submenu xuất hiện và chọn Gundam PG
        submenu_item = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='sub-menu']//a[text()=' Gundam PG']"))
        )

        # Nhấp vào Gundam PG
        submenu_item.click()
    def get_product_name(self):
        name = self.driver.find_element(By.XPATH, "/html/body/section/div[1]/div[1]/div[2]/div/h4").text
        return name

    def click_by_xpath(self, xpath):
        """Click vào phần tử dựa trên XPath"""
        self.driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)  # Thời gian chờ để đảm bảo trang được tải xong
    def test_navigation_links(self, driver, xpath_list, expected_headers):
        """
        Kiểm tra các đường link và tiêu đề tương ứng.

        :param driver: WebDriver instance
        :param xpath_list: Danh sách các đường dẫn XPath
        :param expected_headers: Danh sách tiêu đề mong đợi tương ứng với từng XPath
        """
        driver.get("http://localhost:8000/")  # Điều hướng về trang chủ
        navigation = Navigation(driver)

        for xpath, expected_header in zip(xpath_list, expected_headers):
            try:
                navigation.click_by_xpath(xpath)  # Click vào đường dẫn
                header = navigation.get_text_h1()  # Lấy tiêu đề
                assert header == expected_header, f"Expected '{expected_header}' but got '{header}'."
                print(f"Test passed for XPath: {xpath} with header: '{header}'")
            except Exception as e:
                print(f"Test failed for XPath: {xpath}. Error: {str(e)}")
            finally:
                driver.back()  # Quay lại trang chủ để tiếp tục test
                time.sleep(1)  # Chờ trước khi thực hiện lần test tiếp theo

    def click_menu_hg(self):
        time.sleep(3)
        menu_element = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/a")
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_element).perform()
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/ul/li[2]/a").click()

    def click_menu_mg(self):
        time.sleep(3)
        menu_element = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/a")
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_element).perform()
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/ul/li[3]/a").click()

    def click_menu_rg(self):
        time.sleep(3)
        menu_element = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/a")
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_element).perform()
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/ul/li[4]/a").click()

    def data_validation_show_product(self):
        time.sleep(5)
        # Tìm kiếm danh sách sản phẩm tìm thấy
        products = self.driver.find_elements(By.CSS_SELECTOR, '.block2-txt .js-name-b2')
        product_names = [product.text for product in products]
        # return danh sách sản phẩm tìm thấy
        return product_names



