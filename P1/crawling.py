__author__ = 'lichi'
import csv
import bottle
import beaker.middleware
from bottle import route, redirect, post, run, request, hook
from instagram import client, subscriptions
from instagram.client import InstagramAPI
import networkx as nx
# this program is for crawl the deliverables from instagram from instagram API


access_token = ["2195792816.4703390.fc85db689d894ff5a7636fd61787966c","2195792816.d296051.df7316c7fabf4726b2d7f7c0fcc03eca","2195792816.2d7542a.6fd2469ea72c425f860c6615d8e85b11","2195792816.7d3e419.bdbd41a3f8ab44b89a230651cff16081"]
client_secret = ["84913b93461442d8811e7986c738224f","6c7bc9d050c0464b8c66e712034c1fe7","8836faa2a77b4003a89e5f363feb330b","08a95d597c31474db6080f3a016601fc"]
#api = InstagramAPI(access_token=access_token, client_secret=client_secret)
#recent_media, next_ = api.user_recent_media(user_id="2195792816", count=10)
bottle.debug(True)

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)


CONFIG = {
    'client_id': '<d2960516e0164a4ea784900fdc47482c>',
    'client_secret': '<6c7bc9d050c0464b8c66e712034c1fe7>',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

k=0
l=0

usersparent=[]
useridparent=[]
degree=[]
username_uni=[]


fp = open("non_anonymized_egde_list.csv", "wb")
fp_txt=open("egde_list.txt","w")
fp_degree=open("degree.txt","w")
w=csv.writer(fp)

def user_follow(id,name):
    global k
    global useridparent
    global usersparent
    global username_uni
    global l
    k=k+1
    d=0
    api = InstagramAPI(access_token=access_token[k%4], client_secret=client_secret[k%4])
    #print k
    try:

        content=[]
        user_follows, next = api.user_follows(id)
        match= (x for x in username_uni)
        if(not (name==match)):
            username_uni.append(name)
            l=l+1
            print l
            for user in user_follows:



                ufname=user.username
                ufid=user.id

                unamel=[name,ufname]
                uidl=[id,ufid]
                content = "," .join(map(str,unamel))
            # write  username into csv document
                w.writerow(unamel)
                fp_txt.writelines(content)
                fp_txt.write('\n')
                useridparent.append(uidl)
                usersparent.append(unamel)


                d=d+1

            #print len(users)
            while next:
            #print next
            #print usersparent
                user_follows, next = api.user_follows(with_next_url=next)
            #print user.id
                for user in user_follows:
                    ufname=user.username
                    ufid=user.id
                    unamel=[name,ufname]
                    uidl=[id,ufid]
                    content = "," .join(map(str,unamel))
                # write  username into csv document
                    w.writerow(unamel)
                    fp_txt.writelines(content)
                    fp_txt.write('\n')

                    usersparent.append(unamel)
                    useridparent.append(uidl)

                    d=d+1


            degree.append(d)
            fp_degree.write(str(d))
            fp_degree.write('\n')




            #print usersparent
        #for user in usersparent:
            #fp_init.write(user)
           # fp_init.write('\n')

            #print useridparent
            #print content
            #print len(usersparent)
            #print 'length of userid',len(useridparent)

    except Exception as e:
        print(e)



    #print k,res
if __name__ == "__main__":
    id= # you instagram id
    name= # you instagram username

    user_follow(id,name)


    print len(useridparent)
    print len(usersparent)
    print useridparent



    #users_set=set(usersparent)
    #print users_set
    n=len(useridparent)

    for i in range(0,118):            # get friends of friends
        user_follow( useridparent[i][1], usersparent[i][1])
        usersparent[0:i][:]=[]
        useridparent[0:i][:]=[]

    print len(useridparent)
    #print usersparent
    print 'the number of usersparent',len(usersparent)
    #print useridparent
    print degree
    print len(degree)
    a=usersparent[:][0]
    print len(a)






    for i in range(0,2500):
        #try:
        user_follow( useridparent[118+i][1], usersparent[118+i][1])
        if(i>1000):
            useridparent[0:i][:]=[]
            usersparent[0:i][:]=[]

        #print len(useridparent)
        #except Exception as e:
            #print(e)
    fu=open('username_uni.txt','w')
    for x in username_uni:
        fu.write(x)
        fu.write('\n')

    fu.close()
    print len(username_uni)
    print len(degree)



    fp.close()
    fp_txt.close()
    fp_degree.close()




