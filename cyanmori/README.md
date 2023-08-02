青森每日自动打卡程序
## pip3 install selenium

# 下载 chrome
## 最新版本
```python
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum -y localinstall google-chrome-stable_current_x86_64.rpm
google-chrome-stable --version      # 查看 chrome 版本
```

## 指定版本
```python
wget https://dl.google.com/linux/chrome/rpm/stable/x86_64/google-chrome-stable-114.0.5735.90-1.x86_64.rpm
sudo yum -y localinstall google-chrome-stable-114.0.5735.90-1.x86_64.rpm
google-chrome-stable --version      # 查看 chrome 版本
```

# 下载对应版本 chromedriver
http://chromedriver.storage.googleapis.com/index.html
```bash
wget http://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```
