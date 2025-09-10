class emp:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def inc(self,p):
        self.s=self.s+(self.s*p/100)
    def pr(self):
        print(f"Employee: {self.n} | Salary: {self.s:.2f}") 
e=emp("John",1000)
e.pr()
e.inc(10)
e.pr()
e.inc(20)
e.pr()
e.inc(30)




