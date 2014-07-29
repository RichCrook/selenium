from selenium import webdriver

fp = webdriver.FirefoxProfile()

fp.add_extension(extension='firebug-2.0.xpi')
fp.set_preference("extensions.firebug.currentVersion", "2.0") #Avoid startup screen
fp.set_preference("extensions.firebug.console.enableSites", "true")
fp.set_preference("extensions.firebug.net.enableSites", "true")
fp.set_preference("extensions.firebug.script.enableSites", "true")
fp.set_preference("extensions.firebug.allPagesActivation", "on")
browser = webdriver.Firefox(firefox_profile=fp)