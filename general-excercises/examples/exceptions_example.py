import pudb; pudb.set_trace()
try:
    # from backboxlib import BackBox
    import netaddr
    from netaddr.core import AddrFormatError

    class BackBox:
        def __init__(self, ip):
            try:
                netaddr.IPAddress(ip)
            except AddrFormatError:
                print("The IP isn't good! Please check yourself")
            self.url = ip


    a = BackBox("zainbaain")
    a.connect()


    print("Finished sucessfuly")

except Exception:
    print("An unhandled error occured! Pleas contact BackBox support!")