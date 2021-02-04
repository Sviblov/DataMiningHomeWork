import requests
import time
import json

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
# }

# url ='https://5ka.ru/special_offers/'

# response = requests.get(url , headers=headers)

# with  open('HW1/5ka.html', 'w', encoding ='UTF-8') as file:
#     file.write(response.text)


from pathlib import Path 



class Parser5ka:

    headers = {
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }


    def __init__(self, start_url):
        self.start_url=start_url


    
    def _get_response(self, url, **kwargs):
        while True:
            try:
                
                response = requests.get(url, **kwargs)
     
                if response.status_code != 200:
                    raise Exception
                      
                return response
                
            except Exception:
                time.sleep(0.1)
    
    def run(self):
          for products in self.parse(self.start_url):
              for product in products:
                
                file_path = Path(__file__).parent.joinpath(f'output/{product["id"]}.json')
                print(file_path)
                self.save_file(file_path, product)
 

    # def run(self):
    #     response = requests.get(self.start_url , headers=self.headers)
    #     with  open('HW1/5ka.json', 'w', encoding ='UTF-8') as file:
    #         file.write(response.text)

    def parse(self, url):
        while url:
            response  =  self._get_response(url, headers=self.headers)
            
            data = json.loads(response.text)
            url = data['next']
            yield data.get('results',[])

    def save_file(self, file_path, data):
        with open(file_path, 'w', encoding='UTF-8') as file:
#            file.write(json.dumps(data))
            json.dump(data, file, ensure_ascii=False)


if __name__ == '__main__':
    parser = Parser5ka('https://5ka.ru/api/v2/special_offers/')
    parser.run()






