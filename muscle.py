result1=[]
list=[]
a1=[]
result2=[]
a=input("Enter your Name: ")
print(" Hello",a,"I will ask you about your symptoms and try to diagnose your illness type")
print("ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
questions= [
        {
           "q":"1/Can the player use the injured muscle and continue playing?    1:yes   2:no   3:Relatively poor muscle strength",
            "1": ["Bruises"  ,"Muscle contraction"],
            "2":["Partial rupture","Total rupture"],
            "3":["Tightening of the muscles"]
        },


        {
            "q":"2/Is there bleeding / oozing blood?    1:Minor bleeding   2:severe bleeding  ",
            "1": ["Bruises" ],
            "2":["Tightening of the muscles","Partial rupture","Total rupture"],
            
        },


        {"q":"3/Do you feel pain in the form?    1:knife strike  2:tingling  3:Else",
            "1": ["Partial rupture" ],
            "2":["Bruises" ,"Muscle contraction"],
            "3":[""]
            
        },



        {
           "q":"4/Is there a continuous contraction in the affected muscle?   1:severe contracture  2:Simple contraction ",
           "1":[""],
           "2":["Muscle contraction"],
           "3":[""]
           
        },


        {
           "q":"5/Do you feel stiff when stressed?    1:yes   2:no  ",
           "1": ["inflammation"  ,"stress"],
            "2": [""],
            "3": [""]
        },


        {
           "q":"6/Do you feel weak in the muscle and lack of flexibility?    1:yes   2:no  ",
           "1": ["inflammation"  ,"stress"],
           "2": [""],
            "3": [""]
        },
        
        
        {
          "q":"7/Do you notice an increase in symptoms when exposed to a cold?    1:yes   2:no  ",
           "1": ["inflammation" ],
           "2": [""],
            "3": [""]
        },
        
        
        {
           "q":"8/Do you feel pain when the doctor presses on the affected area, the bone with the muscles that sprout from it?    1:yes   2:no  ",
           "1": ["inflammation"],
           "2": [""],
            "3": [""]
        },
        
        {
          "q":"9/Do you feel very tired and exhausted, and the level of physical abilities decline?    1:yes   2:no  ",
           "1": ["stress"],
           "2": [""],
            "3": [""]
        },
        
        {
           "q":"10/Do you notice a gradual increase in swelling during the first 24 hours after the injury?    1:yes  2:To some extent  3:no",
           "1": ["Partial rupture" ],
           "2":["Bruises"  ,"Muscle contraction"],
            "3": [""]
        },

        {
           "q":"11/Does the skin color change?   1:yes  2:To some extent  3:no",
           "1": ["Bruises"],
           "2":["Tightening of the muscles"  ,"Partial rupture","Total rupture"],
            "3": ["Muscle contraction","inflammation","stress"]
        },

        {
           "q":"12/Is there a tumor?   1:yes  2:To some extent  3:no",
           "1":  ["Bruises"],
           "2":["inflammation","Tightening of the muscles"  ,"Partial rupture","Total rupture"],
            "3": ["Muscle contraction","stress"]
        },

        {
           "q":"13/Is the blood gathering clear around the site of the injury, especially after 48 hours have passed?    1:yes  2:To some extent  3:no",
           "1": ["Bruises" ,"Partial rupture" ],
           "2":[""],
            "3": [""]
        },

        {
           "q":"14/Is there a gap or depression in the place of injury?    1:yes  2:simple  3:no",
           "1": ["Total rupture" ],
           "2":["Partial rupture"],
            "3": [""]
        },

        {
           "q":"15/Does the temperature change locally?    1:yes    2:no",
           "1": ["Bruises","Partial rupture", "Total rupture"],
           "2":[""],
            "3": [""]
        },

        {
           "q":"16/Can the continuous contraction be seen and touched by hand?    1:yes   2:no",
           "1": ["Muscle contraction"],
           "2":[""],
            "3": [""]
        },

        {
           "q":"17/Is there a low level of neuromuscular compatibility?   1:yes  2:no",
           "1": ["stress"],
           "2":[""],
            "3": [""]
        },

        {
           "q":"18/Can you move the injured muscle?   1:yes  2:Simple movement  3:no",
           "1": [""],
           "2":["Bruises"  ,"inflammation","Tightening of the muscles"],
            "3": ["Muscle contraction","stress","Total rupture"]
        },

        {
           "q":"19/How does the injury occur as a result of external shock or external violence, such as colliding with a solid object or the player’s body?    1:yes  2:no",
           "1": ["Bruises"],
           "2":[""],
            "3": [""]
        },

        {
           "q":"20/The way the injury occurs is the result of overstretching some of the fibers in the muscle    1:yes  2:no",
           "1": ["Tightening of the muscles","Partial rupture" ],
           "2":[""],
            "3": [""]
        },

        {
           "q":"21/How does the injury occur as a result of the sudden violent muscle contraction to resist an external force at the moment of its occurrence when the muscle is not prepared for that?    1:yes  2:no",
           "1": ["Muscle contraction","Partial rupture","Total rupture" ],
           "2":[""],
            "3": [""]
        },

        {
           "q":"22/The way the injury occurred as a result of an involuntary contraction of the muscle so that it cannot be relaxed?    1:yes  2:no",
           "1": ["Muscle contraction" ],
           "2":[""],
            "3": [""]
        },

        {
           "q":"23/How does the injury occur as a result of chronic stress and tension on the small fibers that connect the muscle to the bone area associated with it?   1:yes  2:no",
           "1": ["inflammation"],
           "2":[""],
            "3": [""]
        },

        {
           "q":"24/How did the injury occur as a result of a decrease in the player's efficiency and ability, with severe pain when performing muscular effort?    1:yes  2:no",
           "1": ["stress"],
           "2":[""],
            "3": [""]
        }
    
        ]
for question in questions:
    
    question_text = question.get('q')

    print(question_text)

    user_answer= input("Enter answer: ")
    list.append(user_answer)
    print (list)

    for k,v in question.items():
        for l in list:
            
            a1=question.get(user_answer)

    result1.append(a1)
    print(result1)

     
for i in result1:
    for z in i:
        result2.append(z)
print(result2)
            
           
counter = 0
str = result2[0]
     
for v in result2:
    curr_frequency = result2.count(v)
    if(curr_frequency> counter):
        counter = curr_frequency
        str = v
        
# print(str)

if str == "Bruises" and 5<= counter <= 9 :
    print("ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
    print("From The Symptoms You Have Mentioned,You Are Probably Infected With " + str )
    print("Your Treatement ,   ")
    print("Rest time before starting the treatment program: 24-48 hours.    ")
    print( "Duration of the treatment program: 1-10 days")

elif str == "Muscle contraction" and 5<= counter <= 9 :
    print("ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
    print("From The Symptoms You Have Mentioned,You Are Probably Infected With " + str )
    print("Your Treatement ,   ")
    print("Rest time before starting the treatment program: 1-3 days.    ")
    print( "Duration of the treatment program: 1 week")

elif str == "inflammation" and 4<= counter <= 7 :
    print("ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
    print("From The Symptoms You Have Mentioned,You Are Probably Infected With " + str )
    print("Your Treatement ,   ")
    print("Rest time before starting the treatment program: 2-4 days.    ")
    print( "Duration of the treatment program: 1-3 weeks")

elif str == "stress" and 4<= counter <= 7 :
    print("ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
    print("From The Symptoms You Have Mentioned,You Are Probably Infected With " + str )
    print("Your Treatement ,   ")
    print("Rest time before starting the treatment program: 2-4 days.    ")
    print( "Duration of the treatment program: 1-10 days")
        
elif str == "Tightening of the muscles" and 3<= counter <= 5 :
    print("ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
    print("From The Symptoms You Have Mentioned,You Are Probably Infected With " + str )
    print("Your Treatement ,   ")
    print("Rest time before starting the treatment program: 2-4 days.    ")
    print( "Duration of the treatment program: 10-20 days")

elif str == "Partial rupture" and 7<= counter <= 10 :
    print("ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
    print("From The Symptoms You Have Mentioned,You Are Probably Infected With " + str )
    print("Your Treatement ,   ")
    print("Rest time before starting the treatment program: 3-6 days.    ")
    print( "Duration of the treatment program: 3-7 weeks")

elif str == "Total rupture" and 6<= counter <= 8 :
    print("ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
    print("From The Symptoms You Have Mentioned,You Are Probably Infected With " + str )
    print("Your Treatement ,   ")
    print("Rest time before starting the treatment program: According to the opinion of the doctor and after surgery if needed    ")
    print( "Duration of the treatment program: 5-12 weeks")
else:
    print("TRY AGAIN")

            

     


















