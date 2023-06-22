import requests

def obtener_valor_dolar(fecha, api_key, serie1):
    
    url_base = f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?{api_key}&firstdate={fecha}&timeseries={serie1}&function=GetSeries"
    # url_base = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=211730625&pass=uVYeQQAvWY3J&firstdate=2023-06-19&timeseries=F073.TCO.PRE.Z.D&function=GetSeries"
    response = requests.get(url_base)
    v_dolar = response.json()
    
    return v_dolar