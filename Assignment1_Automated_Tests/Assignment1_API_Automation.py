import requests
base_url = "https://jsonplaceholder.typicode.com"

def result(response):
    if response.status_code // 100 == 2:
        print("Request Successful")
        print("Response Status Code:",response.status_code)
        print("Response Data:")
        print(response.json())
    else:
        print("Request Failed")
        print("Response Status Code: ",response.status_code)
        print("Response Data:")
        print(response.json())

def test_cases():
    #GET/posts
    response = requests.get(f"{base_url}/posts")
    print("Test Case: GET/posts")
    result(response)

    #Get/posts/1
    response = requests.get(f"{base_url}/posts/1")
    print("Test Case: Get/posts/1")
    result(response)

    #Get/posts/1/comments
    response = requests.get((f"{base_url}/posts/1/comments"))
    print("Test Case: Get/posts/1/comments")
    result(response)

    #Get/comments?postID=1

    response = requests.get(f"{base_url}/comments?postId=1")
    print("Test Case: Get/comments?postId=1")
    result(response)


    #Post/posts
    new_post = {"user_id":1,
                "title":"New Post",
                "body":"This is a new post created for Testing"}
    response = requests.post(f"{base_url}/posts",json = new_post)
    print("Test Case: Get/posts")
    result(response)

    #Put/posts/1
    updated_post = {"user_id":1,
                "title":"Updated Post",
                "body":"This is an Updated post created for Testing"}
    response = requests.put(f"{base_url}/posts/1",json = updated_post)
    print("Test Case: Get/posts/1")
    result(response)

    #Patch/posts/1
    updated_data = {"title":"Updated Data"}
    response = requests.patch(f"{base_url}/posts/1",json = updated_data)
    print("Test Case: Get/posts/1")
    result(response)

    #Delete/posts/1
    response = requests.delete(f"{base_url}/posts/1")
    print("Test Case: Delete/posts/1")
    result(response)

def main():
    test_cases()

if __name__ == "__main__":
    main()