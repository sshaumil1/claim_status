# claim_status
### 1. Problem Statement
The insurance conpany wants to know about it's costomers claim the insurance or not.

### 2. Brainstorming 
After getting problem statement  i concluded that, some of the parameters can affect this problem. the parameters are city or area, where more chances to accident, what is the population on same area (by means of people and vehicles), age of car also can affect, etc.

### 3. Data Gathering
So, i get data from the kaggel website. I downloaded the csv file. first i had to validate the data first, is the data fit for our problem statement or not. So, i got the data is good according to solve this problem. That's why i read the csv file and made a data frame named train_df.
The data was labelled and had 43 independent features and target feature named is_claim. and independent features are:

1. policy_id: In this feature all the policy id's are present
2. policy_tenure: this feature has the tenure of policy
3. age_of_car: The age of the car is present in this feature
4. age_of_policyholder: The policy holder age is included in this feature
5. area_cluster: The feature has the area, from which area the policy holder came
6. population_density: population of the area is present in this feature
7. make: feature has the values in digits
8. segment: feature provides the information regarding segments from which the vehicle came
9. model: feature has information regarding model
10. fuel_type: the feature has the information regarding fuel type of the vehicle
11. max_torque: feature is about, what is the maximum torque of the vehicle.
12. max_power: feature is about, what is the maximum power of the vehicle.
13. engine_type: feature is about, what is the engine type of the vehicle.	
14. airbags: feature is about, how many airbags in the vehicle.	
15. is_esc: feature has information regarding is vehicle has (Electronic Stability Control) or not.
16. is_adjustable_steering: feature has information regarding is car has adjustable steering or not.
17. is_tpms: feature has information regarding is vehicle has tpms(tire-pressure monitoring system) or not.
18. is_parking_sensors: feature has information regarding is car has parking sensors or not.	
19. is_parking_camera: feature has information regarding is car has parking camera or not.
20. rear_brakes_type: feature has information regarding what are the barke type of the vehicle.	
21. displacement: feature is all about how much displacement is in your vehicle.
22. cylinder: feature is about how many cylinders in the vehicle.
23. transmission_type: feature has information regarding transmission of the vehicle.
24. gear_box: how many gear_box in the vehicle. 
25. steering_type: what is the steering type of the vehicle.
26. turning_radius: what is the turning radius fo the vehicle. 
27. length: what is the length of the vhicle.
28. width: what is the width of the vehicle.
29. height: what is the width of the vehicle. 
30. gross_weight: what is the gross weight of the vehicle. 
31. is_front_fog_lights: feature has information regarding is vehicle has front fog light or not.
32. is_rear_window_wiper: feature has information regarding is vechicle has rear window wiper or not.
33. is_rear_window_washer: feature has information regarding is vehicle has rear window washer or not.	
34. is_rear_window_defogger: feature has information regarding is vehicle has rear window defogger or not.
35. is_brake_assist: feature has information regarding is vehicle has brrake assist or not.	
36. is_power_door_locks: feature has information regarding is vehicle has power door locks or not.	
37. is_central_locking: feature has information regarding is vehicle has central locking system or not.	
38. is_power_steering: feature has information regarding is vehicle has power steering system or not.
39. is_driver_seat_height_adjustable: feature has information regarding is vehicle has driver seat height adustable or not.
40. is_day_night_rear_view_mirror: feature has information regarding is vehicle has day and night rear view mirror or not.
41. is_ecw: feature has information regarding is vehicle has esw or not.
42. is_speed_alert: feature has information regarding is vehicle has speed alert or not.
43. ncap_rating: what is the ncap(safty) rating of the car.

So, by seeing all the features we have to decide that will owner of the vehicle claim the insurance or not.

### 4. EDA
first i checked for null iformation of the features with memory use then i cheked for null values and got no null values. Then i checked for duplicate values and got no duplicated records. Then i checked all the statics of the features with describe funtion. Then i cheked the count plot and found that the data is highly imbalanced.
