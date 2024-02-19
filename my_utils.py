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

    # Perform any necessary cleanup here
    print("Performing cleanup before exiting...")
    # Cleanup code goes here

    # Exit the script
    sys.exit(1)
    

######
    
def entry_convert(df, organism):
    """
    For each entry in a given df, 
    if the entry is from the specified organism (human or mouse),
    just reuse the entry
    if not,
    convert the entry into that of the specified organism (human or mouse)
    """
    # For final output
    converted_id_list = list()
    
    # Organism of interest either human or mouse
    organism_id = organism_id_list[organism]
    
    # for counting how many genes were not found
    reused = similar_but_differ = not_found = 0
    
    # scan entrys in the df
    for i in range(len(df)):
        gene = df.iloc[i, 2]
        
        # judge if the entry comes from human or mouse
        if df.iloc[i, 1] == organism:
            entry_converted = df.iloc[i, 0] # reuse the original gene name
            reused += 1
        else:
            # obtain the human or mouse entry from uniprot
            try:
                r = get_url(f'{WEBSITE_API}/search?query=gene:{gene}+AND+organism_id:{organism_id}+AND+reviewed:true&fields=accession,gene_names')
                result = r.json()['results'][0]
                
                ## get human or mouse entry
                entry_converted = result['primaryAccession']
                ## get gene name and check the names matche between human's or mouse's and the given organism's
                gene_obtained = result['genes'][0]['geneName']['value']
                if gene.lower() != gene_obtained.lower():
                    entry_converted = 'Not_found'
                    similar_but_differ += 1
            except:
                entry_converted = 'Not_found'
                not_found += 1
            
            # take a break
            sleep(1)
        
        # add to the final output list
        converted_id_list.append(entry_converted)
        
        # log every 100
        if i % 100 == 0: print(i, gene, entry_converted)

    return converted_id_list, reused, similar_but_differ, not_found

#####

def get_UniProtEntry(gene):
    '''
    Input: gene (gene name) as a query in UniProt
    Output: UniProt Entry and Gene name that is recorded in UniProt
    '''
    
    try:
        # get response with gene name the query
        r = get_url(f'{WEBSITE_API}/search?query=gene:{gene}+AND+organism_id:{organism_id}&fields=accession,gene_names')
        result = r.json()['results'][0]
        
        ## get human or mouse entry
        entry_converted = result['primaryAccession']
        ## get gene name and check the names match between human's or mouse's and the given organism's
        gene_obtained = result['genes'][0]['geneName']['value']
    
    except:
        entry_converted = 'Not_found'
        gene_obtained = 'Not_found'
        
        
    return entry_converted, gene_obtained