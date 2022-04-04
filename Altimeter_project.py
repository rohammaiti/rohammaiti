while(True):
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)	
    
    print("Please press Q to quite.")
    a=input("Please enter the altitude at which you want the plane to fly-") #altitude of the aircraft in feet.1ft=0.0003048km
    b=(input("Enter the distance from the destination-"))#distance in nautical miles. 1 nautical mile= 1.852km approximately.
    if a=='Q':
        break
    if b=='Q':
        break
    
    a = float(a)
    b = float(b)
    if a==37000 and b>=500:
        print("Maintain the height or decend")
        
    elif a==37000 and b<=499:
        print("Maintain the height, decend or prepare for landing")
        
    elif a>=35000 and b<=400:
        print("Prepare for the process of decend")
        
    elif a==28000 and b>=500:
        print("Maintain the height or decend")
        
    elif a>=28000 and b<=499:
        print("Maintain the height or decend")
        
    elif a==21000 and b>=500:
        print("Maintain the height or decend")
        
    elif a>=21000 and b<=499:
        print("Maintain the height or decend")
        
    elif a==14000 and b>=500:
        print("Maintain the height, decend or prepare for landing")
        
    elif a>=14000 and b<=499:
        print("Maintain the height or prepare for decend")
    
    elif a==10000 and b>=500:
        print("Maintain the height, acend or decend to a lower level")
    
    elif a==10000 and b<=499:
        print("Prepare for decend")
        
    elif a==9000 and b<=499:
        print("Prepare for landing")
    
    elif a>=9000 and b<=499:
        print("Prepare for landing")
        
    elif a==8000 and b<=499:
        print("Prepare for landing")    
    
    elif a>=8000 and b<=499:
        print("Prepare for landing")
        
    elif a==7000 and b<=499:
        print("Prepare for landing")    
    
    elif a>=7000 and b<=499:
        print("Prepare for landing")
        
    elif a==6000 and b<=499:
        print("Prepare for landing") 
    
    elif a>=6000 and b<=499:
        print("Prepare for landing")
        
    elif a==5000 and b<=499:
        print("Prepare for landing")    
    
    elif a>=5000 and b<=499:
        print("Prepare for landing")
        
    elif a==4000 and b<=499:
        print("Prepare for landing")
    
    elif a>=4000 and b<=499:
        print("Prepare for landing")
        
    elif a==3000 and b<=499:
        print("Prepare for landing")  
    
    elif a>=3000 and b<=499:
        print("Prepare for landing")    
    
    elif a==2000 and b<=499:
        print("Prepare for landing and extend the landing gear")
    
    elif a>=2000 and b<=499:
        print("Prepare for landing and extend the landing gear")
    
    elif a==1000 and b<=499:
        print("Prepare for landing and extend the landing gear")
        
    elif a>=1000 and b<=499:  
        print("Prepare for landing and extend the landing gear")
        
    else:
        print("Navigate according to ATC commands")
    
    measure_altitude=a*0.0003048
    measure_altitude=float(measure_altitude)
    print("The altitude of the plane from the ground approximately in km=", measure_altitude)
    
    measure_distance=b*1.852
    measure_distance=float(measure_distance)
    print("The distance of the plane from the destination airport is approximately in km=", measure_distance)
