from playwright.sync_api import Page
import pytest

# @pytest.mark.skip_browser("chromium")
# @pytest.mark.only_browser("chromium")
def test_tab_get_an_estimate(page: Page):
    page.goto("https://captivasoft.net")
    assert page.inner_text('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[6]/a') == "GET AN ESTIMATE"      