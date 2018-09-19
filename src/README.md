# Blogger's API
 *bloggers-api.herokuapp.com*
This is an CRUD API for bloggers, which means bloggers can:
* Create a profile: 
* Edit their profile
* Delete their profile
* Login
* List other bloggers profile
* Post a blog 
* Edit their blog 
* Delete their own blog
* List other blogger's blog
* Search for bloggers by name or email
---
This can be achieved via these endpoints and requests:
* Profiles (url: bloggers-api/herokuapp.com/api/)
    * Create a profile: POST bloggers-api/herokuapp.com/api/profile/ {"email": "", "name" : "", "password": ""}
    * Edit their profile PUT bloggers-api/herokuapp.com/api/profile/id {"id":"", "email": "", "name": ""}
    * Delete their profile DELETE bloggers-api/herokuapp.com/api/id 
    * List other bloggers profile GET bloggers-api/herokuapp.com/api/profile

* Login
    * Login POST bloggers-api/herokuapp.com/api/login {"useraname": "", "password": ""}

* Blog
    * Post a blog POST bloggers-api/herokuapp.com/api/feed {"status_text" : ""}
    * Edit their blog PUT bloggers-api/herokuapp.com/api/feed/id/  {"id", "status_text": ""}
    * Delete their own blog DELETE bloggers-api/herokuapp.com/api/feed/id
    * List other blogger's GET blog bloggers-api/herokuapp.com/api/feed
    * Search for bloggers by name or email bloggers-api/herokuapp.com/api/