#url shortener 
import requests
def shorten_link(full_link,link_name):
  api='dd684531e28d0310ac83164336f9f6f5238f0'
  base_url="https://cutt.ly/api/api.php"
  payload={'key':api,"short":full_link,"name":link_name}
  request=requests.get(base_url,params=payload)
  data=request.json()
  print(data)
  
  try:
    title=data['url']['title']
    shorten_link=data['url']['shortenlink']
    print("Title:",title)
    print("Link:",shorten_link)
  except:
    status=data["url"]["status"]
    print("Error status",status)
link=input("enter ur link: ")
name=input("give your link a name: ")

shorten_link(link,name)

#example:https://samvidha.iare.ac.in/home?action=fee_payment



