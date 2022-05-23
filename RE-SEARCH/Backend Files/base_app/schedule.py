from .models import Url, Cluster
from .scrape import crawl
from .sendMail import send

def scheduled_crawl():
    print('Testing Crawl Status!!!!!!!!!!!!!!!!!!!')
    uncrawled_url_users=set()

    urls = Url.objects.all()

    for url in urls.iterator():
        current_url = Url.objects.get(id=url.id)
        cluster_id = current_url.cluster.id
        link= url.cluster_url
        height= url.depth
        type= url.output_type
        
        #if the url is not crawled then crawl and update the status
        if current_url.is_crawled is not True:
            uncrawled_url_users.add(url.cluster.user.email)
            #uncrawled_url_users = uncrawled_url_users.append(cluster_id.user.id)
            #print(uncrawled_url_users)
            crawled = crawl(link, height, type, cluster_id)

            if crawled:
                current_url.is_crawled = crawled
                current_url.save()
                print(link)
                print(current_url.is_crawled)
                
            else:
                print('Error occured whiled crawling!!!!!!!')
        
        # just for testing
        else:
            print('url: ' + str(current_url.id) + ' - the url is already crawled.......')
    
    for mail in uncrawled_url_users:
        send(mail)
    uncrawled_url_users.clear()
        
    print('Ended crawling')
    

