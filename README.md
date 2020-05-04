# Social statistics collection
This program can help you with analyzing posts in your social networks and show the core of your fans.


## How to install

Python3 have to be already installed. Then use pip (or pip3, there is a contravention with Python2) to install dependencies:
```
git clone https://github.com/djeck1432/amplifer.git
```
After you downloaded the repository open a folder `amplifier` using next command:
```
cd amplifier
```
Now all of the required libraries and modules have to be installed:
```
pip install -r requirements.txt
```
Now we are ready for the script.

## How to start 
For start, code do the next command in the terminal:
```
python smm_analyze.py [social network]
```
`Instagram` - instagram;

`Facebook` - facebook;

`Vkontakte` - vkontakte;

Launch example:
```
python smm_analyze.py instagram
```


## Environment variables 

`INSTAGRAM_LOGIN` - login to`Instagram`;

`INSTAGRAM_PASSWORD` - password to `Instagram`;

`INSTAGRAM_ACCAUNT` - username to  `Instagram`;


`VK_TOKEN` - token `Vkontakte`;

`VK_GROUP_NAME `- group name `Vkontakte`;

`VK_POSTS_AMOUNT` - amount of post;


`FACEBOOK_TOKEN`- token `Facebook`;

`FACEBOOK_GROUP_ID` - `id` group on  `Facebook`;
