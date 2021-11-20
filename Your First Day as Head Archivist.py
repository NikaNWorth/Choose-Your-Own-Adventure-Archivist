#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

#This outlines possible responses
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("Today is your first day as the Head Archivist at the Townville Archives. "
  "\nYou've never been a manager of an information organization before " 
  "\nand you're nervous about what to do, and how to do it right. "
  "\nLuckily, the previous manager left behind a couple books for you. "
  "\nYou look at the shelf breifly, before picking up a book:")
  time.sleep(1)
  print ("""  A. Information services today: An introduction, by Hirsh
  B. 12: Elements of Great Managing, by Wagner and Harter  
  C. Simply Managing, by Mintzberg""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_hirsh()
  elif choice in answer_B:
    option_wagner()
  elif choice in answer_C:
    option_mintzberg()
  else:
    print (required)
    intro()

def option_hirsh(): 
  print ("\nThis book looks interesting, you remember one of "
  "your professors mentioned in when you were in school. You:")
  time.sleep(1)
  print ("""  A. Open it to Chapter 24 - Managing Collections
  B. Open it to Chapter 1- The Transformative Information Landscape: What it Means to be an Information Professional Today  
  C. Open it to Chapter 19 - Strategic Planning""")
  choice = input(">>> ")
  if choice in answer_A:
    option_ch25()
  elif choice in answer_B:
    option_ch1()
  elif choice in answer_C:
    option_ch21()
  else:
    print ("\nMaybe let's look at a different one. "
    "But which one?")
    print ("""  A. Information services today: An introduction, by Hirsh
    B. 12: Elements of Great Managing, by Wagner and Harter  
    C. Simply Managing, by Mintzberg""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hirsh()
    elif choice in answer_B:
        option_wagner()
    elif choice in answer_C:
        option_mintzberg()
        
def option_wagner(): 
  print ("\nThe spine on this one is cracked from the number "
  "of times you've opened it. \nIn your first management job this one "
  "was open on your desk almost all the time. \nIt was especially helpful "
  "when it came to time for your performance review with your boss. \nYou were "
  "able to point to all of the elements you were using\nand all of the ones "
  "you still wanted to incorporate. You:")
  time.sleep(1)
  print ("""  A. Open it to Element 5 - Someone at work cares about me as a person
  B. Open it to Element 4 - Recognition and Praise""")
  choice = input(">>> ")
  if choice in answer_A:
    option_e5()
  elif choice in answer_B:
    option_e4()
  else:
    print ("\nMaybe let's look at a different one. "
    "But which one?")
    print ("""  A. Information services today: An introduction, by Hirsh
    B. 12: Elements of Great Managing, by Wagner and Harter  
    C. Simply Managing, by Mintzberg""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hirsh()
    elif choice in answer_B:
        option_wagner()
    elif choice in answer_C:
        option_mintzberg()

def option_e4():
  print ("\nThis element was one of the hardest for you when you started. "
  "\nLuckily the book provided a lot of feedback on how to integrate it. "
  "\nWould you like to read a quote?. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_e4q()
  else:
    option_readanother()

def option_e5():
  print ("\nThis chapter stood out to a lot when you first read this book. "
  "It's shaped how you've managed every day since then. "
  "You hope your employees here will cared as people and not just employees. "
  "\nWould you like to read a quote?. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_e5q()
  else:
    option_readanother()
    
def option_e5q():
  print ("\nInside the butterfly, milkshake, or Captain Bendo costume "
         "is a manager who wants to know each of his employees and see them succeed. p73 " )
  time.sleep(1)
  print ("""  A. Read another quote
  B. Pick another book
  C. That's enough reading, let's get started """)
  choice = input(">>> ")
  if choice in answer_A:
      print ("""  A. Open it to Element 5 - Someone at work cares about me as a person
          B. Open it to Element 4 - Recognition and Praise""")
      choice = input(">>> ")
      if choice in answer_A:
        option_ch4()
      elif choice in answer_B:
        option_ch6()
      else:
        print ("\nMaybe let's look at a different one. "
        "But which one?")
        print ("""  A. Information services today: An introduction, by Hirsh
        B. 12: Elements of Great Managing, by Wagner and Harter  
        C. Simply Managing, by Mintzberg""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hirsh()
        elif choice in answer_B:
            option_wagner()
        elif choice in answer_C:
            option_mintzberg()
  elif choice in answer_B:
    print ("\n Which one? ")
    option_newbook()
  elif choice in answer_C:
    option_gettowork()
  else:
    print (required)
    option_e5q()
    
def option_e4q():
  print ("\n...the majority of managers and compaines are quicker to swat down "
         "\na problem than they are to praise exemplary performance... Without "
         "\na conscious effort to maintain recognition, the negative events "
         "\nwill continually jump in line before the positive ones. p57 ")
  time.sleep(3)
  print ("""  A. Read another quote
  B. Pick another book
  C. That's enough reading, let's get started """)
  choice = input(">>> ")
  if choice in answer_A:
      print ("""  A. Open it to Element 5 - Someone at work cares about me as a person
          B. Open it to Element 4 - Recognition and Praise""")
      choice = input(">>> ")
      if choice in answer_A:
        option_ch4()
      elif choice in answer_B:
        option_ch6()
      else:
        print ("\nMaybe let's look at a different one. "
        "But which one?")
        print ("""  A. Information services today: An introduction, by Hirsh
        B. 12: Elements of Great Managing, by Wagner and Harter  
        C. Simply Managing, by Mintzberg""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hirsh()
        elif choice in answer_B:
            option_wagner()
        elif choice in answer_C:
            option_mintzberg()
  elif choice in answer_B:
    print ("\n Which one? ")
    option_newbook()
  elif choice in answer_C:
    option_gettowork()
  else:
    print (required)
    option_e4q()
        
def option_mintzberg(): 
  print ("\nOh yeah, this one! "
  "your first boss gave it to you, when you were just starting out as a library aide. You:")
  time.sleep(1)
  print ("""  A. Open it to Chapter 4 - Managing Every Which Way
  B. Open it to Chapter 21 - Management Skills""")
  choice = input(">>> ")
  if choice in answer_A:
    option_ch4()
  elif choice in answer_B:
    option_ch1()
  else:
    print ("\nMaybe let's look at a different one. "
    "But which one?")
    print ("""  A. Information services today: An introduction, by Hirsh
    B. 12: Elements of Great Managing, by Wagner and Harter  
    C. Simply Managing, by Mintzberg""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hirsh()
    elif choice in answer_B:
        option_wagner()
    elif choice in answer_C:
        option_mintzberg()
        
def option_ch4():
  print ("\nYou remember you really liked this chapter. "
  "\nThere was a lot of helpful information about the variety present in management. "
  "\nWould you like to read a quote?. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_ch4q()
  else:
    option_readanother()

def option_ch6():
  print ("\nThere are a lot of sticky notes poking their way out "
  "of this chapter. \nYou remember vaguely the discussion of the "
  "different threads that run through \nthe tapestry of management, "
  "but you can't quite remember the ultimate idea of the chapter. "
  "\nWould you like to read a quote?. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_ch6q()
  else:
    option_readanother()
    
def option_ch4q():
  print ("\nManaging is almost as varied as life itself, "
         "because it is about so much that happens in life itself. p71 " )
  time.sleep(1)
  print ("""  A. Read another quote
  B. Pick another book
  C. That's enough reading, let's get started """)
  choice = input(">>> ")
  if choice in answer_A:
      print ("""  A. Open it to Chapter 4 - Managing Every Which Way
          B. Open it to Chapter 6 - Managing Effectively""")
      choice = input(">>> ")
      if choice in answer_A:
        option_ch4()
      elif choice in answer_B:
        option_ch6()
      else:
        print ("\nMaybe let's look at a different one. "
        "But which one?")
        print ("""  A. Information services today: An introduction, by Hirsh
        B. 12: Elements of Great Managing, by Wagner and Harter  
        C. Simply Managing, by Mintzberg""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hirsh()
        elif choice in answer_B:
            option_wagner()
        elif choice in answer_C:
            option_mintzberg()
  elif choice in answer_B:
    print ("\n Which one? ")
    option_newbook()
  elif choice in answer_C:
    option_gettowork()
  else:
    print (required)
    option_ch4q()
    
def option_ch6q():
  print ("\na healthy organization is not a collection of detached "
         "human resources but a community of engaged human beings. p165 " )
  time.sleep(1)
  print ("""  A. Read another quote
  B. Pick another book
  C. That's enough reading, let's get started """)
  choice = input(">>> ")
  if choice in answer_A:
      print ("""  A. Open it to Chapter 4 - Managing Every Which Way
          B. Open it to Chapter 6 - Managing Effectively""")
      choice = input(">>> ")
      if choice in answer_A:
        option_ch4()
      elif choice in answer_B:
        option_ch6()
      else:
        print ("\nMaybe let's look at a different one. "
        "But which one?")
        print ("""  A. Information services today: An introduction, by Hirsh
        B. 12: Elements of Great Managing, by Wagner and Harter  
        C. Simply Managing, by Mintzberg""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hirsh()
        elif choice in answer_B:
            option_wagner()
        elif choice in answer_C:
            option_mintzberg()
  elif choice in answer_B:
    print ("\n Which one? ")
    option_newbook()
  elif choice in answer_C:
    option_gettowork()
  else:
    print (required)
    option_ch6q()


def option_ch24():
  print ("\nOh! You remember this one! "
  "It was one of your favorites. A lot of good information for an archivist. "
  "\nWould you like to read a quote?. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_ch24q()
  else:
    option_readanother()

def option_ch1():
  print ("\nLet's start at the beginning. "
  "Maybe Hirsh has something that can help us figure out this new role. "
  "\nWould you like to read a quote?. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_ch1q()
  else:
    option_readanother()

def option_ch19():
  print ("\nThis will have some good general information. "
  "Even though a lot of the information was about libraries, "
  "\nyou remember that there was some good advice for managers "
  "\nacross all types of information organizations. "
  "\nWould you like to read a quote?. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_ch19q()
  else:
    option_readanother()
    
def option_ch19q():
  print ("\nStrategy exists to solve a problem--\nspecifically, the problem "
        "of how an organization can \naccomplish its goals with available resources. p232 ")
  time.sleep(1)
  print ("""  A. Read another quote
  B. Pick another book
  C. That's enough reading, let's get started """)
  choice = input(">>> ")
  if choice in answer_A:
      print ("""  A. Open it to Chapter 24 - Managing Collections
          B. Open it to Chapter 1- The Transformative Information Landscape: What it Means to be an Information Professional Today  
          C. Open it to Chapter 19 - Strategic Planning""")
      choice = input(">>> ")
      if choice in answer_A:
        option_ch24()
      elif choice in answer_B:
        option_ch1()
      elif choice in answer_C:
        option_ch19()
      else:
        print ("\nMaybe let's look at a different one. "
        "But which one?")
        print ("""  A. Information services today: An introduction, by Hirsh
        B. 12: Elements of Great Managing, by Wagner and Harter  
        C. Simply Managing, by Mintzberg""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hirsh()
        elif choice in answer_B:
            option_wagner()
        elif choice in answer_C:
            option_mintzberg()
  elif choice in answer_B:
    print ("\n Which one? ")
    option_newbook()
  elif choice in answer_C:
    option_gettowork()
  else:
    print (required)
    option_ch19q()
           
def option_ch1q():
  print ("\nIn today's information landscape, information professionals "
         "\nmust constantly survey the information and technology environment to "
         "\nidentify trends that have implications for the information field. "
         "\nAdapting to these changes is part of what makes being an information "
         "\nprofessional so interesting and exciting. p4 ")
  time.sleep(3)
  print ("""  A. Read another quote
  B. Pick another book
  C. That's enough reading, let's get started """)
  choice = input(">>> ")
  if choice in answer_A:
      print ("""  A. Open it to Chapter 24 - Managing Collections
          B. Open it to Chapter 1- The Transformative Information Landscape: What it Means to be an Information Professional Today  
          C. Open it to Chapter 19 - Strategic Planning""")
      choice = input(">>> ")
      if choice in answer_A:
        option_ch24()
      elif choice in answer_B:
        option_ch1()
      elif choice in answer_C:
        option_ch19()
      else:
        print ("\nMaybe let's look at a different one. "
        "But which one? ")
        print ("""  A. Information services today: An introduction, by Hirsh
        B. 12: Elements of Great Managing, by Wagner and Harter  
        C. Simply Managing, by Mintzberg""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hirsh()
        elif choice in answer_B:
            option_wagner()
        elif choice in answer_C:
            option_mintzberg()
  elif choice in answer_B:
    print ("\n Which one? ")
    option_newbook()
  elif choice in answer_C:
    option_gettowork()
  else:
    print (required)
    option_ch1q()
 
def option_readanother():
    print ("\nI'm too busy to get lost in reading quotes, "
    "\nmaybe I'll check out another book? "
    "\nOr maybe I should just get to work? ")
    print (""" A. Take a look at another book 
 B. Get to work """)
    choice = input(">>> ")
    if choice in answer_A:
        option_newbook()
    if choice in answer_B:
        option_gettowork()
    
def option_newbook():
    print ("\nLet's read a different one. "
    "But which one? ")
    print ("""  A. Information services today: An introduction, by Hirsh
    B. 12: Elements of Great Managing, by Wagner and Harter  
    C. Simply Managing, by Mintzberg""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hirsh()
    elif choice in answer_B:
        option_wagner()
    elif choice in answer_C:
        option_mintzberg()

def option_ch24q():
  print ("\nWith the informaiton organization's focus on informtion "
         "literacy, collection managers must not only maintain collections that work "
         "\nseamlessly with their role as teachers, coaches, and partners "
         "\nin the information exchange process, but they must do much better "
         "\nin promoting these collections so users are aware of them. p290 ")
  time.sleep(1)
  print ("""  A. Read another quote
  B. Pick another book
  C. That's enough reading, let's get started """)
  choice = input(">>> ")
  if choice in answer_A:
      print ("""  A. Open it to Chapter 24 - Managing Collections
          B. Open it to Chapter 1- The Transformative Information Landscape: What it Means to be an Information Professional Today  
          C. Open it to Chapter 19 - Strategic Planning""")
      choice = input(">>> ")
      if choice in answer_A:
        option_ch24()
      elif choice in answer_B:
        option_ch1()
      elif choice in answer_C:
        option_ch19()
      else:
        print ("\nMaybe let's look at a different one. "
        "But which one? ")
        print ("""  A. Information services today: An introduction, by Hirsh
        B. 12: Elements of Great Managing, by Wagner and Harter  
        C. Simply Managing, by Mintzberg""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hirsh()
        elif choice in answer_B:
            option_wagner()
        elif choice in answer_C:
            option_mintzberg()
  elif choice in answer_B:
    print ("\n Which one? ")
    option_newbook()
  elif choice in answer_C:
    option_gettowork()
  else:
    print (required)
    option_ch24q()
    
def option_gettowork():
  print ("\nAlright, enough books for now, it's time to get to work. "
  "\nThere's so much to do! You have to create the strategic plan, "
  "\nset your mission, values, and vision, "
  "\nassess your collection, talk to your staff, set schedules, "
  "\nand so much more! ")
  time.sleep(3)
  print ("\nIt's going to be a hectic first day. "
  "\nBut at least you know you have these resources here for when you need them. ")
  time.sleep(2)
  print ("\nThe End! Thank you for playing! ")

#references
#Hirsh, S. (2018). Information services today: An introduction. Rowman and Littlefield.
#Harter, J. & Wagner, R. (2006). 12: The elements of great managing. Gallup Press.
#Mintzberg, H. (2013). Simply managing: What managers do and can do better. Berret-Koehler Publishers. 

intro()


# In[ ]:




