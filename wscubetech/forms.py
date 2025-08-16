from django import forms
 
class userForm(forms.Form):  #forms ko inherite karke .Form ko use kiya hai
    num1 = forms.CharField()
    num2 = forms.CharField() 
     