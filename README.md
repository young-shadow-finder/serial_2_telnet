# shadow_young_tools

email_notify.py

  it is a tool for send email to target email for private notice
  email_notify.py --FROM sender@type.com --TO receiver@type.com --SUBJECT “msg subject” --PASSWORD "your password"


log_tools.py

  offer a log tools, now just with 2 functions,other functions may be added in the future

serial_server.py

  it is a tool for convert serial to telnet
  you can run it in pycharm or use pyinstall to package it
  then use cmd "${exe_file_name} --COM COM6 --BAND 9600 --PORT 9988"
  --COM:     serial name(COM6 is for windows, maybe, linux should be other names)
  --BAND:    baud rate
  --PORT:    net port


slow_running_light.py

  this is a simple tools for slow running, set frequence in input box
  the color block will change color refer the param frequence


I hope these will help you solve some problems and if you have some good suggestions I will glad to hear from you.
Have a nice day~

Try ubuntu install android enviroment

sudo apt install curl ca-certificates -y
curl https://repo.waydro.id | sudo bash
sudo apt install waydroid -y

sudo waydroid init
sudo waydroid container start
sudo systemctl restart waydroid-container.service
waydroid prop set persist.waydroid.multi_windows true
# 启动 
waydroid session start
# 启动 UI
waydroid show-full-ui
# 查看状态
waydroid status
# 进入adb shell
waydroid shell


waydroid_script

sudo waydroid init -s GAPPS -f
git clone https://github.com/casualsnek/waydroid_script
cd waydroid_script
sudo python3 -m pip install -r requirements.txt
sudo python3 main.py certified
复制获取的 ID，进入设备注册页面，登录谷歌账户并输入前面生成的ID，设置完需要重启 sudo systemctl restart waydroid-container.service

安装 libhoudini，支持 arm 架构 apk

# cd waydroid_script
sudo python3 main.py install libhoudini
waydroid app install /path/to/apk


adb shell settings put global http_proxy "ip:port"  
cert_hash=$(openssl x509 -subject_hash_old -in ssl-proxying-certificate.pem | head -1)
sudo mkdir -p /var/lib/waydroid/overlay/system/etc/security/cacerts/
sudo cp ssl-proxying-certificate.pem /var/lib/waydroid/overlay/system/etc/security/cacerts/${cert_hash}.0
设置完成后需要重启 sudo systemctl restart waydroid-container.service
