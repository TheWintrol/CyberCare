First of all I've started an HTML code declaring, that it's an HTML file, selecting language.



In head tag, I've declared meta tags with charset UTF-8, because this character set is  capable of encoding all characters on the web.
http-equiv and content is for supporting old, legacy browsers, just in case.
name and content in the meta tag are written because the whole webpage is adaptive depending on the device's screen.



In the body tag, I've created whole layout of the form.
Firstly, I created a "A-container" div to keep all of the posts and form nice and neatly with the same width, display and flex direction.
Secondly, I created a "container" which stores the form with the submit button.
Then I've created a heading, a form and in the form I created 4 more divs, which have span element and input element. 
Every input element has a type depending on the use and also they have ID, which will be useful when JS comes into play.
Also a button was created with a submit type and with a date validation function when a user presses submit button.
Then the selection of the year was craeted with a filtering function.
Lastly, I've created an empty div for the posts, that have been already submitted.



In the style tag, I've set the global margin, padding to 0, set up fonts, box sizing.
Basically, in the style tag I've customized a layout based on the requirements. Set up widths, heights, colors, flex parameters, so that the elements go where they belong.
In the comment section I've added inline-size and overflow-wrap, so that the text, taht the user inputs does not go out of the box.



Lastly, I've taken my posts from the local storage using JSON.parse method.
I didn't need to do any extra work with storing them, because when user clicks submit button, the post automatically goes into the local storage.
I've written a function called drawPosts, which lets me visualize the information, that the user inputs in the form.

In this function I've passed the parameter postai, so that the function could see the information from local storage.
I used if (!postai) to check if the variable is null or undefined. It if was undefined, then the function stops. It happens when there are no posts at the moment in the local storage.
Although if the condition is incorrect, then all the posts are visualized.
Here's where the empty div post-container comes into play. It stores every post, that there is in the local storage after the form and year selection button.
container.innerHTML nulls the HTML file so there's no bugs or interception between the posts.
To visualize all posts, I've set up a for cycle which goes through every post and visualizes it.
In the for cycle every post is visualized with the user data, which he has inputted in the form. 
Here are three different divs - one stores the whole post inside and second stores image and username with date and the third stores only username and date. 
They are divided because that way, it's easier to put sections into right place to mae them visually appealing.
After that there is a container.innerHTML += s, which adds every post.

The checkDate function takes a variable called value, to check if the user entered date is not in the future.
toISOString() function returns a date object as a string, using the ISO standard, so the code understand the date format.

Then there is a validate function, which checks if the user has entered a full name, which contains 2 words. 
[A-Za-z] matches any character from lowercase a through uppercase Z, that way checking if the user has inputted only one word or two.
If the user entered only 1 word, then the error will appear.

After the user presses Submit button, the JS takes every value from the text inputs, that the user has written. I save them in an array, to that I could display them easily when needed.
after that, the code checks if the array is empty by using unshift method. Then it adds valeus to the array.
JSON.stringify() method converts a JavaScript value to a JSON string, so it return readable text and not code values.

The last step was to enable filtering in the webpage.
I've taken the posts from local storage and the value from selection tab.
Then I've created an array which contains only filtered posts.
Lastly, I've created a for cycle, which goes through every post and checks if the selection date matches the post date, that the user has entered. If it does, then the post is saved in the new array and then visualized ont the webpage.



Regarding the back end with Python, since I had to learn this programming language from scratch, I haven't been able to fully fulfill the requirements :( The code has some errors, but the whole logic should be clear. :)

Nevertheless, I've set up Flask, then imported every asset and function in order for Flask to work properly.

Then I have enabled a variavle called app, which was used to reach the database.
After that, I've created a db model with the table data from the posts.
I initialized a resource fields array, which containe the data from the posts.

Then in the Post(Resource) class I've written a code, which helps to filter the table data by a post id with get method.
Then I defined a a put method, which puts the information in the database.

After that, I've added a code to add resource to the API.