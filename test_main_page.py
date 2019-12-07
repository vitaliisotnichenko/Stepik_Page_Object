import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.list_goods import ListGoods
from pages.item_details_page import ItemDetailsPage
from pages.verification_page import VerificationPage
from pages.checkout_page import CheckoutPage
from pages.delivery_address import DeliveryAddress
from pages.payment_page import PaymentPage
from pages.view_order import ViewOrder


class TestBuyGoods:

        @pytest.mark.need_review
        def test_buy_new_item_as_guest(self, browser):
                self.main_page = MainPage(browser)
                self.main_page.open()
                self.main_page.go_to_all_items()
                self.list_goods = ListGoods(browser)
                self.list_goods.click_on_the_good()
                self.item_details_page = ItemDetailsPage(browser)
                self.item_details_page.add_to_cart()
                self.verification_page = VerificationPage(browser)
                self.verification_page.proceed_order()
                self.checkout_page = CheckoutPage(browser)
                self.checkout_page.enter_email_checkout("test123_fake@gmail.com")
                self.checkout_page.enter_password_checkout("123456")
                self.delivery_window = self.checkout_page.click_submit_button_at_checkout()
                assert "Адрес доставки" in self.delivery_window
                self.delivery_address_page = DeliveryAddress(browser)
                self.delivery_address_page.add_first_name_at_delivery_address_page("Vitalii")
                self.delivery_address_page.add_last_name_at_delivery_address_page("ivanov")
                self.delivery_address_page.add_region_at_delivery_address_page("Darnytsa")
                self.delivery_address_page.add_city_at_delivery_address_page("Kyiv")
                self.delivery_address_page.add_postal_code_at_delivery_address_page("12354")
                self.delivery_address_page.choose_the_country_at_delivery_address_page("UA")
                self.delivery_address_page.click_submit_button_at_delivery_address_page()
                self.payment_page = PaymentPage(browser)
                self.payment_page.add_payment()
                self.view_order = ViewOrder(browser)
                accept = self.view_order.confirm_order()
                assert "Подтверждение заказа" in accept

        @pytest.mark.need_review
        def test_sign_up_new_user(self, browser):
                self.main_page = MainPage(browser)
                self.main_page.open()
                self.main_page.go_to_login_page()
                self.login_page = LoginPage(browser)
                self.login_page.registration_form_at_page()
                self.login_page.enter_email("test123_new_2+")
                self.login_page.enter_password("123456Tt@")
                self.login_page.confirm_password("123456Tt@")
                self.login_page.click_on_confirm_registration_button()
                self.login_page.should_be_registration_success_message()
                assert "Спасибо за регистрацию!" in self.login_page.should_be_registration_success_message()

        @pytest.mark.need_review
        def test_add_comment_about_item(self, browser):
                self.main_page = MainPage(browser)
                self.main_page.open()
                self.main_page.go_to_all_items()
                self.list_goods = ListGoods(browser)
                self.list_goods.click_on_the_good()
                self.item_details_page = ItemDetailsPage(browser)
                self.comment_text = self.item_details_page.add_comment()
                assert "Оставить отзыв о товаре" in self.comment_text
                self.item_details_page.add_comment_title()
                self.item_details_page.add_comment_message()
                self.item_details_page.add_comment_name()
                self.item_details_page.add_comment_email()
                self.item_details_page.click_add_comment_button()
                assert "Оставить отзыв о товаре" not in self.comment_text
