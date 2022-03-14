# My Custom rsa encryption Algorithm from start


**I was learing about rsa and thought how hard it is to make, making a fully working algorithm was not that hard but making it fast is ...completly another thing, so just created a basic rsa algorithm with simple public and private key(I tried to crack it and end result is ... maybe I need a 🤔 faster computer)**

**How to use (Only for me if I forget somehow😊)**


```
from rsa import RSA
import time #Only for time checking

r = RSA()
print(r.public_key,r.private_key)
text = 1000 * "This is a test"


start = time.process_time()
t = r.encrypt(text)
print(t)

d = r.decrypt(t)
print(d)

print(time.process_time() - start)

```


**Took about 0.002s to complete(👆code) and I only used 200 prime numbers, time increase o(n²)(maybe!!)**
