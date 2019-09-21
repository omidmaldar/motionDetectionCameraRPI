# For sending email
* If you use Gmail, make `Less Secure APP Access` **ON** Read [Less Secure APP Access and Google Account](https://support.google.com/accounts/answer/6010255?authuser=1&p=less-secure-apps&hl=en&authuser=1&visit_id=637046560394549091-3119828862&rd=1) 

# Finding IP addr
* `ifconfig wlan0 | grep 'inet ' | awk '{print $2}'`
* **ETHR** `ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1`
* **WLAN** `ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1`

