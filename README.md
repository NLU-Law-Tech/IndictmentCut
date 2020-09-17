# IndictmentCut
## Install
```bash
$ pip install -U git+https://github.com/NLU-Law-Tech/IndictmentCut.git
```

### 找事實
```python
def find_fact(Indictment, break_line='\r\n'):
```
```python
from Indictment import find_fact
fact = find_fact(Indictment)
print(fact)
```