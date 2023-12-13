<div margin-bottom="80%">
    <img src="https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/Tech_stack_final_logo_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T113646Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=cbe76986a8a313c88f8890bc2c79a03bda98aa27af1eb96bbe0693a3cf1bf192" align="right" width="200">
</div>

<div>
    <img src="https://github.com/vivifyhealthcare/whatsapp_business_api/assets/127088274/f1633012-f0d3-4b85-9895-733f46735292" width="100"/>  
</div>

<h1 font-size="50px" align="center">Setting up WhatsApp business account</h1>

## Step 1: Download WhatsApp Business App

- If you don't have WhatsApp Business installed on your phone, download it from the Google Play Store (for Android) or the App Store (for iOS).

## Step 2: Verification

#### Open the WhatsApp Business app.

- Enter your phone number for verification. Make sure it's a valid and active phone number as WhatsApp will send a verification code to this number.

- Verify your phone number by entering the code received via SMS.

## Step 3: Set Up Your Business Profile

- After verification, you'll be prompted to set up your business profile. This includes:
- **Business Name:** Enter the name of your business.
- **Business Category:** Choose a category that best describes your business.
- **Business Description:** Add a brief description of your business.

## Step 4: Add Additional Business Information (Optional)

- You can add more details about your business, such as your address, business hours, email, and website. This information can be added later as well.

## Step 5: Customize Your Business Profile

- Upload a profile picture for your business. This could be your logo or another image that represents your business.
- Personalize your business profile to make it more engaging for customers.

## Step 6: Start Using WhatsApp Business Features

- Explore the various business features offered by WhatsApp Business, including:
- Messaging Tools: Use quick replies and labels to efficiently manage customer inquiries.
- Business Hours: Set your working hours to inform customers about your availability.
- Away Messages: Create automated responses for when you're not available.
## Step 7: Promote Your WhatsApp Business Account

- Share your WhatsApp Business number on your website, social media, and other communication channels.
- Consider using the WhatsApp Business API for more advanced business communication and integration.


# How to generate WhatsApp permanent access token 

## Steps: 

- Open your browser search for https://developers.facebook.com. 
- It looks like as below
- <img width=500 src ="https://vivifyassets.s3.ap-south-1.amazonaws.com/developers.facebook2.png">
 
- Click on "Myapps"
-  <img width=500 src="https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/image_24.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T101444Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=e4c43928ff5e1244302777a2098a4b46afbe9865ed8e606b127549fdfb75db1e">
- Click on displayed app 
- In dashborad click on "WhatsApp" and under dropdown click on "API Setup" 
- It will show temparory acess token, since temparory acess will expire in 23hours. so whith this token we need to generate new token after every 23 hours. 
- So to resolve this problem we need to generate permanent access token.
- In WhatsApp dropdown click on "configuration".
- Now click on permeant acecess token displayed in the middle box
- After clicking, it shows few steps to generate permeant token under required assets click on the link point number four.
- <img width = 500 src = "https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/image_31.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T102523Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=48b3eb22fecb0a2eed7cdcb2cbaeec72a9b941d5d5f006fb54e5b9ecfbf17abb">
- The link will navigate to meta business help centre
- <img width = 500 src = "https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/image_32.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T111122Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=68bf2a82544d10e8040c87729eee5702b0c52ab88fe7589e5979fceb1229e4ca">
- It shows steps to get the permeant token.
- Click on "App Dashborad" then select "Business settings." 
- In Dashborad under users click on "system users" it shows as below
- <img width = 500 src = "https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/image_30.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T102355Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=2c3248c778e6e8a8fef244164f6238dfb36694ab0609fa330ef6be3160dad020">
- In that click on "Add" button it shows a dialogue box fill the dialogue box then click on create system user.
- <img width = 500 src = "https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/image_29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T102226Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=cb189789b1577d56ab85b5812256fd0188394a4b1cc882a15e50d8ac073900ea">

- In the same page right side click on "Assign assets" button it will show dialogue box, in this "click on apps" option in the left side.
- <img width = 500 src ="https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/image_28.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T102136Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=64e6fba1fab66b3b9912597395b03fe2d7ba4fe31db1ab38f0d85ec7650e3195">   
- After clicking you will get your business name, select the name clicking on check box and in "manage app" section enable to right, and click on save changes.<image>

- Again in the same page click on "Generate new token", a dialogue box is displayed in that selct the app with your business name, then select on "Never."
- <img width = 500 src ="https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/image_27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T102055Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=26d9fa25ba1653a01307cce3a6713e9b168631d5dd0eaf0bea7690bb53b847a3">
- It follows another drop down in that enable "WhatsApp_business_management" and "WhatsApp_business_messaging" by selecting the check box.
<img width= 500 src ="https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/image_25.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T101909Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=34fabdc20bd266609226fc0b7b3d22746fb7b05ca37b0c0640e52954d17fb332">
- Then click on Generate token as shown in the bottom.
- <img width = 500 src = "https://ivin-pro-data-conversion.s3.amazonaws.com/Ivin_Staging/image_33.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVUQMV7NG27MI2U77%2F20231206%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T111221Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=636ed37b42abfb2dc74cf560e623190cd8f4fd16bc096296797df979648c4975">
- It leads to your permeant acess token, then copy the token in the dialogue box.
- Now a permeant token is avilable to use in the code.


# Message template with image

## Description
Ensure that you have a WhatsApp Business API account. This is typically used by medium and large businesses. If you are a small business or an individual, you might not have access to the API.Visit the official WhatsApp Business API documentation to understand the guidelines and specifications for creating message templates. You may find details about message templates, including supported message types, media formats, and other requirements.
 
## Steps: 

- Click on 'App Dashboard,' and it will display a dialogue box like this:
<img width=500 src ="https://vivifyassets.s3.ap-south-1.amazonaws.com/image.png">

- Within this image, choose 'WhatsApp Manager' and click on the 'Account Tools' option located on the left side.

- Clicking on "Message Templates" will navigate to this page
<img width=500 src ="https://vivifyassets.s3.ap-south-1.amazonaws.com/message+templete.png">

- In the image above, select the 'Create Template' option located on the right side.

- After clicking on 'Create Template,' you'll be prompted to provide information such as category, name, and language. Fill in the required details, then click on the 'Continue' button.

- Next, you can customize your template further by adding an image in the header and entering text in the body.
- 
- Images allow you to showcase your brand, products, or services in a visually consistent way. This helps in reinforcing brand identity and recognition.

- Images can help convey complex information more clearly. For example, if you need to provide step-by-step instructions, an image can make the process easier to understand.

- Make sure your message template and image comply with WhatsApp's policies. This includes guidelines on content, frequency, and user consent.



**Note:** Ensure you comply with WhatsApp Business policies and guidelines to avoid any issues.

<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>
