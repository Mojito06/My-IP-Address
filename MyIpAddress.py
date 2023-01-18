def whoTheFuckAmI():
    ip = "None"
    try:
        ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    except:
        pass
    return ip
    
whoTheFuckAmI()
