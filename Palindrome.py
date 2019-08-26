num=int(input())
su=0
if (num<5):
   su=num+num
   print(su)
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
   su=reve+num 
   reve=reverse(su)
   if reve==su :
      print('Palindrome is ',su)
   else:
      while reve!=su :
         su=reve+su
         reve=reverse(su)
      print ('Palindrome is',su)
         
   
