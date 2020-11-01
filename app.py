from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

PATH = "/Users/louisconway/Developer/chromedriver"
driver = webdriver.Chrome(PATH)

class trade:
    def __init__(self, url, ticker, company_name):
        self.url = url 
        self.ticker = ticker
        self.company_name = company_name

        self.percentage_per_trade = 0.25
        self.stop_loss_per = 0.99
        self.take_prof_per = 1.04

        self.login()
        time.sleep(5)
        self.demo_account()
        time.sleep(5)
        self.account_balance()
        time.sleep(5)
        self.search()
        time.sleep(5)
        self.get_price()
        time.sleep(5)
        self.equity_management()
        time.sleep(3)
        self.buy()
        time.sleep(4)
        self.close_pos()

    def login(self):
        # Working Well
        driver.get(self.url)
        logIn_click = driver.find_element_by_xpath('//*[@id="wg_loginBtn"]')
        logIn_click.click()

        while True:
            try:
                email_type = driver.find_element_by_xpath('/html/body/div[26]/div/div[2]/div[2]/div[1]/div/input')
                email_type.send_keys('louis.conway123@gmail.com')
                password_type = driver.find_element_by_xpath('/html/body/div[26]/div/div[2]/div[2]/div[2]/div/input')
                password_type.send_keys('**')
                confirm_click = driver.find_element_by_xpath('//*[@id="l_overlay"]/div/div[2]/button')
                confirm_click.click()
                print("Logged In")
                print('end')
                break
            except:
                print("trying...")

    def demo_account(self):
        while True:
            try:
                account_button_click = driver.find_element_by_xpath('/html/body/app-root/div/topbar/div/account-info')
                account_button_click.click()
                switch_click = driver.find_element_by_xpath('/html/body/app-root/div/topbar/div/account-info/div/div[3]/div[6]')
                switch_click.click()
                break
            except:
                print("attempting to click")

    def account_balance(self):
        str_equity = driver.find_element_by_xpath('/html/body/app-root/div/topbar/div/div[2]/balance-info/div/topbar-info/div/topbar-info-item[2]/div/div[2]/span').text
        temp = str_equity[1:]
        temp_equity = temp.replace(",","")
        self.equity = float(temp_equity)
        print(self.equity)
    
    def search(self):
        # Searching the correct ticker
        print("search has started")
        while True:
            try:
                time.sleep(3)
                search_company = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[1]/div/div[2]/trade-view/div/div[1]/trade-topbar/div/div[1]/trade-search-field/div/input')
                search_company.send_keys(self.company_name)
                time.sleep(3)
                break
            except:
                print("failed")
        
        click_comp = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[1]/div/div[2]/trade-view/div/div/div/trade-instruments-list/scroll-pane/div[1]/trade-instruments-button[1]/div/div[1]')
        click_comp.click()
        
        get_ticker = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[1]/div/div[2]/trade-view/trade-side-panel/div/div/div[3]/trade-market-info/div/scroll-pane/div[1]/div[2]/div[1]/div').text
        print(get_ticker)

        if get_ticker == self.ticker:
            # Buy SEQ
            print("BUY SEQ")
            trade_button_click = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[1]/div/div[2]/trade-view/trade-side-panel/div/div/div[2]/div/div[1]')
            trade_button_click.click()
        else:
            print("Unable to locate the correct stock")

    def get_price(self):
        while True:
            try:   
                str_current_price = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[1]/div/div[2]/trade-view/div/div/div/trade-instruments-list/scroll-pane/div[1]/trade-instruments-button[1]/div/div[4]/div[1]/price-ticker2/div/span[1]').text
                self.current_price = float(str_current_price)
                print(self.current_price)
                break
            except:
                pass

    def equity_management(self):
        self.trade_amount = self.equity * self.percentage_per_trade
        self.share_num = self.trade_amount / self.current_price
        self.stop_loss = self.current_price * self.stop_loss_per
        self.take_profit = self.current_price * self.take_prof_per
        
        self.loss_forcast = self.stop_loss * self.share_num
        self.profit_forecast = self.take_profit * self.share_num

        print("Trade Equity: {}".format(self.trade_amount))
        print("Volume of Shares: {:.2f}".format(self.share_num))
        print("Stop Loss: {}".format(self.stop_loss))
        print("Take Profit: {}".format(self.take_profit))

    def buy(self):
        # need to confirm if this is actually buy button.
        buy_selection_click = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[1]/div/div[2]/trade-view/div/div[1]/div/trade-instruments-list/scroll-pane/div[1]/trade-instruments-button[1]/div/div[4]/div[2]')
        buy_selection_click.click()

        while True:
            try:
                #Summit Trade
                buy_button_click = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[1]/div/div[2]/trade-view/trade-side-panel/div/div/div[3]/trade-deal-ticket/place-order/div/div[1]/div')
                buy_button_click.click() 
                print("position has been filled")
                break      
            except:
                print("attempting to click the buy button")
    
    def close_pos(self):
        pos_tab = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[2]/div[1]/popup-button[1]')
        pos_tab.click()
        while True:
            p_l_num = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[1]/div[2]/positions-popup/positions-list2/scroll-pane/div[1]/positions-list-item2[2]/positions-list-sub-item2/div[9]/span').text
            print(p_l_num)
            if p_l_num >= self.take_profit:
                close_pos = driver.find_element_by_xpath('/html/body/app-root/div/left-side-panel/div[1]/div[2]/positions-popup/positions-list2/scroll-pane/div[1]/positions-list-item2[2]/positions-list-sub-item2/div[10]/close-position-button/div')
                close_pos.click()
                break
            else:
                time.sleep(3)
        

class screener:
    def __init__(self, url):
        self.url = url

        self.data()

    def data(self):
        driver.get(self.url)
        screener_click = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[3]/a')
        screener_click.click()
        while True:
            try:
                view_all = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td[12]')
                view_all.click()
                break
            except:
                print("View all failed")

        while True:
            try:
                exchange_select = Select(driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/select'))
                exchange_select.select_by_index(3)
                rsi_select = Select(driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr[9]/td[8]/select'))
                rsi_select.select_by_index(6)
                sma200_select = Select(driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr[10]/td[6]/select'))
                sma200_select.select_by_index(2)
                break
            except:
                print("loading")
            
        while True:
            try:
                volume_click = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[4]/td/div/table/tbody/tr[4]/td/table/tbody/tr[1]/td[11]')
                volume_click.click()
                time.sleep(2)
                volume_click2 = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[4]/td/div/table/tbody/tr[4]/td/table/tbody/tr[1]/td[11]')
                volume_click2.click()
                self.ticker = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[4]/td/div/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/a').text
                self.company_name = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[4]/td/div/table/tbody/tr[4]/td/table/tbody/tr[2]/td[3]/a').text
                break
                
            except:
                print("loading")

website = screener('https://finviz.com')
print(website.ticker)
print(website.company_name)

trade_site = trade('https://capital.com', website.ticker, website.company_name)