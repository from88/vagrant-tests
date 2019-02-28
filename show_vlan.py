import json
import requests
from requests.auth import HTTPBasicAuth
import sys
if __name__ == "__main__":

    auth = HTTPBasicAuth('admin', 'admin')
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = 'http://127.0.0.1:8888/ins'

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show vlan brief",
            "output_format": "json"
        }
    }


    response = requests.post(url, data=json.dumps(payload),headers=headers, auth=auth)
    #print(response)


    result = response.text
    result_dict = json.loads(result)
    vlans = result_dict['ins_api']['outputs']['output']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']
    print('{:12}{:<10}'.format('VLAN ID','NAME'))
    for dict in vlans:
        print('{:12}{:10}'.format(dict['vlanshowbr-vlanid'], dict['vlanshowbr-vlanname']))
