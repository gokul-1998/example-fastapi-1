
from.database import client,session
from app import schemas



def test_toot(client):
    # session.query() we can query db
    res=client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message')=="Hello World"
    assert res.status_code==200
    
def test_create_user(client):
    res=client.post("/users/",json={"email":"hello123@gmail.com","password":"password"})
    new_user=schemas.UserOut(**res.json())
    assert new_user.email=="hello123@gmail.com"
    assert res.status_code==201