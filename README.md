# Femur-Pre-op-Planning-in-Blender-using-Python-scripting
This is a Blender API written in python which acts as an add-on & help in preoperative planning of Femur bone of human anatomy. Pre-op planning involves getting few measurements in the form of anlges and lengths which whill be compared further with standard value range by surgeon to take correct surgical action to reduce damage in damaged bone. For getting these measurements, design engineer has to identify few landmarks, make a few axes, create planes by taking reference from axes and then make few projections in certain plane to get the angles. This becomes a tedius task when repeated for different patient. 

Here's the femur bone for your reference: 

![image](https://user-images.githubusercontent.com/61643913/119250524-43c38700-bbbe-11eb-9b3d-87a022a0b113.png)

Need of an hour is to just have an automatic/semi-automatic way of doing it inorder to reduce the time requirements. Here comes the blender add-on handy. This addon has 4 parts named “Landmarks & axes”, “Projections”, “Angles” &  “MeasureIt”. On expanding we can see buttons under each of these. 

![image](https://user-images.githubusercontent.com/61643913/119250412-8f296580-bbbd-11eb-9f03-1fd833a5018c.png)

Identifying landmarks is still a manual task. User has to keep the 3D cursor at the location which he as identified to be a landmard & press respective button to get the object in scene collection. User has to select total 12 landmarks inorder to get all the meanurements in the end. User can skip few of these as well according to his need. 

![image](https://user-images.githubusercontent.com/61643913/119250420-9e101800-bbbd-11eb-8160-57f8217bcef5.png) ![image](https://user-images.githubusercontent.com/61643913/119250423-a2d4cc00-bbbd-11eb-90b1-4bfa82cebf39.png) ![image](https://user-images.githubusercontent.com/61643913/119250425-a9fbda00-bbbd-11eb-8ae0-6bcc62df15aa.png)

Axes are created by using these landmarks. User just need to click on respective button on the panel to get the axis. Same is applicable for the planes. 

While creating axes, planes or measurements if one or more landmard are missing, on clicking the button, system will show the error message giving information to user about the need of missing item. This also makes sure that system wont crash when user continuously try operations which is missing few essential components. 

![image](https://user-images.githubusercontent.com/61643913/119252917-53e26300-bbcc-11eb-9df8-80cc51c97bf6.png)

