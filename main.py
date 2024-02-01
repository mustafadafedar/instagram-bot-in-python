# first install instabot (pip install instabot)
# acc means account

'''self.cookie_dict["urlgen"]
KeyError: 'urlgen 
(if you are getting this error uncomment bellows code  '''

# import os
# import shutil


# def clean_up(i):
#     dir = "config"
#     remove_me = "imgs\{}.REMOVE_ME".format(i)
#     # checking whether config folder exists or not
#     if os.path.exists(dir):
#         try:
#             # removing it so we can upload new image
#             shutil.rmtree(dir)
#         except OSError as e:
#             print("Error: %s - %s." % (e.filename, e.strerror))
#     if os.path.exists(remove_me):
#         src = os.path.realpath("imgs\{}".format(i))
#         os.rename(remove_me, src)


# def upload_post(i):
#     bot = Bot()

#     bot.login(username="your_username", password="your_password")
#     bot.upload_photo("imgs/{}".format(i), caption="Caption for the post")


# if __name__ == '__main__':
#     # enter name of your image bellow
#     image_name = "img.jpg"
#     clean_up(image_name)
#     upload_post(image_name)


from instabot import Bot
bot = Bot()
bot.login(username="add username ", password="add password")

# follow someone using follow method
bot.follow('acc you want to follow')

# upload photo
bot.upload_photo("add/path/of/photo",caption=" add caption")

# # unfollow account
bot.unfollow("acc u want to unfollow")

# # message multiple accounts
bot.send_message("add mesage",["1st username","2nd username","3rd username","etc"])

# see directly about your followers
followers = bot.get_user_followers("add username of your acc") 
for follower in followers:
    print(bot.get_user_info(follower))
    
# # see directly about your followings
following = bot.get_user_following("add username of your acc")
for Following in following:
    print(bot.get_user_info(following))

