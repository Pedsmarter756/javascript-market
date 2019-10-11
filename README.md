# [Data Centric Development Cookbook Application](https://dcd-cookbook.herokuapp.com/)

I have greated this online cookbook using the Python framework Flask and MongoDB for the Data Centric Development module of the Code Institute Full Stack Web Development diploma. This application allows users to create an account in order to add, edit or delete recipes and to manage the categories associated with them. Users who do not have an account are still able to browse the recipes on the homepage, and filter by category but are restricted to this by basic user authentication.

## UX

From looking at other recipe site ideas on [Dribbble](https://dribbble.com/search?q=cookbook) I knew I wanted to display the recipe information on a 'card', so that it looks like the recipe cards you can pick up from supermarkets. The homepage displays all of the recipes in a browse view, and the user can click the filtering options to narrow this down by category i.e. 'Breakfast' for fast filtering.
I took inspiration for the colour scheme from [Color-Hex](https://www.color-hex.com/color-palette/827)

## User Stories

- A user (with or without an account) wants to view recipes: They can view the recipes on the [homepage](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/home.html), and [filter](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/filter.html) by category. The user can click on a card to open up the recipe view.

- A user would like to add a recipe: 
  - The user needs to sign in/create an account to add a recipe. 
  - They should choose to login or sign up from the CTA buttons in the navbar (or side menu if viewing on mobile)
  - On either the login or sign up page, they should enter a username and password, and click the button to sign in or create an account
  - Once logged in, they can choose the 'Add Recipe' option in the navbar
  - The user is navigated to a [form](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/addrecipe.html) in which they can fill in the necessary information about their recipe
  - The form has validation, so all fields must be filled in before the 'Add' button will work.
  - Once they have completed all fields and clicked to ['Add'](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L96-L117) the data will be posted to the database and they will redirected back to their [My Recipes](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/profile.html) page where their recipe will be displayed in the lister view.

- A user wants to edit a recipe:
  - The user must be already logged in, and the user must be the owner of the recipe.
  - If both of the above are satisfied, on the My Recipes page there will be an 'Edit' button inside the card of each recipe.
  - The user clicks the 'Edit' button and is taken to an [editing form](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/editrecipe.html). The form is pre-filled with the information about the recipe that they inputted.
  - The user can change aspects that they would like to (validation still applies so no fields can be left incomplete)
  - The user can press the button to 'Save changes' or 'Cancel' if they change their mind. Pressing ['Save changes'](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L120-L143) will post the changes to the database and redirect the user back to the My Recipes page.
  
- A user wants to delete a recipe:
  - The user must be already logged in, and the user must be the owner of the recipe.
  - If both of the above are satisfied, on the My Recipes page a 'Delete' button will appear inside the card.
  - If the user clicks the ['Delete'](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L146-L149) button, the recipe will be deleted and the user will remain on the My Recipes page.
  
- A user wants to add a category:
  - The user must be already logged in.
  - Once logged in, the user can click the ['Manage Categories'](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/categories.html) button in the navbar.
  - The user clicks ['Add Category'](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/addcategory.html) which will take them to a small form.
  - The user enters the name of the new category and presses 'Add'
  - The user is redirected back to the Categories lister with the new category added - the categories are listed alphabetically.
  
- A user wants to edit a category: 
  - The user must be already logged in.
  - Once logged in, the user can click the 'Manage Categories' button in the navbar.
  - The user clicks ['Edit'](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L184-L197) next to the category they want to edit, which will take them to a small [form](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/editcategory.html).
  - The user enters the new name of the category and presses 'Save Changes'
  - The user is redirected back to the Categories lister with the edited category displayed - the categories are listed alphabetically.
  
- A user wants to delete a category:
  - The user must be already logged in.
  - Once logged in, the user can click the 'Manage Categories' button in the navbar.
  - The user clicks ['Delete'](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L178-L181) next to the category they want to delete.
  - The user remains on the Categories lister and the category is deleted.
  
- A user wants to view a recipe:
  - On the homepage, or the My Recipes page (when logged in) the user can click on a recipe card to view the [recipe](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L152-L155) information. The [recipe card](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/recipe.html) contains information regarding ingredients, method, cooking time, preparation time, servings and the category as well as recipe name and image.
  
- A user wants to filter by category:
  - On the homepage, the user can click on the filters in the menu bar (i.e. Breakfast) to [filter by meal category](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L37-L47).
  - The user is redirected to a [filter page](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/filter.html) displaying only these meals.

- A user wants to log out:
  - Only applicable to logged in users
  - The user can click 'Log Out' in the navbar, they are [redirected to the homepage](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L90-L93).

## Wireframes created using Balsamiq:

### Homepage

![Wireframe / Site Diagram](static/images/wireframes/DCD_Homepage.png "Homepage")


### Add Category

![Wireframe / Site Diagram](static/images/wireframes/DCD_Add_Category.png "Add Category")


### Add Recipe

![Wireframe / Site Diagram](static/images/wireframes/DCD_Add_Recipe.png "Add Recipe")


### Categories

![Wireframe / Site Diagram](static/images/wireframes/DCD_Categories.png "Categories")


### Login

![Wireframe / Site Diagram](static/images/wireframes/DCD_Login.png "Login")


### Sign Up

![Wireframe / Site Diagram](static/images/wireframes/DCD_Sign_up.png "Sign Up")


### Recipe View

![Wireframe / Site Diagram](static/images/wireframes/DCD_Recipe_View.png "Recipe View")


### Search Results

![Wireframe / Site Diagram](static/images/wireframes/DCD_Search_Results.png "Search Results")

## Database Schema
![Wireframe / Site Diagram](static/images/database_schema/Database_Schema_mongo.png "Database Schema")

### Example schema from the 'recipes' collection:
```
{
    "_id": {
        "$oid": "5cbdf6f4e7179a264cf45ea0"
    },
    "cooking_time": "15 mins",
    "cuisine": "British",
    "method": "Bring a deep saucepan of water to the boil (at least 2 litres) and add the vinegar. Break the eggs into 4 separate coffee cups or ramekins. Split the muffins, toast them and warm some plates. Swirl the vinegared water briskly to form a vortex and slide in an egg. It will curl round and set to a neat round shape. Cook for 2-3 mins, then remove with a slotted spoon. Repeat with the other eggs, one at a time, re-swirling the water as you slide in the eggs. Spread some sauce on each muffin, scrunch a slice of ham on top, then top with an egg. Spoon over the remaining hollandaise and serve at once.",
    "ingredients": [
        "3 tbsp White Wine Vinegar",
        "2 Toasting Muffins",
        "4 Eggs",
        "4 slices Parma Ham",
        "1 batch Hollandaise sauce"
    ],
    "name": "Eggs Benedict",
    "image": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Eggs_Benedict-01-cropped.jpg",
    "added_by": "cskinner",
    "prep_time": "5 mins",
    "category": "Breakfast",
    "serves": "2"
}
```

## Features
 
### Existing Features
- The site uses basic user authentication to [create a user account](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L62-L75) and allow the user to [log in](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L50-L59) - the site is then accessible through the login/sign up functionality.
- Users can add a recipe by filling out the fields in the ['Add a Recipe'](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/addrecipe.html) form. The [data](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L102-L117) from this form is then used to construct the recipe card.
- View [recipe card](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/recipe.html) containing image and all information inputted in form including ingredients, method, cooking and preparation time etc.
- There is the ability to [Edit](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/editrecipe.html)/[Delete](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L146-L149) recipes you as a user have added - recipes are protected from deletion by anyone else as delete button only available to owner of recipe.
- A user can [Add](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/addcategory.html)/[Edit](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/editcategory.html)/[Delete](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py#L178-L181) categories

### Features Left to Implement
- Likes on recipes: Users can upvote recipes: I would add an additional field inside each MongoDB document for 'likes' and have this increment by 1 whenever the user clicks on the like button.
- Search bar to filter on keywords: I would add a search bar in the navigation area, which would allow the user to search for keywords featured in the ingredients array.
- For optimisation, I would move the logic behind the filtering of meals by category into the back-end of the project rather than filtering in the [front-end](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/templates/filter.html) 

## Technologies Used

- [Flask](http://flask.pocoo.org/)
    - The project uses **Flask** , a Python micro framework to provide a functional and lightweight core for the application

- [Jinja2](http://jinja.pocoo.org/docs/2.10/)
    - This app uses the **Jinja2** for the front-end templating of the routes outlined in the app.py file. 
    - Modelled on Django's templating style, **Jinja2** is scalable and modular to allow for reusable components

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - HTML used for the **structure** of the page templates

- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - Language used to apply styles to each page for **styling of the components** (e.g. colour schemes, fonts, images)
    
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - I have used Javascript in the add/edit recipe forms to power the logic behind the 'Add Ingredient' and 'Remove Ingredient' buttons. I have also used this to create a validation error for the Materialize select component as there is a known issue with this component showing error messages.
    - JS has also been used to power the sliding side menu action on smaller screen sizes
    
- [Materialize](https://materializecss.com/)
    - I have used Materialize throughout the project to create navbars, side menus, input types in forms and icons
   
- [MongoDB](https://mlab.com/welcome/)
    - I have used MLab to implement a **database** in this project. This is where all of the user, recipe and category data is stored.

## Testing
I included a piece of [automated testing](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/test_app.py) in the app to check whether the routing for the site was working correctly, this can be seen here The first test is for the homepage (index.html) - this looks for the response of the page (200, if the page is up for example) and then compares to see if this is equal to the 200 response status needed. If yes, the test passes. This works the same for the other tests, but for the login and signup pages.

### Manual Testing
- **User goes to the URL https://dcd-cookbook.herokuapp.com/ (Homepage):** _Homepage is up and showing a 200 response status in developer tools_
- **User who does not have an account tries to log in via the login page:** _Form data is posted to the users document - the username is not in the database so the user is redirected to the sign up page_
- **User who does have an account tries to log in via the login page:** _Form data is posted to the users document - the username is in the database so the hashed password is checked against that stored in the database. User is redirected to the My Recipes profile page as details are correct_
- **User wants to view a recipe:** _User clicks on a recipe card on the homepage (whether logged in or not) and they are redirected to the recipe details page with the url of /recipe/<recipe_id>_
- **User wants to filter recipes by category:** _User can click on any of the category buttons in the navbar to filter by this term (whether logged in or not). The user will be taken to a URL of /<category_name> and will display recipe cards that have the "category" field of that particular category._
- **User wants to add a recipe:** _If the user is not logged in, but tries to access the /add_recipe URL they will see a page that prompts them to log in to view content. If the user is logged in they can open the navbar and choose the option to 'Add Recipe'. This opens a page with a form they can complete with the required fields. The user must complete all fields in order for the form to post, validation error messages will show otherwise. Once all fields are complete, user clicks to add recipe and their recipe is displayed on their My Recipes profile page._
- **User wants to edit a recipe:** _If the user is not logged in, they will not be able to edit the recipe. If the user is logged in, they will see an edit button appear on the recipe card inside their My Recipes page. Only the owner of the recipe can edit the recipe. They are taken to a form pre-filled with the details of the recipe stored in the database. The user can edit the necessary fields (all fields must still be completed) and then they can save the changes. The edited recipe will be visible in their My Recipes page._
- **User wants to delete a recipe:** _If the user is not logged in, they will not be able to delete the recipe. If the user is logged in, they will see a delete button appear on the recipe card inside their My Recipes page. Only the owner of the recipe can delete the recipe. Once the delete button is clicked, the recipe is removed and the user stays on the My Recipes page._
- **User wants to manage categories:** _If the user is not logged in, they will not be able to manage the categories. If the user is logged in they will be able to choose the 'Manage Categories' option in the navbar._
- **User wants to edit a category:** _Same as the above. On the Manage Categories page the user can click the edit button next to the category they wish to edit. This takes the user to a small form where they can edit the name of the category. Upon saving changes the user is taken back to the /categories URL where all the categories are displayed alphabetically (a renamed recipe will result in the order rearranging alphabetically)_
- **User wants to delete a category:** _Same as above. On the Manage Categories page the user can click the delete button next to the category they wish to delete. This keeps the user on the /categories URL but the required category will be removed from the list._

## Bugs
At first, I was only implementing sessions by way of assigning a user a username to allow them to post/edit/delete recipes and categories. However my mentor made a good point that anyone is then technically able to create an account and delete recipes/categories that are not their own. To resolve this, I have implemented basic user authentication using [flask bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/). If the user tries to sign in and they have not created an account already, they will be redirected to the Sign Up page to do so. This is because the posted data in the login form will first check the users document to see if the username exists, and then that the hashed password matches. On the sign up page, the data is posted and the user's account is created. I have also hidden the content of certain pages from view if the username is not in the session data (this is replaced with a prompt for the user to login to view content) and have placed a conditional on the delete/edit recipe buttons so that these buttons only appear if the user that is logged in, is the owner of the recipe.

## Deployment

This application is hosted on Heroku at: https://dcd-cookbook.herokuapp.com/ In order to deploy this app to heroku, I added a [Procfile](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/Procfile) which tells heroku the language of the app and the name of the file that needs to be run - in this case this was [app.py](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/app.py)
I then set up a [requirements.txt](https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub/blob/master/requirements.txt) file which holds the dependencies that this app requires in order to run. Both the Procfile an requirements.txt file are committed to the repository and pushed to Heroku.

I had to set up some environment variables inside Heroku in order for the app to appear on the live URL. The following are configured under Settings -> Reveal Config Vars
  - IP: 0.0.0.0
  - PORT: 5000
  - MONGO_URI: This is set in the env.py file for use locally, but needs to be set in the config vars in heroku. It takes the format of mongodb://<db_user>:<db_password>@mongodb0.example.com:<port>/<db_name>

#### Run app locally
  - Clone this repository using ``` $ git clone <https://github.com/charlotteskinner90/dcd-milestone-project-recipe-hub.git> ```
  - Install dependencies required for the app to run from the requirements.txt file by running the following command in the terminal ```pip install -r requirements.txt```
  - Set your environment variables i.e. IP: 127.0.0.1 and PORT: 5000 to view the site in the browser.
  - Set debug to True at the very bottom of app.py when running locally, set to False when deployed to production.
  - Run the code in an IDE of your choice ```python app.py```
  - Follow the database instructions below to set up a database to use with this app.
  
#### Database setup
  - Create a MongoDB database in MLab named 'recipe_hub'
  - Add 'users', 'recipes' and 'categories' collections
  - Set the MONGO_URI as an app.config in the env.py file (you can find this inside the recipe_hub collection): mongodb://<db_user>:<db_password>@mongodb0.example.com:<port>/<db_name>
  
#### Deploying to Heroku
  - If you would like to deploy your own version to Heroku, first make sure that you have a Heroku account.
  - Log in to your Heroku account on the CLI ``` $ heroku login ```
  - Clone the repository ``` $ heroku git:clone -a dcd-cookbook ``` then ``` $ cd dcd-cookbook ```
  - Make your changes
  - Set the aforementioned environment variables in the Config Vars section of Heroku (under Settings) before deployment
  - Deploy to Heroku using git:
    - ``` $ git add . ```
    - ``` $ git commit -m "commit message" ```
    - ``` $ git push heroku master ```
  
#### Contributing
  - Make the desired changes to the app
  - If you feel the changes you have made to this app will benefit this project, please feel free to submit a pull request for consideration - thanks!


## Credits

### Content
 
- Logic behind making the validation error on the Materialize dropdown came from a solution I found on [Stack Overflow](https://stackoverflow.com/a/36806073)
- While researching how to create a button that creates new divs onclick, I came across this [Stack Overflow](https://stackoverflow.com/a/6678088) thread which explained how to use the .append() function to achieve this

### Media

Some example recipes have been obtained from [BBC Good Food](https://www.bbcgoodfood.com/)

### Acknowledgements

I would like to thank my mentor Anthony Ngene for his helpful feedback and support during this project.
