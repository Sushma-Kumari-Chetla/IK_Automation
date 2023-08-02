'''
Assignment 2: Create a basic Framework structure (request generation and validation)
For the test cases above, modularize the code so that there are functions to:
Generate the endpoint
Generate the HTTP request
Generate any headers
Generate any data
Make the HTTP request
Parse out the response status code and body
For validation:
Before validation, please ensure each test case contains a code block
Validate the expected status code is the actual status code
Validate that expected data is somewhere in the response body
In the event of errors and test failures, ensure that the tests have failed.
'''
################ Program ################
import requests
base_url = "https://jsonplaceholder.typicode.com"

# Funtion to generate EndPoint
def generate_endpoint(resource,resource_id = None):
    end_point = f"{base_url}/{resource}"
    if resource_id is not None:
        end_point+=f"/{resource_id}"
    return end_point

#Function to generate http reauest
def generate_http_request(method,end_point,data = None, headers = None):
    response = None
    if method == "GET":
        response = requests.get(end_point,headers = headers)
    if method == "POST":
        response = requests.post(end_point,json = data,headers = headers)
    if method == "PUT":
        response = requests.put(end_point,json = data,headers = headers)
    if method == "PATCH":
        response = requests.patch(end_point,json = data,headers = headers)
    if method == "DELETE":
        response = requests.delete(end_point,headers = headers)
    return response

#Function to generate Headers:
def validate_response(response,expected_status_code,expected_data = None):
    if response.status_code == expected_status_code:
        print("Test Case passed: Response Status Code is as expected")
    else:
        print(f"Test Case Failed: Expected Status Code is {expected_status_code},but got response {response.status_code}")
    if expected_data is not None:
        if expected_data in response.json():
            print("Test Case Passed: Expected Data is present in Response Body")
        else:
            print("Test Case Failed: Expected Data is not present in Response Body")

#Test Cases
#Get/posts
end_point = generate_endpoint("posts")
response = generate_http_request("GET",end_point)
print("Test Case: GET/POSTS")
validate_response(response,200)


#GET/posts/1
end_point = generate_endpoint("posts",1)
response = generate_http_request("GET",end_point)
print("Test Case: GET/posts/1")
validate_response(response,200)

#GET/posts/1/comments
end_point = generate_endpoint("posts",1)+"/comments"
response = generate_http_request("GET",end_point)
print("Test Case: Get/posts/1/comments")
validate_response(response,200)

#GET/comments?postId=1
end_point = generate_endpoint("comments")+"?postId=1"
response = generate_http_request("GET",end_point)
print("Test Case: Get/comments?postId=1")
validate_response(response,200)

#POST/posts
end_point = generate_endpoint("posts")
new_post = {"Userd_Id":2121,
            "title":"New_Post",
            "body":"This is a new Post to test Assignment2"}
response = generate_http_request("POST",end_point,data=new_post)
print("Test Case: POST/posts")
validate_response(response,201)
print(response.text)
print(response.json)

#PUT/posts/1
end_point = generate_endpoint("posts",1)
updated_post = {"User_Id":1212,
                "title":"Updated_Post",
                "body":"This is post is being updated to test Assignment2"}
response = generate_http_request("PUT",end_point,data = updated_post)
print("Test Case: PUT/posts/1")
validate_response(response,200)
print(response.text)
print(response.json())

#PATCH/posts/1
end_point = generate_endpoint("posts",1)
updated_data = {"title":"PATCH WORK"}
response = generate_http_request("PATCH",end_point,updated_data)
print("Test Case: PATCH/posts/1")
validate_response(response,200)
print(response.text)
print(response.json())

# DELETE/posts/1
end_point = generate_endpoint("posts",1)
response = generate_http_request("DELETE",end_point)
print("Test Case: DELETE/posts/1")
validate_response(response,200)