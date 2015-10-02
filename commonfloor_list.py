import requests
import json


print ("Enter the locality frequently visited.")
inp_str = raw_input().strip()

area_respc = requests.get("https://www.commonfloor.com/autosuggest.php?c=Bangalore&\
                        item=locationbuilderproject&str="+inp_str+"&res_type=json")
area_respc = json.loads(area_resp.content)

"""
area_resp = status, count, data -> [0] -> category, city, type, name, id
"""
area = []
for area_count in range(area_respc["count"]):
    if area_resp["data"][area_count]["type"] == "area":
        area_code = area_resp["data"][area_count]["id"]
        area_code = "area_"+str(area_code)
        area.append(area_code)
for area_code in area:
    url = 'https://www.commonfloor.com/nitro/search/search-results'
    payload = {"search_intent":"rent","property_location_filter":[area_code],"city":"Bangalore"}
    respc = requests.post(url, data=json.dumps(payload))
    resp_parsec = json.loads(respc.content)
        
    """
    resp_parse = status
                 groups_total_count
                 groups_count
                 data[0] == card_type, children, project_data, result_count
                 page
                 result_count
                 
        resp_parse -> data[0]["children"][0] = isShortListed
                listing_city        listingImages       posted_by_name
                vci_data            custom_title        gallery_images
                lng                 listing_state_flag  city
                listing_id          verified            flooring
                title               listing_area_id     project_status
                availability        is_super_agent      posted_on
                listing_state       project_id          floor_plans
                listing_intent      project_name        price
                builtup_sqft_area   listing_area        virtual_tour_present
                property_address    lat                 is_under_review
                posted_by_type      unitType            posted_ago
                numBedrooms         virtual_tour        posting_url
    """

    for houses in range(resp_parsec["result_count"]):
        try:
            print resp_parsec["data"][houses]["children"][0]["title"],
            print resp_parsec["data"][houses]["children"][0]["lat"],
            print resp_parsec["data"][houses]["children"][0]["lng"],
            print resp_parsec["data"][houses]["children"][0]["price"]
        except:
            break

