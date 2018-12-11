# QuoteOTD

A "quote of the day" server in Python3

## A little story
A day I was wondering about the port 17, what in the world could be the use of this port ? It is one of the well-known ports but I don't know for which protocol it is used. So I decided to do some researches, I found out that it's used for the qotd (Quote Of The Day) protocol. And I decided to implements this protocol in TCP in Python3 because there was almost nothing about it.

## How to setup
If you juste want to test read the script, if you want to set it up on your server read the daemon.

### The script

Open a terminal a launch these commands in order to test the script.

```
git clone https://github.com/M1ster0x/QuoteOTD.git
cd QuoteOTD
sudo python3 QuoteOfTheDay.py
``` 

### The daemon

In order to setup a daemon and launch the server with
```
systemctl start quoteotd
```
You have to clone the repo, make the script executable and set the daemonfile in the right place
```
git clone https://github.com/M1ster0x/QuoteOTD.git
cd QuoteOTD
chmod 0755 QuoteOfTheDay.py quoteotd.service
sudo mv QuoteOfTheDay.py /usr/bin/quoteotd
sudo mv quoteotd.service /etc/systemd/system/
```
Once you've done that you can start/stop the daemon or even enable it if you want it to launch at boot.
