import requests

def get_url(url, **kwargs):
    """
    Obtain a response from a given URL, with graceful error handling.
    
    Parameters:
    - url (str): The URL to fetch.
    - kwargs: Additional keyword arguments to pass to requests.get().
    
    Returns:
    - requests.Response: The response object from the request, if successful.
    
    Exits:
    - The script exits gracefully if an unrecoverable error occurs, after logging the error.
    """
    try:
        response = requests.get(url, **kwargs)
        response.raise_for_status()  # Will raise HTTPError for 4xx/5xx responses
        return response
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error for URL {url}: {e.response.status_code} {e.response.reason}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your network connection.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")

    # Exit the script
    sys.exit(1)
    
    
def find_duplicate(query_list):
    duplicates = []
    count = dict()
    for item in query_list:
        if item not in count.keys():
            count[item] = 1
        else:
            count[item] += 1
            duplicates.append(item)
    return duplicates

def find_AH(AA_seq, prediction):
    '''
    Return residues that are predicted to be an AH
    as a list of residues and their locations
    Note that there is '\n' in the end of both AA and prediction strings,
    thus precition[0-1] and predition[last] return non-1 anyway,
    preventing the bug when predciton starts or ends with 1
    '''
    AH_res_loc_dict = dict()

    for i in range(len(prediction)): # account for the \n
        if (prediction[i-1] != '1') & (prediction[i] == '1'):
            AH_start = i

        elif (prediction[i-1] == '1') & (prediction[i] != '1'):
            AH_end = i
            
            # pack AH residues and locations into a dictionary
            AH_res = AA_seq[AH_start:AH_end]
            AH_loc = str(AH_start+1) + '-' + str(AH_end) # residue number is non-pythonic and starts with 1, not 0
            AH_res_loc_dict[AH_res] = AH_loc

    return AH_res_loc_dict

