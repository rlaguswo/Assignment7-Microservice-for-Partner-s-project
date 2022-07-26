# CS361-Assignment7-MLS-player-Microservice



A.Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.
  First when the user clicks the info link, the main application request URL by sending row index of the csv. 
  <img width="362" alt="Screen Shot 2022-07-25 at 11 11 32 PM" src="https://user-images.githubusercontent.com/103084098/180936711-e8f693f3-d5b3-42bb-b6ef-8f073bf911c0.png">

  
  Second, the microservice receives the request from the main application.
  <img width="326" alt="Screen Shot 2022-07-25 at 11 12 58 PM" src="https://user-images.githubusercontent.com/103084098/180936108-45d9b8f5-504b-489a-969c-f5783fce65b6.png">

B.Clear instructions for how to RECEIVE data from the microservice you implemented
  After the microservice receives the request from the main application, the microservice creates URL.
<img width="650" alt="Screen Shot 2022-07-25 at 11 13 59 PM" src="https://user-images.githubusercontent.com/103084098/180936248-3d27eea1-7665-4126-9f34-a07379538c9a.png">
 The microservice sends created url to the main application.
<img width="217" alt="Screen Shot 2022-07-25 at 11 14 56 PM" src="https://user-images.githubusercontent.com/103084098/180936388-6892366d-b2e6-4f28-8280-b0adb4a16a96.png">

The main application receives Data(created URL) from the microservice by using zeromq, and then provide to the user by printing the url on the webpage.
<img width="491" alt="Screen Shot 2022-07-25 at 11 16 20 PM" src="https://user-images.githubusercontent.com/103084098/180936581-ea31152d-bc5a-4c95-b640-f18c9357ed72.png">


C. UML Sequance Diagram. 
<img width="80%" src= "https://user-images.githubusercontent.com/103084098/180919103-de84842a-0862-4523-894c-0ba5ee97875a.jpeg">
