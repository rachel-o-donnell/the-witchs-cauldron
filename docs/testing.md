# Testing
Add a spell title that already exists
### Methodology

Manual tests were applied as I was building features to ensure all features added were as fully finished as needed at their respective stages. Any bugs found were either dealt with immediately or noted in READme for future fixing. Validators of affected/changed files /pages were rechecked after each bug fix after initial validation had begun

&nbsp;

#### Buttons and links
| Testing | Expected Outcome | Steps | Results |
|--------|---------|---------|---------|
| NAVBAR |
| Logo | Logo link brings you to the home page | Clicked logo link when on spell detail page | PASS |
| Magic Categories | Magic Categories dropdown features a list of categories | Clicked Magic Categories button | PASS |
| Magic Categories | Clicking the categories links will bring you to a page with all spells relating to that category | Added spells pertaining to each category, CLicked various categories, each time the page rendered spells that had been tagged with that category | PASS |
| Add Spell | Add a Spell brings you to a page where you can post a spell | Clicked Add a spell in Nabvar | PASS |
| Home | Home button takes you to the home page | Clicked Home in Nabvar | PASS |
| Sign In | Sign In takes you to a sign in page |  Clicked Sign In in Nabvar |PASS |
| Register | Register takes you to a register page |  Clicked Register in Nabvar |PASS |
| Logout | Logout takes you to a logout page |  Clicked Logged Out in  Nabvar |PASS |
| HOMEPAGE |
| Spell Title | Spell Title takes you to the spell detail page | Clicked Spell Title in home page | PASS |
| Footer |
| Fontawesome icons | Clicking Fontawesome icons opens the respective page in a new tab, LinkedIN and Github are linked to my own pages | Clicked each icon | PASS |
| Footer Logo | Footer Logo link brings you to the home page | Clicked footer logo | PASS |
| ADD A SPELL PAGE |
| Post | Clicking the post button on a valid form publishes the spell to the home page | Clicked the Post button on a valid form | PASS |
| SPELL DETAIL PAGE |
| Likes and comments favicons |
| Heart Favicon and counter | Heart Favicon changes to all black if you click and counter increases by 1 | Clicked on favicon | PASS |
| Heart Favicon and counter | Heart Favicon changes to black outline if you 'unlike' and counter decreases by 1 | Clicked on favicon | PASS |
| Heart Favicon and counter (Home page) | Heart Favicon appears all black only for the spells you have liked from the spell detail page and counter in showing and increasing/decreasing | Liked multiple random spells and checked on home page which ones were black and what count they had  | PASS |
| Comment Favicon and counter | Comment favicon appears on home page and spell detail page with a count denoting how many comments have been made on each post. Counter increases/decreases accordingly | Added and deleted comments | PASS |
| Edit and delete buttons | Edit and delete buttons only appear for a spell you have created |  Created a spell under one username - buttons appear, logged out and logg in as a different user - buttons do not appear on the same post , but do appear when I post a new spell with the 2nd user | PASS |
| EDIT A SPELL PAGE |
| Edit | Edit button brings you to edit a spell page | clicked on edit button | PASS |
| DELETE A SPELL PAGE |
| Delete | Delete button brings you to delte a spell page | clicked on delete button | PASS |
|COMMENTS |
| Post (COMMENTS)| Post button posts a comment and you stay on the same page | Clicked Post button after commenting in box | PASS | 
| Edit (COMMENTS)| Edit button pulls your comment into the body for you to re-edit edit a comment page | clicked on edit button | PASS |
| Update button (COMMENTS) | Comment is updated, user is brought to the home page | Posted a comment, edited it and pressed the update button | PASS |
| Delete (COMMENTS)|  Delete button brings you to the delete comment page  | clicked on delete button | PASS |
| 2nd Delete button (COMMENTS) | Comment is deleted and user is brough to the home page | Created and deleted a comment | PASS |

&nbsp;

### Hover features 
| Testing | Expected Outcome | Steps | Results |
|--------|---------|---------|---------|
| HOME PAGE |
| NAVBAR |
| Logo | Logo | -
| Magic Categories | Magic Categories button changes color when hovered over | hovered over dropdown button | PASS |
| Home | Home button changes color when hovered over | hovered over home button | PASS |
| Add Spell | Add Spell changes color when hovered over | hovered over Add Spell | PASS |
| Sign In | Sign In changes color when hovered over | hovered over Sign In  PASS |
| Register | Register changes color when hovered over | hovered over Register | PASS |
| Logout | Logout changes color when hovered over | hovered over Logout | PASS |
| SPELL DISPLAYS |
| Spell Title |  Spell Title changes color when hovered over | hovered over Spell Title | PASS |
| SPELL DETAIL PAGE |
| Edit | Post button changes color when hovered over | hovered over edit button | PASS |
| Delete | Delete button changes color when hovered over | hovered over delete | PASS |
|COMMENTS |
| Post (COMMENTS)| Post button changes color when hovered over | hovered over Post button | PASS |
| Update (COMMENTS) | Update button changes color when hovered over | hovered over Update button |PASS 
| Delete (COMMENTS)|  Delete button changes color when hovered over | hovered over delete button | PASS |
| 2nd Delete button (COMMENTS) | Delete button changes color when hovered over | hovered over delete button | PASS |
| ADD A SPELL PAGE |
| Post | Post button changes color when hovered over | hovered over Post button | PASS |
| EDIT A SPELL PAGE |
| Update | Update button changes color when hovered over | hovered over Update button | PASS |
| Delete | Delete button changes color when hovered over | hovered over Delete button | PASS |
| SIGN IN PAGE |
| Sign In | Sign In changes color when hovered over | hovered over Sign In |  |
| REGISTER PAGE |
| Register | Register changes color when hovered over | hovered over Register |  |
| LOGOUT PAGE |
| Logout | Logout changes color when hovered over | hovered over Logout |  |

