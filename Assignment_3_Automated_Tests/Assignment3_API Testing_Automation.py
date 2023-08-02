'''
With your new framework, write some tests for each endpoint such that the endpoint is supposed to fail with a non-200 status code,
and validate the expected status code returned.
'''
import requests
base_url = "https://jsonplaceholder.typicode.com"

def generate_endpoint(resource,resource_id = None):
    endpoint = f"{base_url}/{resource}"
    if resource_id is not None:
        endpoint+=f"/{resource_id}"
    return endpoint

def generate_http_request(method,endpoint,data = None,headers = None):
    response = None
    if method == "GET":
        response = requests.get(endpoint,headers = headers)
    if method == "POST":
        response = requests.post(endpoint,json = data, headers = headers)
    if method == "PUT":
        response = requests.put(endpoint,json = data,headers = headers)
    if method == "PATCH":
        response = requests.patch(endpoint,json = data, headers = headers)
    if method == 'DELETE':
        response = requests.patch(endpoint,json = data, headers = headers)

    return response

def validate_response(response,expected_status_code,expected_data = None):
    if response.status_code == expected_status_code:
        print(f"Test Case PASSED: Response status code is as expected - {expected_status_code}")
    else:
        print(f"Test Case FAILED: Expected Status_code is {expected_status_code}, but Code is {response.status_code}")

    if expected_data is not None:
        if expected_data == response.json():
            print("Test Case PASSED: Expected Data is present in Response")

        else:
            print("Test Case FAILED: Expected Data is not present in Response")
        print(f"Expected Data: {expected_data}")
        print(f"Response Data: {response.json()}")

#Test Cases
def test_cases():
    #GET/posts
    endpoint = generate_endpoint("posts")
    response = generate_http_request("GET",endpoint)
    print("Test Case: GET/posts")
    validate_response(response,200)
    print("Negative Test Case: GET/posts - Expected 201")
    validate_response(response,201)

    #GET/posts/1
    endpoint = generate_endpoint("posts",1)
    response = generate_http_request("GET",endpoint)
    print("Test Case: GET/posts/1")
    validate_response(response,200)
    endpoint = generate_endpoint("post",1)
    response = generate_http_request("GET",endpoint)
    print("Negative_Test Case: GET/post*/1")
    validate_response(response,200)

    #GET/posts/1/comments
    endpoint = generate_endpoint("posts",1)+"/comments"
    response = generate_http_request("GET",endpoint)
    print("Negative Test Case: GET/posts/1/comments - with expected 404")
    validate_response(response,404)

    #GET/comments?postId=1
    endpoint = generate_endpoint("comments")+"?postId=1"
    response = generate_http_request("GET",endpoint)
    print("Test Case: GET/comments?postId=1")
    validate_response(response,200)
    print("Negative Test Case: GET/comments?postId=1")
    validate_response(response,501)

    #POST/posts
    endpoint = generate_endpoint("posts")
    new_post = {"User_ID":1,
                "title":"NEW POST",
                "Body":"NEW POST TO TEST ASSIGNMENT 3",
                "id":101}
    responses = generate_http_request("POST",endpoint,data = new_post)
    print("Test Case: POST/posts")
    validate_response(responses, 201, new_post)
    print("Negative Test Case: POST/posts - Validating response of Get/comments?postID=1")
    validate_response(response,201,new_post)

    # PUT/posts/1
    endpoint = generate_endpoint("posts",1)
    updated_post = {"User_ID":43,
                "title":"Updating to verify Put",
                "Body":"Updating Post to Test Assignment3"}
    response = generate_http_request("PUT",endpoint,data = updated_post)
    print("Negative Test Case: PUT/posts/1 - Invalid expected code")
    validate_response(response,201)
    print("Negative Test Case: PUT/posts/1 - Comparing text of with Post TC")
    validate_response(responses,200)

    # PATCH/posts/1
    endpoint = generate_endpoint("posts",1)
    updated_data = {"userId":"XX",
                    "id":"YY"}
    response = generate_http_request("PATCH",endpoint,data = updated_data)
    print("Test Case: PATCH/posts/1")
    validate_response(response,200)
    print("Negative Test Case: PATCH/posts/1 - compare with wrong expected result")
    validate_response(response,500)

    # DELETE/posts/1
    endpoint = generate_endpoint("posts",1)
    response = generate_http_request("DELETE",endpoint)
    print("Negative Test Case: DELETE/posts/1 - Comparing with a string expected value'200'")
    validate_response(response,"200")

def main():
    test_cases()

if __name__ == "__main__":
    main()