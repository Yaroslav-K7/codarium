from selene import have
from selene.support.jquery_style_selectors import s, ss
from selene.support.shared import browser

browser.open('https://www.ecosia.org/')

s("(//*[contains(@class, 'input')])[2]").type('yashaka selene').press_enter()
s("(//*[contains(@class, 'result-title')])[1]").click()
ss('[href="/yashaka/selene"]').should(have.size(3))
