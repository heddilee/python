site = "http://google.com"
site = site[7:]
site = site[0:-4] # == site[:site.index(".")]

password = site[0:3] + str(len(site)) + str(site.count("e")) + "!"
print(password)