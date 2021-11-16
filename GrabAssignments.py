import asana
import requests
import json
# Opening JSON file
f = open('tokens.json',)
# returns JSON object as
# a dictionary

tokens = json.load(f)
studentID =  requests.get("https://mycourses.unh.edu/api/v1/users/self"+"?access_token="+tokens["canvas"]).json()['id']

#r = requests.get('https://mycourses.unh.edu/api/v1/users/76831/courses'+"?state=avalible&access_token="+tokens["canvas"])
r = requests.get('https://mycourses.unh.edu/api/v1/courses/'+"?enrollment_type=student&access_token="+tokens["canvas"])
#r = requests.get('https://mycourses.unh.edu/api/v1/users/76831/courses/85180/assignments'+"?access_token="+tokens["canvas"])

courseids = ['85392']
#print(r.'json())

for i in r.json():
    courseids.append(str(i['id']))
client = asana.Client.access_token(tokens["asana"])
print(courseids)
for i in courseids:
    r = requests.get('https://mycourses.unh.edu/api/v1/users/self/courses/'+i+'/assignments'+"?bucket=future&access_token="+tokens["canvas"])
    for a in r.json():
        if a["due_at"] != None:
            #print(a['name']+"  "+a["due_at"][0:10])            
            client.headers = {'Asana-Enable': 'new_user_task_lists'}
            result = client.tasks.create_task({"assignee_status": "upcoming",'assignee':'1201343046336008','name': a['name'], 'due_at': a["due_at"], 'workspace':"1201342996618706"}, opt_pretty=True)
            print(result)