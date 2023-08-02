import requests

# uniprot API URL
WEBSITE_API = "https://rest.uniprot.org/uniprotkb/"

# organism id
organism_id_list = {'Homo sapiens': '9606', 'Mus musculus': '10090'}
organism_id = organism_id_list['Homo sapiens']

def summing(a, b):
    return a + b

def get_url(url, **kwargs):
    '''
    Obatin a response from a given url
    '''
    
    response = requests.get(url, **kwargs)
    
    if not response.ok:
        print(response.text)
        response.raise_for_status()
        sys.exit()
        
    return response


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