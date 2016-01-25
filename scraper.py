import time
import praw
import csv
import datetime
import unicodedata
import codecs

r= praw.Reddit("Getting submissions from r/drugs by /u/scarface1993 v7.0")
r.login #ENTER YOUR USERNAME AND PASSWORD
alist=['alcohol','trees','stopdrinking','drugs','redditorsinrecovery','OpiatesRecovery','opiates','leaves','opiatesrecovery']
for i in range(0,len(alist)):
    #Getting the subreddit
    astring=alist[i]
    subreddit= r.get_subreddit(astring)

    #Getting the latest posts from the subreddit selected
    new_submissions= list(subreddit.get_new(limit=None))

    #Getting todays time
    date_today=time.time()

    #Creating lists
    sub_ids_post= ['Post Id']
    authors_post=['Author']
    text_post=['Text']
    time_stamp_post=['Time']
    title_post=['Title']
    sub_ids_comment=['Comment']
    authors_comment=['Author']
    text_post_comment=['Text']
    time_stamp_comment=['Time']
    post_id_comment=['Post ID']

    #Going Through the submissions
    for submission in new_submissions:
        #Getting Time of the Post
        date_post=submission.created_utc
        if date_today-date_post<(86400):
            print('post',date_post)
            print('today',date_today)
            print('today-post',date_today-date_post)

            #Checking if author is still a part of reddit or not
            #If no author, the author name is deleted,else name will be name of the author
            if not submission.author:
                athr='Deleted'
            else:
                athr=submission.author.name

            #Making sure the post is not repeated
            if submission.id not in sub_ids_post:
                #Getting the text of the post, also solving the unicode 
                op_text=submission.selftext
                encode_op_text=op_text.encode('ascii','ignore')
                encode_title=submission.title.encode('ascii','ignore')
                print(type(op_text))
                #If the text is blank, then we discard the post
                if len(op_text)>1:
                    #Appending the name of author in author list
                    authors_post.append(athr)

                    #Getting unique submission id number
                    sub_id=submission.id

                    #Putting submission id in sub_ids list
                    sub_ids_post.append(sub_id)
                    tme=datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')

                    #Putting time in time list
                    time_stamp_post.append(tme)
                    text_post.append(encode_op_text)

                    #Getting title
                    title_post.append(encode_title)

                    #Comments
                    commentList=praw.helpers.flatten_tree(submission.comments)
                    #Checking if number of comments is more than 0
                    if len(commentList)!=0:
                        for post in commentList:
                            #Getting id of the submission and appending it to the list
                            post_id_comment.append(sub_id)
                            #Checking the author of the post
                            try:
                                auth=post.author
                            #If the author is not there, we give it an attribute error and give the author the name deleted
                            except AttributeError:
                                auth="Deleted"
                            #Appending the authors name to the list
                            authors_comment.append(auth)
                            #Getting post id and appending the list
                            post_id=post.id
                            sub_ids_comment.append(post_id)
                            #Date of the comment
                            try:
                                tm=datetime.datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                            except:
                                tm='Time cannot be determined'
                            time_stamp_comment.append(tm)
                            try:
                                body=post.body
                                encode_body=body.encode('ascii','ignore')
                            except:
                                body='Post cannot be determined'

                            text_post_comment.append(encode_body)


    if astring=='drugs':
        print('in drugs')
        with codecs.open("Drugs-Posts-All(2).csv",'a','utf8') as csvfile:
            a=csv.writer(csvfile)
            rows=zip(sub_ids_post,authors_post,time_stamp_post,title_post,text_post)
            a.writerows(rows)
            
        with codecs.open("Drug-Comments-All(2).csv",'a',encoding='utf8') as csvfile:
            b=csv.writer(csvfile)
            row=zip(post_id_comment,sub_ids_comment,authors_comment,time_stamp_comment,text_post_comment)
            b.writerows(row)


    elif astring=='alcohol':
        print('in alcohol')
        with codecs.open("Alcohol-Posts-All(2).csv",'a','utf8') as csvfile:
            
            a=csv.writer(csvfile)
            rows=zip(sub_ids_post,authors_post,time_stamp_post,title_post,text_post)
            a.writerows(rows)
            
        with codecs.open("Alcohol-Comments-All(2).csv",'a',encoding='utf8') as csvfile:
            b=csv.writer(csvfile)
            row=zip(post_id_comment,sub_ids_comment,authors_comment,time_stamp_comment,text_post_comment)
            b.writerows(row)

    elif astring=='trees':
        print('in trees')
        with codecs.open("Trees-Posts-All(2).csv","a",'utf8') as csvfile:
            
            a=csv.writer(csvfile)
            rows=zip(sub_ids_post,authors_post,time_stamp_post,title_post,text_post)
            a.writerows(rows)

        with codecs.open("Trees-Comments-All(2).csv","a",'utf8') as csvfile:
            
            b=csv.writer(csvfile)
            row=zip(post_id_comment,sub_ids_comment,authors_comment,time_stamp_comment,text_post_comment)
            b.writerows(row)

    elif astring=='stopdrinking':
        print('stopdrinking')
        with codecs.open("Stop-Drinking-Posts-All(2).csv","a",'utf8') as csvfile:
            a=csv.writer(csvfile)
            rows=zip(sub_ids_post,authors_post,time_stamp_post,title_post,text_post)
            a.writerows(rows)

        with codecs.open("Stop-Drinking-Comments-All(2).csv","a",'utf8') as csvfile:
            print("Stop drinking")
            b=csv.writer(csvfile)
            row=zip(post_id_comment,sub_ids_comment,authors_comment,time_stamp_comment,text_post_comment)
            b.writerows(row)

    elif astring=='redditorsinrecovery':
        print('redditorsinrecovery')
        with codecs.open("Redditors-In-recovery-Posts-All(2).csv","a",'utf8') as csvfile:
            a=csv.writer(csvfile)
            rows=zip(sub_ids_post,authors_post,time_stamp_post,title_post,text_post)
            a.writerows(rows)

        with codecs.open("Redditors-In-recovery-Comments-All(2).csv","a",'utf8') as csvfile:
            print("Stop drinking")
            b=csv.writer(csvfile)
            row=zip(post_id_comment,sub_ids_comment,authors_comment,time_stamp_comment,text_post_comment)
            b.writerows(row)

    elif astring=='OpiatesRecovery':
        print('OpiatesRecovery')
        with codecs.open("Opiates-Recovery-Posts-All(2).csv","a",'utf8') as csvfile:
            a=csv.writer(csvfile)
            rows=zip(sub_ids_post,authors_post,time_stamp_post,title_post,text_post)
            a.writerows(rows)

        with codecs.open("Opiates-Recovery-Comments-All(2).csv","a",'utf8') as csvfile:
            print("Stop drinking")
            b=csv.writer(csvfile)
            row=zip(post_id_comment,sub_ids_comment,authors_comment,time_stamp_comment,text_post_comment)
            b.writerows(row)


    elif astring=='opiates':
        print('opiates')
        with codecs.open("Opiates-Posts-All(2).csv","a",'utf8') as csvfile:
            a=csv.writer(csvfile)
            rows=zip(sub_ids_post,authors_post,time_stamp_post,title_post,text_post)
            a.writerows(rows)

        with codecs.open("Opiates-Comments-All(2).csv","a",'utf8') as csvfile:
            print("Stop drinking")
            b=csv.writer(csvfile)
            row=zip(post_id_comment,sub_ids_comment,authors_comment,time_stamp_comment,text_post_comment)
            b.writerows(row)
