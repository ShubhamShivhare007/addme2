#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
mouse=Flask(__name__)
@mouse.route('/')
def jfdskjfdkj():
    return render_template('twenty.html')
@mouse.route('/info',methods=['GET','POST'])
def dhjdjhs():
    if(request.method=='POST'):
        num1=int(request.form['a'])
        num2=int(request.form['b'])
        Total=num1+num2
        return render_template('twenty.html',shubham=Total)
if __name__=='__main__':
    mouse.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




