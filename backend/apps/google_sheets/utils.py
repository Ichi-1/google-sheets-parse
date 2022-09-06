import traceback
import xmltodict
import urllib3

def get_cbr_xml():
    """
    Perform GET request to CBR and parse response data to python dict
    """
    CBR_DAILY_COURSE_XML = "https://www.cbr.ru/scripts/XML_daily.asp?"
    http = urllib3.PoolManager()
    response = http.request("GET", CBR_DAILY_COURSE_XML)

    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return data



def get_current_usd_course():
    """
    Loop over Valute Dict and returning current USDRUB course. 
    Casted from string to float number.
    """
    cbr_parsed = get_cbr_xml()
    valute_dict = cbr_parsed["ValCurs"]["Valute"]
    
    for valute in valute_dict:
        if valute["Name"] == "Доллар США":
            return float(valute["Value"].replace(',', '.'))
    
    
