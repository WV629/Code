from selenium_out_url import chrome_driver
from selenium.webdriver.common.by import By
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from send import send_qq_email


def main():
    driver = chrome_driver().selenium_out_url()
    driver.get("https://cccc.gg/auth/login")
    element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "email")))
    element.send_keys("2762882807@qq.com")
    driver.find_element(By.ID, "password").send_keys("WUWEIWV52629")
    driver.find_element(By.CLASS_NAME, 'MuiButton-label').click()
    element1 = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='购买套餐']/following-sibling::a")))
    if element1.text == "已签到":
        subject = "青森每日签到"
        content = "今日已签到！"
        print(content)
        send_qq_email(sender_email, sender_password, receiver_email, subject, content)
    else:
        before = driver.find_element(By.XPATH, "//p[text()='剩余流量']/preceding-sibling::div/strong").text
        # 点击签到
        element1.click()
        driver.refresh()
        after = driver.find_element(By.XPATH, "//p[text()='剩余流量']/preceding-sibling::div/strong").text
        subject = "青森每日签到"
        content = f"""亲爱的 WV，恭喜您，签到成功！
            签到前 {before}
            签到后 {after}
                """
        print(content)
        send_qq_email(sender_email, sender_password, receiver_email, subject, content)

if __name__ == '__main__':
    sender_email = "2762882807@qq.com"
    sender_password = "luftjoescukfddbi"
    receiver_email = "2762882807@qq.com"
    try:
        main()
    except Exception as e:
        subject = "青森每日签到-出错啦！"
        content = traceback.format_exc()
        send_qq_email(sender_email, sender_password, receiver_email, subject, content)