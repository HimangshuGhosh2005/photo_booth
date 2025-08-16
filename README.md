Project: Photo API Stubs (For Future Use) 
Problem Statement: You are to create stub endpoints that simulate the behavior of a photo 
management backend. These stubs will prepare the backend structure for future full-featured photo 
upload and retrieval functionality. 
• Create a POST /api/photos/upload endpoint that accepts a photo upload request and 
returns a response with a generated photoId, along with metadata like filename, size, and 
uploadTime. 
• Create a GET /api/photos endpoint that returns a list of photo objects, each containing fields 
such as id, name, url, and uploadedAt. 
• Responses should be properly formatted in JSON and follow consistent schema conventions 
to make future integration smoother.

added feature: delete endpoint that recieves object id ad deletes the object

problem faced:
in basic django in POST from postman can not able to send CSRF token so used parser class from drf

<img width="455" height="445" alt="image" src="https://github.com/user-attachments/assets/80f87a11-24d9-4f0e-b017-8d74b14d4a3b" />
