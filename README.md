# cisco-assignment
Cisco Assignment

STEPS TO RUN THE APP (Ubuntu OS):
---------------------------------
1. virtualenv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python app.py (To run the app in CLI. CTL+C to stop the app.)
5. http://0.0.0.0:5000 will return 'Welcome To Cisco!' (Note: In terminal we need to check whether the host is 0.0.0.0 or its changed)

Ping API
--------
1. method : POST
2. endpoint : http://0.0.0.0:5000/api/ping
3. post data : {
	"url": "https://reqres.in/api/users?page=1"
}
4. response : {
    "status": true,
    "message": "Payload data loaded successfully",
    "data": [
        {
            "id": 1,
            "email": "george.bluth@reqres.in",
            "first_name": "George",
            "last_name": "Bluth",
            "avatar": "https://reqres.in/img/faces/1-image.jpg"
        },
        {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        }
    ]
}

Info API
--------
1. method : GET
2. endpoint : http://0.0.0.0:5000/api/info
3. response : {
    "Receiver": "Cisco is the best!"
}

