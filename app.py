#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def jfdskjfdkj():
    return render_template('twenty.html')
@app.route('/info',methods=['GET','POST'])
def dhjdjhs():
    if(request.method=='POST'):
        num1=int(request.form['a'])
        num2=int(request.form['b'])
        Total=num1+num2
        return render_template('twenty.html',shubham=Total)
if __name__=='__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




