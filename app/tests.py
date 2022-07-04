from django.test import TestCase

# Create your tests here.

def test_login(self): # Method name should start with 'test'.
    data = {
        "username": "testuser@gmail.com",
        "password": "password"
    }
    url = reverse('user_login')
    res = self.client.post(url, data)
    self.assertEquals(res.status_code, 200)
    self.assertEquals(res.data, 'Login success')

def test_register(self):
    data = {
        "first_name": "test",
        "last_name": "user",
        "gender": "Male",
        "dob": "2000-01-01",
        "email": "testuser@gmail.com",
        "password": "password",
        "phone": "123456789"
    }
    url = reverse('user_register')
    res = self.client.post(url, data)
    # print(res.data)
    self.assertEquals(res.status_code, 200)
    self.assertEquals(res.data, 'Successfully registered')

def test_updatePassword(self):
    data = {
        "username": "testuser@gmail.com",
        "current_password": "password",
        "new_password": "newpassword"
    }
    url = reverse('update_password')
    res = self.client.post(url, data)
    self.assertEquals(res.ststus_code, 200)
    self.assertEquals(res.data, 'Password updated successfully')

def test_insertPost(self):
    data = {
        "username": "testuser@gmail.com",
        "content": "My new post"
    }
    url = reverse('insert_post')
    res = self.client.post(url, data)
    self.assertEquals(res.ststus_code, 200)
    self.assertEquals(res.data, 'Post uploaded successfully')

def test_deletePost(self):
    data = {
        "post_id" : 23
        }
    url = reverse('delete_post')
    res = self.client.post(url, data)
    self.assertEquals(res.ststus_code, 200)
    self.assertEquals(res.data, 'Post deleted successfully')
