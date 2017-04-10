def test_send():
    try:
        #status.set("sending")
        #root.update_idletasks()
        var1 = str("0")
        ip_value = str(var1)
        cat_value = str(var1)
        comment_value = str(var1)
        api_key = str(var1)
        url = 'https://www.abuseipdb.com/report/json?key='
        #requests.get(url + api_key + '&category=' + cat_value + '&comment=' + comment_value + '&ip=' + ip_value)
        final_url = (url + api_key + '&category=' + cat_value + '&comment=' + comment_value + '&ip=' + ip_value)
        print(final_url)
    except ValueError:
        pass
    assert final_url == "https://www.abuseipdb.com/report/json?key=0&category=0&comment=0&ip=0"