&nbsp;

#### ERROR PAGES 
| Testing | Expected Outcome | Steps | Results |
|--------|---------|---------|---------|
| 404 |  404 Error page appears when page request does not exist | entered /help at the end of the http | PASS
| 500 | 500 Error page appears when there is a server error | | UNTESTED |
| 403 | 403 Error page appears when user tries to acces a page they are not allowed | Added edit_comment/1 to end of hhtp address when signed in as a different user than the author of the comment | PASS |

&nbsp;

#### FORMS 

#### ADD A SPELL
| Testing | Expected Outcome | Steps | Results |
|--------|---------|---------|---------|
| Form Validation EMPTY | Form validation will prompt for user action if empty form is submitted |   Try to submit empty form | PASS |
| Form Validation TITLE | Form validation will prompt for user action to fill content if only title is filled |  Try to submit only title  | PASS |
| Form Validation TITLE AND CONTENT | Post Will be uploaded and user returned to homepage, default category will be general| Try to submit only title and content | PASS |
| Form Validation ALL DETAILS | Fill all details of form | User returned to homepage and post is displayed with all relavant info on home page and all extra details on the spell detail page, post appears in relavant category search | PASS |
| COMMENTS |
| Post (COMMENTS)| Post button posts a comment and you stay on the same page | Clicked Post button after commenting in box | PASS |

&nbsp;

### FORM VIEWS 
| Testing | Expected Outcome | Steps | Results |
|--------|---------|---------|---------|
| Posts display on home page |
| Title | Title appears on card on home page | Added a ttile to the form | PASS |
| Description(spell overview -if any) | Description(spell overview -if any)appears on card on home page | Added a description to the form| PASS |
| Likes icon and count | Likes icon and count appear on card on home page | like a post | PASS |
| Comments icon and count | Comments icon and count appear on card on home page | comment on a post | PASS |
| Creator | Creator name is posted depending on who has written the spell | created different spells using different loggins | PASS |
| Posted on | Posted on appears on the card and is true to time and date posted | posted a spell | PASS |
| Posts display on Spell Detail page |
| Title | Title appears on card on spell detail page | Added a ttile to the form | PASS |
| Description(spell overview -if any) | Description(spell overview -if any)appears on card on spell detail page | Added a description to the form| PASS |
| Likes icon and count | Likes icon and count appear in correct sectionon spell detail page | like a post | PASS |
| Comments icon and count | Comments icon and count appear in correct sectionon spell detail page | comment on a post | PASS |
| Creator | Creator name is posted depending on who has written the spell | created different spells using different loggins | PASS |
| Posted on | Posted on appears on spell detail and is true to time and date posted | posted a spell | PASS |
| Items needed | Items needed  appear in correct section on spell detail page | added items needed| PASS |
| Content | Items needed appear in correct section on spell detail page| added content | PASS |

&nbsp;

#### Messaages: PASS
| Testing | Expected Outcome | Steps | Results |
|--------|---------|---------|---------|
| SIGN IN etc |
| Sign In | Sign In message appears in banner |  Signed In  PASS |
| Register | Register message appears in banner |  Registered as new User | PASS |
| Logout | Logout message appears in banner |  Logged out | PASS |
| SPELLS|
| Add Spell | Your Spell was deleted message appears | Added a spell | PASS |
| Edit Spell | Your Spell was edited message appears | Edited a spell | PASS |
| Delete Spell | Your Spell was deleted message appears | Deleted a spell | PASS |
| COMMENTS |
| Add Comment | Your Comment was deleted message appears | Added a comment | PASS |
| Edit Comment | Your Comment was edited message appears | Edited a comment | PASS |
| Delete Comment | Your Comment was deleted message appears | Deleted a comment | PASS |

&nbsp;


#### Responsiveness 
| Testing | Results |
|--------|---------|
| Navbar - goes to burger | PASS |
| footer - change to m-0 around social fontawesome icons | PASS |
| Home Page - fully responsive | PASS |
| Spell Detail Page | PASS |
| Add Spell | PASS |
| Edit Spell | PASS |
| Delete Spell | PASS |
| Edit Comment  | PASS |
| Delete Comment | PASS |
| Categories page | PASS |
| 500 | PASS | 
| 403 | PASS | 
| 404 | PASS | 

| Register | NOT STYLED but responsive |
| Loggout | NOT STYLED but responsive |
| Login | NOT STYLED but responsive |


&nbsp;

## Code Validation

### HTML
Wc3 HTML - All pages pass without error apart from Add Spell(see below)

Errors coming from Summernote's code regarding the summernote widget - I did remove the widgets and this solved the problem but then the form would not register things like a new line, bullet points etc. So I've decided to add it back as otherise the posts could end up affectign the UX terribly. 

Most of the errors are from the same issues that are repeated with each form but I set the width to 100% in settings.py to make it responsive and that added another error but that is the only solution I found. 

### PYTHON
Pycodestyle? - pep 8 replacement

Pep8CI - all files pass without error

Conflicts arise with pythonchecker and imported python linter in terminal. I've gone with what the terminal has suggested.

### CSS 
Jigsaw Wc3 validation - passes without error

&nbsp;

### Lighthouse 


Return to [README.md]() ADD LINK