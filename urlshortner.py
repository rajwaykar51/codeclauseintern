import requests
#importing requests module
def shorten_link(full_link,link_name):

    api_key = '970d322f87562459db1f974ac181cb71610a7'
    base_url = 'https://cutt.ly/api/api.php'

    payload = {'key': api_key, 'short': full_link, 'name':link_name}
    request = requests.get(base_url, params=payload)
    data = request.json()

    print(" ")

    try:
        title= data['url']['title']
        short_link= data['url']['shortLink']

        print("Title: ",title)
        print("Link: ",short_link)

    except:
        status = data['url']['status']
        print("Error Status: ", status)
        # url => status: 1	the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened
        # url => status: 2	the entered link is not a link
        # url => status: 3	the preferred link name is already taken
        # url => status: 4	Invalid API key
        # url => status: 5	the link has not passed the validation. Includes invalid characters
        # url => status: 6	The link provided is from a blocked domain
        # url => status: 7	OK - the link has been shortened.

link= input("Enter URL: ")
name= input("Enter name: ")
shorten_link(link,name)