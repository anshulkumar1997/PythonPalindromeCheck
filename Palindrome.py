num=int(input())
if (num<10):
   print('Palindrome is ',num)
else:
   def reverse(num):
       temp=num
       rev=0
       while temp!=0 :
           rev=rev*10
           rev+=temp%10
           temp=temp//10
       return rev
   reve=reverse(num)
   if reve==num :
      print(num,' is Palindrome')
   else:
      print(num,' is Not Palindrome')
         
   
